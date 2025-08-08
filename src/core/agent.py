"""
Main Dynamic Stock Agent class.
Orchestrates the conversation flow and manages the overall agent behavior.
"""

from typing import Dict, Any, Optional

from .state import AgentState
from .workflow import WorkflowBuilder
from ..ai.question_generator import QuestionGenerator
from ..handlers.input_handler import InputHandler
from ..handlers.output_handler import OutputHandler
from ..utils.config import Config

class DynamicStockAgent:
    """Main agent class that orchestrates the stock research conversation."""
    
    def __init__(self):
        # Initialize components
        self.config = Config()
        self.question_generator = QuestionGenerator(self.config)
        self.input_handler = InputHandler()
        self.output_handler = OutputHandler(
            self.config.app_name, 
            self.config.welcome_message
        )
        
        # Build workflow
        workflow_builder = WorkflowBuilder(self)
        self.graph = workflow_builder.build_workflow()
        
        print("🚀 Initializing Dynamic Stock Research Agent...")
    
    def run(self) -> Optional[Dict[str, Any]]:
        """Run the dynamic stock agent."""
        initial_state = {
            "user_goal": "",
            "current_question_index": 0,
            "user_answers": {},
            "questions_list": [],
            "questions_generated": False,
            "current_step": "",
            "all_complete": False,
            "messages": []
        }
        
        try:
            result = self.graph.invoke(initial_state)
            
            if result.get("all_complete"):
                self.output_handler.show_success_message()
                
                # Return structured data for next phase
                return {
                    "goal": result["user_goal"],
                    "answers": result["user_answers"],
                    "questions": result["questions_list"]
                }
            
            return result
            
        except Exception as e:
            self.output_handler.show_error_message(e)
            return None
    
    # Node functions for the LangGraph workflow
    def _ask_goal_node(self, state: AgentState) -> AgentState:
        """Ask the user what they want to accomplish today."""
        self.output_handler.show_welcome()
        
        goal = self.input_handler.get_user_goal()
        
        return {
            **state,
            "user_goal": goal,
            "current_step": "goal_collected",
            "messages": state.get("messages", []) + [f"User goal: {goal}"]
        }
    
    def _generate_questions_node(self, state: AgentState) -> AgentState:
        """Generate questions using AI or fallback methods."""
        user_goal = state['user_goal']
        
        # Handle exit commands
        if self.input_handler.is_exit_command(user_goal, self.config.exit_commands):
            return {**state, "questions_list": [], "all_complete": True}
        
        self.output_handler.show_thinking_message()
        
        # Generate questions
        questions = self.question_generator.generate_questions(user_goal)
        
        return {
            **state,
            "questions_list": questions,
            "questions_generated": True,
            "current_question_index": 0,
            "user_answers": {},
            "current_step": "questions_ready",
            "messages": state.get("messages", []) + [f"Generated {len(questions)} questions"]
        }
    
    def _ask_question_node(self, state: AgentState) -> AgentState:
        """Ask the current question from the generated list."""
        questions = state["questions_list"]
        current_index = state["current_question_index"]
        
        if current_index >= len(questions):
            return state  # Safety check
        
        current_q = questions[current_index]
        
        # Display question
        self.output_handler.show_question(current_q, current_index, len(questions))
        
        # Get answer
        answer = self.input_handler.get_answer(current_q['question'], current_q['id'])
        
        # Handle exit during question answering
        if self.input_handler.is_exit_command(answer, self.config.exit_commands):
            return {**state, "all_complete": True}
        
        # Update user answers
        updated_answers = state["user_answers"].copy()
        updated_answers[current_q["id"]] = answer
        
        return {
            **state,
            "user_answers": updated_answers,
            "current_question_index": current_index + 1,
            "current_step": f"answered_q{current_index + 1}",
            "messages": state.get("messages", []) + [f"Q{current_index + 1}: {answer}"]
        }
    
    def _complete_node(self, state: AgentState) -> AgentState:
        """Complete the conversation and summarize collected information."""
        self.output_handler.show_completion_summary(
            state['user_goal'],
            state["questions_list"],
            state["user_answers"]
        )
        
        return {
            **state,
            "all_complete": True,
            "current_step": "complete",
            "messages": state.get("messages", []) + ["Conversation completed"]
        }
