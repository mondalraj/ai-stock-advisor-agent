"""
Utility functions and decorators for the AI Stock Advisor Agent.
"""

import time
import json
import functools
from typing import Any, Dict, List

def timing_decorator(func):
    """Decorator to measure function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"⏱️ {func.__name__} completed in {elapsed_time:.2f}s")
        return result
    return wrapper

def clean_json_response(response_text: str) -> str:
    """Clean and extract JSON from AI response text."""
    response_text = response_text.strip()
    
    # Handle markdown code blocks
    if "```json" in response_text:
        json_start = response_text.find("```json") + 7
        json_end = response_text.find("```", json_start)
        json_text = response_text[json_start:json_end].strip()
    # Handle plain JSON arrays
    elif "[" in response_text and "]" in response_text:
        json_start = response_text.find("[")
        json_end = response_text.rfind("]") + 1
        json_text = response_text[json_start:json_end]
    else:
        json_text = response_text
    
    return json_text

def validate_question_structure(questions: List[Dict[str, Any]]) -> bool:
    """Validate that questions have the required structure."""
    if not isinstance(questions, list) or len(questions) == 0:
        return False
    
    required_fields = ['id', 'question', 'purpose']
    for question in questions:
        if not all(field in question for field in required_fields):
            return False
    
    return True

def format_conversation_summary(goal: str, answers: Dict[str, str], 
                               questions: List[Dict[str, str]]) -> str:
    """Format a conversation summary for display."""
    summary = f"🎯 Goal: {goal}\n\n"
    summary += "📋 Information Collected:\n"
    summary += "-" * 40 + "\n"
    
    for i, question in enumerate(questions):
        answer = answers.get(question["id"], "No answer")
        summary += f"{i+1}. {question['question']}\n"
        summary += f"   💭 {answer}\n\n"
    
    return summary
