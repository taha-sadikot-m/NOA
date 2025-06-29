from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
import os
from datetime import datetime
import re
import sqlite3
from functools import wraps
from config import Config
from supabase_service import get_supabase_service

app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config['DATABASE'] = Config.DATABASE

def init_db():
    """Initialize database (SQLite fallback)"""
    if Config.USE_SUPABASE:
        try:
            supabase_service = get_supabase_service()
            supabase_service.create_tables()
            print("Supabase tables initialized")
            return
        except Exception as e:
            print(f"Supabase initialization failed: {e}")
            print("Falling back to SQLite...")
    
    # SQLite fallback
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("SQLite database initialized")

def get_db_connection():
    """Get database connection (SQLite fallback)"""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Main landing page"""
    return render_template('index.html')

@app.route('/features')
def features():
    """Features page"""
    return render_template('features.html')

@app.route('/pricing')
def pricing():
    """Pricing page"""
    return render_template('pricing.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

@app.route('/admin')
def admin():
    """Admin dashboard"""
    return render_template('admin.html')

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    """Handle email subscription (redirects to API endpoint)"""
    if request.method == 'POST':
        # Redirect to API endpoint
        return redirect(url_for('api_subscribe'), code=307)
    return redirect(url_for('index'))

@app.route('/api/subscribe', methods=['POST'])
def api_subscribe():
    """Handle email subscription"""
    try:
        email = request.form.get('Newsletter-Email-2')
        if not email:
            return jsonify({'success': False, 'message': 'Email is required'}), 400
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({'success': False, 'message': 'Invalid email format'}), 400
        
        # Try Supabase first
        if Config.USE_SUPABASE:
            try:
                supabase_service = get_supabase_service()
                result = supabase_service.add_subscription(email)
                return jsonify(result)
            except Exception as e:
                print(f"Supabase error: {e}")
                # Fall back to SQLite
        
        # SQLite fallback
        conn = get_db_connection()
        existing = conn.execute('SELECT id FROM subscriptions WHERE email = ?', (email,)).fetchone()
        
        if existing:
            conn.close()
            return jsonify({'success': False, 'message': 'Email already subscribed'}), 400
        
        conn.execute('INSERT INTO subscriptions (email) VALUES (?)', (email,))
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True, 
            'message': 'Thank you! Your submission has been received!'
        })
    except Exception as e:
        return jsonify({'success': False, 'message': 'Something went wrong'}), 500

@app.route('/api/contact', methods=['POST'])
def contact_form():
    """Handle contact form"""
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if not all([name, email, message]):
            return jsonify({'success': False, 'message': 'All fields are required'}), 400
        
        # Try Supabase first
        if Config.USE_SUPABASE:
            try:
                supabase_service = get_supabase_service()
                result = supabase_service.add_contact_message(name, email, message)
                return jsonify(result)
            except Exception as e:
                print(f"Supabase error: {e}")
                # Fall back to SQLite
        
        # SQLite fallback
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO contact_messages (name, email, message)
            VALUES (?, ?, ?)
        ''', (name, email, message))
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True, 
            'message': 'Thank you for your message! We\'ll get back to you soon.'
        })
    except Exception as e:
        return jsonify({'success': False, 'message': 'Something went wrong'}), 500

# Admin routes for viewing data (optional - for development)
@app.route('/admin/subscriptions')
def admin_subscriptions():
    """Admin view of subscriptions"""
    if Config.USE_SUPABASE:
        try:
            supabase_service = get_supabase_service()
            subscriptions = supabase_service.get_subscriptions()
            return jsonify(subscriptions)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    # SQLite fallback
    conn = get_db_connection()
    subscriptions = conn.execute('SELECT * FROM subscriptions ORDER BY created_at DESC').fetchall()
    conn.close()
    return jsonify([dict(sub) for sub in subscriptions])

@app.route('/admin/contacts')
def admin_contacts():
    """Admin view of contact messages"""
    if Config.USE_SUPABASE:
        try:
            supabase_service = get_supabase_service()
            messages = supabase_service.get_contact_messages()
            return jsonify(messages)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    # SQLite fallback
    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM contact_messages ORDER BY created_at DESC').fetchall()
    conn.close()
    return jsonify([dict(msg) for msg in messages])

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Initialize database
with app.app_context():
    init_db()

# For Vercel deployment - remove the main block
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000) 