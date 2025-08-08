"""
Question generator that handles both AI and fallback question generation.
Provides a unified interface for generating questions based on user goals.
"""

from typing import List, Dict, Any

from .gemini_client import GeminiClient
from ..fallback.questions import FallbackQuestionGenerator
from ..utils.config import Config

class QuestionGenerator:
    """Unified question generator with AI and fallback capabilities."""
    
    def __init__(self, config: Config):
        self.config = config
        self.gemini_client = GeminiClient(config)
        self.fallback_generator = FallbackQuestionGenerator()
    
    def generate_questions(self, user_goal: str) -> List[Dict[str, Any]]:
        """Generate questions using AI if available, otherwise use fallback."""
        # Check for exit commands
        if user_goal.lower().strip() in self.config.exit_commands:
            return []
        
        if self.gemini_client.is_enabled:
            print("🧠 Consulting Gemini AI (via LangChain) for optimal questions...")
            try:
                return self.gemini_client.generate_questions(user_goal)
            except Exception as e:
                print(f"⚠️ AI generation failed, using smart fallback")
                return self.fallback_generator.generate_questions(user_goal)
        else:
            print("📋 Using smart fallback questions based on your goal...")
            return self.fallback_generator.generate_questions(user_goal)
    
    @property
    def is_ai_enabled(self) -> bool:
        """Check if AI question generation is available."""
        return self.gemini_client.is_enabled
