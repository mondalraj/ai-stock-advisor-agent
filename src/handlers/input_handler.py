"""
Input handler for managing user interactions.
Handles user input with proper error handling and validation.
"""

from typing import Optional

class InputHandler:
    """Handles user input with proper error handling."""
    
    @staticmethod
    def get_user_goal() -> str:
        """Get the user's goal with error handling."""
        try:
            goal = input("\n💬 What would you like to do today? ").strip()
            return goal
        except EOFError:
            # For automated testing or pipe input
            goal = "Find good stocks to invest in"
            print(goal)
            return goal
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for using the Dynamic Stock Agent!")
            return "quit"
    
    @staticmethod
    def get_answer(question_text: str, question_id: str) -> str:
        """Get user answer to a specific question."""
        try:
            answer = input("\n💬 Your answer: ").strip()
            return answer
        except EOFError:
            # For automated testing, provide a default answer
            answer = f"Default answer for {question_id}"
            print(answer)
            return answer
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for using the Dynamic Stock Agent!")
            return "quit"
    
    @staticmethod
    def is_exit_command(text: str, exit_commands: list) -> bool:
        """Check if the input text is an exit command."""
        return text.lower().strip() in exit_commands
