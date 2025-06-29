from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Noa is working!',
        'environment': os.environ.get('VERCEL', 'local')
    })

@app.route('/test')
def test():
    return jsonify({
        'status': 'success',
        'message': 'Test endpoint working!'
    })

if __name__ == '__main__':
    app.run(debug=True) 