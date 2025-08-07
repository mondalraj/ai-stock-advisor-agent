#!/usr/bin/env python3
"""
Simple LangGraph Agent - Greeting Bot
A basic LangGraph implementation that asks for a name and greets the user.
"""

from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AgentState(TypedDict):
    """State definition for the greeting agent."""
    user_input: str
    user_name: str
    greeting_complete: bool
    messages: list[str]

class GreetingAgent:
    def __init__(self):
        self.graph = self._build_graph()
    
    def _build_graph(self):
        """Build the LangGraph workflow."""
        workflow = StateGraph(AgentState)
        
        # Add nodes
        workflow.add_node("ask_name", self._ask_name_node)
        workflow.add_node("greet_user", self._greet_user_node)
        
        # Set entry point
        workflow.set_entry_point("ask_name")
        
        # Add conditional edges
        workflow.add_conditional_edges(
            "ask_name",
            self._should_greet,
            {
                "greet": "greet_user",
                "ask_again": "ask_name",
            },
        )
        
        # Add edge from greet_user to end
        workflow.add_edge("greet_user", END)
        
        return workflow.compile()
    
    def _ask_name_node(self, state: AgentState):
        """Node that asks for the user's name."""
        if not state.get("user_input"):
            # First time asking
            print("\n🤖 Hello! I'm a simple LangGraph agent.")
            user_input = input("What's your name? ").strip()
        else:
            # Asked again due to empty input
            print("\n🤖 I didn't catch that.")
            user_input = input("Could you please tell me your name? ").strip()
        
        return {
            "user_input": user_input,
            "user_name": user_input if user_input else "",
            "greeting_complete": False,
            "messages": state.get("messages", []) + [f"User input: {user_input}"]
        }
    
    def _greet_user_node(self, state: AgentState):
        """Node that greets the user."""
        name = state["user_name"]
        greeting = f"🎉 Nice to meet you, {name}! Welcome to the LangGraph demo!"
        print(f"\n🤖 {greeting}")
        
        return {
            "user_input": state["user_input"],
            "user_name": name,
            "greeting_complete": True,
            "messages": state["messages"] + [f"Agent: {greeting}"]
        }
    
    def _should_greet(self, state: AgentState) -> Literal["greet", "ask_again"]:
        """Decide whether to greet or ask for name again."""
        if state["user_name"] and state["user_name"].strip():
            return "greet"
        else:
            return "ask_again"
    
    def run(self):
        """Run the greeting agent."""
        initial_state = {
            "user_input": "",
            "user_name": "",
            "greeting_complete": False,
            "messages": []
        }
        
        print("🚀 Starting Simple LangGraph Agent...")
        print("="*40)
        
        result = self.graph.invoke(initial_state)
        
        print("\n" + "="*40)
        print("✅ Agent completed successfully!")
        print(f"👋 Final greeting: User '{result['user_name']}' has been greeted!")
        
        return result

def main():
    """Main function."""
    try:
        agent = GreetingAgent()
        agent.run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
