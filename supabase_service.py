from supabase import create_client, Client
from config import Config
import logging
from datetime import datetime
from typing import Dict, List, Optional

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SupabaseService:
    """Service class for Supabase operations"""
    
    def __init__(self):
        """Initialize Supabase client"""
        if not Config.USE_SUPABASE:
            raise ValueError("Supabase credentials not configured")
        
        self.supabase: Client = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)
    
    def create_tables(self):
        """Create necessary tables in Supabase (run this once)"""
        try:
            # Create subscriptions table
            self.supabase.table('subscriptions').select('*').limit(1).execute()
            logger.info("Subscriptions table already exists")
        except Exception as e:
            logger.info("Creating subscriptions table...")
            # Note: In Supabase, tables are typically created via the dashboard
            # This is just a check to ensure the table exists
        
        try:
            # Create contact_messages table
            self.supabase.table('contact_messages').select('*').limit(1).execute()
            logger.info("Contact messages table already exists")
        except Exception as e:
            logger.info("Creating contact messages table...")
            # Note: In Supabase, tables are typically created via the dashboard
            # This is just a check to ensure the table exists
    
    def add_subscription(self, email: str) -> Dict:
        """Add a new email subscription"""
        try:
            # Check if email already exists
            existing = self.supabase.table('subscriptions').select('id').eq('email', email).execute()
            
            if existing.data:
                return {'success': False, 'message': 'Email already subscribed'}
            
            # Insert new subscription
            result = self.supabase.table('subscriptions').insert({
                'email': email,
                'created_at': datetime.utcnow().isoformat()
            }).execute()
            
            if result.data:
                return {'success': True, 'message': 'Thank you! Your submission has been received!'}
            else:
                return {'success': False, 'message': 'Failed to add subscription'}
                
        except Exception as e:
            logger.error(f"Error adding subscription: {str(e)}")
            return {'success': False, 'message': 'Something went wrong'}
    
    def add_contact_message(self, name: str, email: str, message: str) -> Dict:
        """Add a new contact message"""
        try:
            result = self.supabase.table('contact_messages').insert({
                'name': name,
                'email': email,
                'message': message,
                'created_at': datetime.utcnow().isoformat()
            }).execute()
            
            if result.data:
                return {'success': True, 'message': 'Thank you for your message! We\'ll get back to you soon.'}
            else:
                return {'success': False, 'message': 'Failed to send message'}
                
        except Exception as e:
            logger.error(f"Error adding contact message: {str(e)}")
            return {'success': False, 'message': 'Something went wrong'}
    
    def get_subscriptions(self, limit: int = 100) -> List[Dict]:
        """Get all subscriptions (for admin purposes)"""
        try:
            result = self.supabase.table('subscriptions').select('*').order('created_at', desc=True).limit(limit).execute()
            return result.data
        except Exception as e:
            logger.error(f"Error getting subscriptions: {str(e)}")
            return []
    
    def get_contact_messages(self, limit: int = 100) -> List[Dict]:
        """Get all contact messages (for admin purposes)"""
        try:
            result = self.supabase.table('contact_messages').select('*').order('created_at', desc=True).limit(limit).execute()
            return result.data
        except Exception as e:
            logger.error(f"Error getting contact messages: {str(e)}")
            return []
    
    def delete_subscription(self, email: str) -> Dict:
        """Delete a subscription (for admin purposes)"""
        try:
            result = self.supabase.table('subscriptions').delete().eq('email', email).execute()
            return {'success': True, 'message': 'Subscription deleted'}
        except Exception as e:
            logger.error(f"Error deleting subscription: {str(e)}")
            return {'success': False, 'message': 'Failed to delete subscription'}

# Global instance
supabase_service = None

def get_supabase_service() -> Optional[SupabaseService]:
    """Get Supabase service instance"""
    global supabase_service
    if Config.USE_SUPABASE:
        if supabase_service is None:
            supabase_service = SupabaseService()
        return supabase_service
    return None 