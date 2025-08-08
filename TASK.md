## **Personal Investment Advisor AI Agent – Intelligent Research & Analysis**

### **Main Goal**

Be your personal investment advisor for stocks and mutual funds. Answer any investment question by intelligently researching from various sources, analyzing data using LLM capabilities, and providing well-reasoned recommendations.

---

## **How the Agent Works**

1. **Start a Conversation**

   * Greets you and asks:
     * What do you want to do today? (e.g., "Find good dividend stocks")
   * Uses Gemini AI (via LangChain) to generate 3-4 tailored, clarifying questions about your goal (market, style, criteria, timeline, etc.).
   * If AI is unavailable, uses smart fallback questions.

   **Interactive Q&A**
   * Asks each question in turn, collects your answers.
   * You can type `quit`, `exit`, or `stop` at any time to end the session.

   **Summary & Next Steps**
   * Shows a summary of your goal and all answers.
   * Prepares the collected information for further analysis (e.g., stock screening, ranking, etc.).

---

2. **Intelligent Query Processing**

   * **Query Understanding**: Uses Gemini to understand your investment question/goal
   * **Research Planning**: Decides what information is needed and how to structure Perplexity queries
   * **Query Optimization**: Formulates effective search queries for Perplexity to get comprehensive data

---

3. **Research & Data Collection**

   * **Multi-Source Research**: Uses Perplexity for real-time web research, market insights, financial data, and news
   * **Comprehensive Analysis**: Perplexity provides stock prices, fundamentals, mutual fund data, market trends
   * **News & Sentiment**: Gathers recent news, analyst opinions, and market sentiment via Perplexity
   * **Self-Validation**: Checks if gathered data is sufficient and reliable

---

4. **Analysis & Reasoning Loop**

   * **Initial Analysis**: Processes collected data using LLM reasoning
   * **Self-Evaluation**: Asks itself:
     * "Is this analysis complete and helpful?"
     * "Do I need more data or different perspectives?"
     * "Are my conclusions well-supported?"
   * **Refinement Loop**: If not satisfied, refines research and re-analyzes
   * **Quality Check**: Ensures recommendations are actionable and well-reasoned

---

5. **Intelligent Response Generation**

   * **Personalized Advice**: Tailors recommendations to your specific situation
   * **Multi-Perspective Analysis**: Presents pros, cons, and risks
   * **Actionable Insights**: Provides clear next steps and decision points
   * **Source Attribution**: Shows what sources informed the analysis

---

## **LangGraph Architecture (Simple & Effective)**

**Core Nodes:**
- `conversation_node` ✅ (Already implemented)
- `research_planner_node` (Decides what to research)
- `data_collector_node` (Gathers information)
- `analyzer_node` (Processes and reasons about data)
- `validator_node` (Self-checks quality)
- `response_generator_node` (Creates final advice)

**LLM Usage:**
- **Gemini**: Query understanding, analysis, reasoning, response generation
- **Perplexity**: Real-time research, financial data collection, market insights, news analysis

**Tools:**
- Perplexity API for comprehensive research and data collection
- Data processing utilities
- Self-validation prompts

---

## **Key Capabilities**

* **Adaptive Intelligence** – Can handle any investment question, from stock picks to portfolio strategy
* **Self-Improving** – Continuously validates and refines its analysis
* **Multi-Modal Research** – Combines real-time data, historical analysis, and current market sentiment
* **Personal Context** – Remembers your preferences and tailors advice accordingly
* **Transparency** – Shows its reasoning process and sources

---

This agent is designed to be your **intelligent investment research partner** that can think, research, analyze, and provide well-reasoned advice on any investment topic.

