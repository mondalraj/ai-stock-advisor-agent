"""
State management for the Dynamic Stock Agent.
Defines the state structure and type annotations for the LangGraph workflow.
"""

from typing import TypedDict, List, Dict

class AgentState(TypedDict):
    """State definition for the dynamic stock screener agent."""
    # User input
    user_goal: str
    current_question_index: int
    user_answers: Dict[str, str]
    
    # AI-generated questions
    questions_list: List[Dict[str, str]]
    questions_generated: bool
    
    # Conversation state
    current_step: str
    all_complete: bool
    messages: List[str]
