# Simple LangGraph Agent - Greeting Bot

A basic LangGraph implementation that demonstrates a simple workflow: asking for a user's name and providing a personalized greeting.

## Project Structure

```
ai-stock-advisor-agent/
├── main.py           # Complete LangGraph agent in one file
├── requirements.txt  # Dependencies (langgraph and python-dotenv)
├── .env             # Environment file (no API keys needed)
├── .gitignore       # Git ignore file
└── README.md        # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup and Installation

### 1. Clone or navigate to the project directory
```bash
cd ai-stock-advisor-agent
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the Agent

### Start the greeting agent
```bash
python main.py
```

## What the Agent Does

1. **Starts** - Displays a welcome message
2. **Asks for your name** - Prompts you to enter your name
3. **Validates input** - If you don't enter a name, it asks again
4. **Greets you** - Provides a personalized greeting
5. **Completes** - Shows a success message

## Example Interaction

```
🚀 Starting Simple LangGraph Agent...
========================================

🤖 Hello! I'm a simple LangGraph agent.
What's your name? John

🤖 🎉 Nice to meet you, John! Welcome to the LangGraph demo!

========================================
✅ Agent completed successfully!
👋 Final greeting: User 'John' has been greeted!
```

## Features

- ✅ Single file implementation
- ✅ No API keys required
- ✅ Proper LangGraph state management
- ✅ Conditional workflow logic
- ✅ Input validation
- ✅ Clean error handling

## Deactivating the Virtual Environment

When you're done, you can deactivate the virtual environment:
```bash
deactivate
```

## Troubleshooting

### Python not found
Make sure Python 3.8+ is installed:
```bash
python3 --version
```

### Dependencies not installing
Make sure you're in the virtual environment:
```bash
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

### Permission errors
On macOS/Linux, you might need to make the file executable:
```bash
chmod +x main.py
```

## Next Steps

This is a basic LangGraph implementation. You can extend it by:
- Adding more nodes and complex workflows
- Integrating with LLMs (OpenAI, Anthropic, etc.)
- Adding memory and conversation history
- Creating more sophisticated state management
- Adding tool integrations
