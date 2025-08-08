"""
Output handler for managing display and formatting.
Handles all user-facing output with consistent formatting.
"""

from typing import List, Dict, Any
from ..utils.helpers import format_conversation_summary

class OutputHandler:
    """Handles output formatting and display."""
    
    def __init__(self, app_name: str, welcome_message: str):
        self.app_name = app_name
        self.welcome_message = welcome_message
    
    def show_welcome(self):
        """Display the welcome message."""
        print("\n" + "="*60)
        print(self.app_name)
        print("="*60)
        print(self.welcome_message)
        print("-"*60)
        print("💡 Tip: Type 'quit', 'exit', or 'stop' to end the session")
    
    def show_thinking_message(self):
        """Display thinking message."""
        print("\n🤔 Let me think about what information I need...")
    
    def show_question(self, question: Dict[str, str], current_index: int, total_questions: int):
        """Display a question to the user."""
        print(f"\n📝 Question {current_index + 1} of {total_questions}")
        print("-" * 40)
        print(f"🎯 {question['question']}")
    
    def show_completion_summary(self, user_goal: str, questions: List[Dict[str, str]], 
                               answers: Dict[str, str]):
        """Display the completion summary."""
        print("\n" + "="*60)
        print("✅ INFORMATION GATHERING COMPLETE!")
        print("="*60)
        
        summary = format_conversation_summary(user_goal, answers, questions)
        print(summary)
        
        print("🚀 Ready to proceed with intelligent stock analysis!")
        print("=" * 60)
    
    def show_final_results(self, result: Dict[str, Any]):
        """Display final results summary."""
        print("\n" + "="*60)
        print("✅ DYNAMIC CONVERSATION PHASE COMPLETED")
        print("="*60)
        print("Next: Implement intelligent analysis based on collected information...")
        print(f"📝 Goal achieved: {result.get('goal', 'N/A')}")
        print(f"📋 Questions answered: {len(result.get('answers', {}))}")
        
        # Show what data we collected for the next phase
        print("\n🔍 Collected Information for Analysis:")
        for q_id, answer in result.get('answers', {}).items():
            print(f"   • {q_id}: {answer}")
    
    def show_success_message(self):
        """Display success message."""
        print("\n🎉 Dynamic conversation completed successfully!")
        print("📊 All information gathered based on your specific goal.")
    
    def show_error_message(self, error: Exception):
        """Display error message."""
        print(f"\n❌ Error during conversation: {error}")
    
    def show_goodbye(self):
        """Display goodbye message."""
        print("\n\n👋 Goodbye! Thanks for using the Dynamic Stock Agent!")
