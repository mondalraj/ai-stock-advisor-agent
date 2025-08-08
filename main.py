#!/usr/bin/env python3
"""
AI Stock Advisor Agent - Modular Implementation
A dynamic LangGraph-based agent that uses Gemini via LangChain for intelligent stock research.

This modular implementation separates concerns into logical components while maintaining
a single entry point for simplicity.
"""

def main():
    """Main function."""
    try:
        # Import from modular structure
        from src.core.agent import DynamicStockAgent
        from src.handlers.output_handler import OutputHandler
        from src.utils.config import Config
        
        print("🚀 Initializing Dynamic Stock Research Agent...")
        
        agent = DynamicStockAgent()
        result = agent.run()
        
        if result:
            config = Config()
            output_handler = OutputHandler(config.app_name, config.welcome_message)
            output_handler.show_final_results(result)
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Thanks for using the Dynamic Stock Agent!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
