import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for the Flask app"""
    
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'noa-secret-key-2024')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    
    # Supabase Configuration
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
    
    # Database Configuration (fallback to SQLite if Supabase not configured)
    USE_SUPABASE = bool(SUPABASE_URL and SUPABASE_KEY)
    DATABASE = 'noa_database.db'  # Fallback SQLite database 