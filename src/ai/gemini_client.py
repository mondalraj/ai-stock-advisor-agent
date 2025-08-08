"""
Gemini AI client using LangChain integration.
Handles communication with Google's Gemini model for question generation.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from typing import Optional, List, Dict, Any
import json
import time

from ..utils.config import Config
from ..utils.helpers import clean_json_response, validate_question_structure

class GeminiClient:
    """Client for interacting with Gemini AI via LangChain."""
    
    def __init__(self, config: Config):
        self.config = config
        self.llm: Optional[ChatGoogleGenerativeAI] = None
        self.is_enabled = False
        
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the Gemini client if API key is available."""
        if self.config.has_valid_api_key:
            try:
                self.llm = ChatGoogleGenerativeAI(**self.config.get_gemini_config())
                self.is_enabled = True
                print("✅ Gemini AI enabled via LangChain (optimized for speed)")
            except Exception as e:
                print(f"⚠️ Failed to initialize Gemini client: {e}")
                self.is_enabled = False
        else:
            print("⚠️ No valid Gemini API key found (set GEMINI_API_KEY for AI-powered questions)")
            self.is_enabled = False
    
    def generate_questions(self, user_goal: str) -> List[Dict[str, Any]]:
        """Generate questions using Gemini AI."""
        if not self.is_enabled or not self.llm:
            raise RuntimeError("Gemini client is not properly initialized")
        
        # Create optimized messages for question generation
        system_message = SystemMessage(content=self._get_system_prompt())
        human_message = HumanMessage(content=f"User goal: {user_goal}")
        
        # Measure response time
        start_time = time.time()
        
        try:
            # Invoke the model
            messages = [system_message, human_message]
            response = self.llm.invoke(messages)
            
            elapsed_time = time.time() - start_time
            
            # Process response
            response_text = response.content.strip()
            json_text = clean_json_response(response_text)
            questions = json.loads(json_text)
            
            # Validate structure
            if not validate_question_structure(questions):
                raise ValueError("Generated questions don't match required structure")
            
            print(f"✅ Generated {len(questions)} AI-powered questions ({elapsed_time:.2f}s)!")
            return questions
            
        except Exception as e:
            elapsed_time = time.time() - start_time
            print(f"⚠️ AI generation failed after {elapsed_time:.2f}s: {str(e)[:50]}...")
            raise e
    
    def _get_system_prompt(self) -> str:
        """Get the optimized system prompt for question generation."""
        return """You are an expert stock analyst. Generate 3-4 essential questions for stock research based on the user's goal. 

IMPORTANT: Respond ONLY with valid JSON array. No explanations, no markdown, no extra text.

Format:
[
  {"id": "short_id", "question": "clear question?", "purpose": "brief purpose"},
  {"id": "market", "question": "Which markets interest you?", "purpose": "scope"}
]

Requirements:
- Questions must be specific to the goal
- Use natural, conversational language
- Cover key aspects: market, preferences, criteria, timeline
- Keep questions concise for fast responses"""
