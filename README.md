# AI Stock Advisor Agent

A dynamic LangGraph-based agent that uses Google's Gemini AI via LangChain to generate intelligent, contextual questions for stock research. The agent adapts its questioning strategy based on your specific goals and provides smart fallbacks when AI is unavailable.

## 🎯 Features

- **Dynamic Question Generation**: AI-powered questions tailored to your specific investment goals
- **Smart Fallbacks**: Context-aware backup questions when AI is unavailable
- **Modular Architecture**: Clean, maintainable code structure with separated concerns
- **LangChain Integration**: Optimized Gemini AI client with performance monitoring
- **Interactive Workflow**: Natural conversation flow using LangGraph
- **Performance Optimized**: Fast response times with configurable AI parameters

## 🏗️ Project Structure

```
ai-stock-advisor-agent/
├── main.py                    # Main entry point
├── requirements.txt           # Python dependencies
├── .env                      # Environment variables (create from .env.example)
├── README.md                 # This file
└── src/                      # Modular source code
    ├── __init__.py
    ├── core/                 # 🧠 Core agent logic
    │   ├── __init__.py
    │   ├── agent.py          # Main agent orchestration
    │   ├── state.py          # LangGraph state definitions
    │   └── workflow.py       # LangGraph workflow builder
    ├── ai/                   # 🤖 AI integration
    │   ├── __init__.py
    │   ├── gemini_client.py  # LangChain Gemini client
    │   └── question_generator.py # Unified question generation
    ├── handlers/             # 🎯 Input/output management
    │   ├── __init__.py
    │   ├── input_handler.py  # User input processing
    │   └── output_handler.py # Display formatting
    ├── utils/                # 🔧 Utilities
    │   ├── __init__.py
    │   ├── config.py         # Configuration management
    │   └── helpers.py        # Utility functions
    └── fallback/             # 🛡️ Fallback systems
        ├── __init__.py
        └── questions.py      # Smart fallback questions
```

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd ai-stock-advisor-agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Create a `.env` file in the project root:

```bash
# Copy example environment file
cp .env.example .env

# Edit .env and add your Gemini API key
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
```

**Get your Gemini API key:**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy it to your `.env` file

### 3. Run the Application

```bash
python main.py
```

## 📋 Requirements

Create a `requirements.txt` file with these dependencies:

```
langgraph>=0.2.0
langchain-google-genai>=2.0.0
python-dotenv>=1.0.0
```

## 🎮 Usage Examples

### Basic Usage
```bash
python main.py
```

The agent will:
1. Ask what you want to accomplish
2. Generate relevant questions using AI or fallbacks
3. Collect your answers interactively
4. Provide a summary of gathered information

### Example Interaction
```
🤖 INTELLIGENT STOCK RESEARCH AGENT
What would you like to do today? Find good dividend stocks

🧠 Consulting Gemini AI for optimal questions...
✅ Generated 4 AI-powered questions (1.2s)!

📝 Question 1 of 4
🎯 Which markets interest you most for dividend investing?
💬 Your answer: US and European markets

📝 Question 2 of 4  
🎯 What minimum dividend yield are you targeting?
💬 Your answer: At least 4%

[... continues with remaining questions ...]
```

### Exit Commands
Type any of these to exit: `quit`, `exit`, `stop`, `bye`

## 🔧 Configuration

### Environment Variables (`.env`)
```bash
# Required: Your Gemini API key
GEMINI_API_KEY=your_actual_api_key_here
```

### AI Model Configuration
Edit `src/utils/config.py` to modify:
- **Model**: `gemini-1.5-flash` (fastest)
- **Temperature**: `0.1` (focused responses)
- **Max Tokens**: `500` (speed optimization)
- **Top P**: `0.8` (reduced randomness)

## 🧪 Development & Testing

### Test Individual Components
```python
# Test configuration
python -c "from src.utils.config import Config; print('Config OK')"

# Test AI question generation
python -c "
from src.ai.question_generator import QuestionGenerator
from src.utils.config import Config
config = Config()
generator = QuestionGenerator(config)
questions = generator.generate_questions('Find growth stocks')
print(f'Generated {len(questions)} questions')
"

# Test fallback questions
python -c "
from src.fallback.questions import FallbackQuestionGenerator
questions = FallbackQuestionGenerator.generate_questions('Find dividend stocks')
print(questions)
"
```

### Code Structure Benefits

- **Maintainable**: Each module has a single responsibility
- **Testable**: Components can be tested in isolation
- **Extensible**: Easy to add features without modifying existing code
- **Reusable**: Modules can be used in other projects

## 📈 Performance Optimizations

The application includes several performance optimizations:

1. **Optimized AI Parameters**: Fast model with reduced tokens
2. **Response Time Monitoring**: Track AI performance 
3. **Smart Fallbacks**: Instant local question generation
4. **Efficient JSON Parsing**: Robust response processing
5. **Lazy Loading**: Modules loaded only when needed

## 🐛 Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

**2. API Key Issues**
```bash
# Check if .env file exists and has correct key
cat .env

# Verify key format (should start with 'AI...')
echo $GEMINI_API_KEY
```

**3. Slow AI Responses**
- Free tier has rate limits
- Check internet connection
- AI will fallback to local questions automatically

**4. Module Not Found**
```bash
# Make sure you're in the correct directory
pwd
# Should show: /path/to/ai-stock-advisor-agent

# Check if src/ directory exists
ls -la src/
```

### Debug Mode

Add debugging to `main.py`:
```python
import traceback

# In the except block:
except Exception as e:
    print(f"❌ Error: {e}")
    traceback.print_exc()  # Shows full error trace
```

## 🚀 Extending the Agent

### Add New AI Provider
1. Create `src/ai/openai_client.py`
2. Update `src/ai/question_generator.py`
3. Add configuration to `src/utils/config.py`

### Add New Question Types
1. Modify `src/fallback/questions.py`
2. Add new contextual logic
3. Update system prompts in `src/ai/gemini_client.py`

### Add Web Interface
1. Create `src/web/` directory
2. Add Flask/FastAPI handlers
3. Extend `src/handlers/` for web responses

### Add Database Storage
1. Create `src/storage/` directory
2. Add database models and connections
3. Update agent to save conversation history

## 📚 API Reference

### Core Classes

**`DynamicStockAgent`** - Main orchestration class
- `run()` - Execute the full conversation workflow
- Returns conversation results for further processing

**`QuestionGenerator`** - AI and fallback question generation
- `generate_questions(user_goal)` - Get questions for a goal
- `is_ai_enabled` - Check if AI is available

**`Config`** - Configuration management
- `has_valid_api_key` - Validate API key
- `get_gemini_config()` - Get AI model settings

### Workflow Nodes

1. **ask_goal** - Collect user's investment goal
2. **generate_questions** - Create relevant questions  
3. **ask_question** - Interactive Q&A loop
4. **complete** - Summarize and finish

## 📄 License

This project is open source. Feel free to modify and extend it for your needs.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes in the modular structure
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues and questions:
1. Check the troubleshooting section above
2. Review the modular code structure in `src/`
3. Test individual components
4. Create an issue with full error details

---

**Happy Investing! 📈** The AI Stock Advisor Agent helps you ask the right questions to make informed investment decisions.
