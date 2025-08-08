"""
LangGraph workflow builder for the Dynamic Stock Agent.
Defines the graph structure and conditional logic.
"""

from typing import Literal
from langgraph.graph import StateGraph, END

from .state import AgentState

class WorkflowBuilder:
    """Builds the LangGraph workflow for the stock agent."""
    
    def __init__(self, agent_instance):
        """Initialize with reference to the agent instance for node functions."""
        self.agent = agent_instance
    
    def build_workflow(self) -> StateGraph:
        """Build and compile the LangGraph workflow."""
        workflow = StateGraph(AgentState)
        
        # Add nodes
        workflow.add_node("ask_goal", self.agent._ask_goal_node)
        workflow.add_node("generate_questions", self.agent._generate_questions_node)
        workflow.add_node("ask_question", self.agent._ask_question_node)
        workflow.add_node("complete", self.agent._complete_node)
        
        # Set entry point
        workflow.set_entry_point("ask_goal")
        
        # Add edges
        workflow.add_edge("ask_goal", "generate_questions")
        workflow.add_edge("generate_questions", "ask_question")
        
        # Conditional edge to continue asking questions or complete
        workflow.add_conditional_edges(
            "ask_question",
            self._should_continue_questions,
            {
                "continue": "ask_question",
                "complete": "complete",
            },
        )
        
        workflow.add_edge("complete", END)
        
        return workflow.compile()
    
    def _should_continue_questions(self, state: AgentState) -> Literal["continue", "complete"]:
        """Decide whether to ask more questions or complete."""
        current_index = state["current_question_index"]
        total_questions = len(state["questions_list"])
        
        if current_index < total_questions:
            return "continue"
        else:
            return "complete"
