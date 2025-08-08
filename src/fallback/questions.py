"""
Fallback question generator for when AI is unavailable.
Provides smart, context-aware questions based on user goals.
"""

from typing import List, Dict, Any

class FallbackQuestionGenerator:
    """Generate fallback questions when AI is not available."""
    
    @staticmethod
    def generate_questions(user_goal: str) -> List[Dict[str, Any]]:
        """Generate optimized fallback questions based on user goal."""
        goal_lower = user_goal.lower()
        
        # Core questions that work for most goals (optimized for speed)
        base_questions = [
            {
                "id": "market", 
                "question": "Which markets interest you most?", 
                "purpose": "Geographic scope"
            },
            {
                "id": "style", 
                "question": "Describe your investment style and risk tolerance?", 
                "purpose": "Risk profile"
            },
            {
                "id": "criteria", 
                "question": "What specific criteria should I focus on?", 
                "purpose": "Selection criteria"
            }
        ]
        
        # Add one contextual question based on goal (faster than multiple checks)
        contextual_question = FallbackQuestionGenerator._get_contextual_question(goal_lower)
        if contextual_question:
            base_questions.append(contextual_question)
        
        return base_questions
    
    @staticmethod
    def _get_contextual_question(goal_lower: str) -> Dict[str, str]:
        """Get a contextual question based on goal keywords."""
        if any(word in goal_lower for word in ['dividend', 'income', 'yield']):
            return {
                "id": "income", 
                "question": "What dividend yield or income level do you target?", 
                "purpose": "Income requirements"
            }
        elif any(word in goal_lower for word in ['growth', 'best', 'top']):
            return {
                "id": "growth", 
                "question": "What defines 'good performance' for you?", 
                "purpose": "Success metrics"
            }
        elif any(word in goal_lower for word in ['budget', 'cheap', 'price']):
            return {
                "id": "budget", 
                "question": "Any price range or budget considerations?", 
                "purpose": "Financial constraints"
            }
        else:
            return {
                "id": "timeline", 
                "question": "What's your investment timeline?", 
                "purpose": "Time horizon"
            }
