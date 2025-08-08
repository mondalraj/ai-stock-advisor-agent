"""
AI Stock Advisor Agent - Modular Implementation
A dynamic LangGraph-based agent that uses Gemini via LangChain for intelligent stock research.
"""

__version__ = "1.0.0"
__author__ = "AI Stock Advisor Team"

from .core.agent import DynamicStockAgent
from .core.state import AgentState

__all__ = ["DynamicStockAgent", "AgentState"]
