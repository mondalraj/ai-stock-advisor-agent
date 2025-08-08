"""
Configuration management for the AI Stock Advisor Agent.
Handles environment variables and application settings.
"""

import os
from dotenv import load_dotenv

class Config:
    """Configuration manager for the application."""
    
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Gemini AI Configuration
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.gemini_model = "gemini-1.5-flash"  # Fastest model
        self.gemini_temperature = 0.1  # Lower for faster, focused responses
        self.gemini_max_tokens = 500   # Limit for faster response
        self.gemini_top_p = 0.8       # Reduce randomness for speed
        
        # Application Settings
        self.app_name = "🤖 INTELLIGENT STOCK RESEARCH AGENT"
        self.welcome_message = """Hello! I'm your AI-powered stock research assistant.
I can help you with various stock-related tasks and will ask
intelligent questions based on what you want to accomplish."""
        
        # Exit commands
        self.exit_commands = ['quit', 'exit', 'stop', 'bye']
    
    @property
    def has_valid_api_key(self) -> bool:
        """Check if a valid API key is configured."""
        return (self.gemini_api_key and 
                self.gemini_api_key != "your_gemini_api_key_here")
    
    def get_gemini_config(self) -> dict:
        """Get Gemini configuration parameters."""
        return {
            "model": self.gemini_model,
            "google_api_key": self.gemini_api_key,
            "temperature": self.gemini_temperature,
            "max_tokens": self.gemini_max_tokens,
            "top_p": self.gemini_top_p,
        }
