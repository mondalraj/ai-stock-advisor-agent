## **Stock Research & Screener AI Agent – Functional Blueprint (Self-Thinking + Feedback Loop)**

### **Main Goal**

Find fundamentally strong stocks, detect price drops, assess valuation, and make intelligent, self-driven decisions — while asking you for input when needed.

---

## **How the Agent Works**

1. **Start a Conversation**

   * Greets you and gathers:

     * Target market or exchange.
     * Types of companies (size, sector, etc.).
     * Risk appetite (low / medium / high).
     * Price drop alert threshold.
   * Confirms your preferences before starting.

---

2. **Self-Planning Step (Thinking Phase)**

   * Reviews your inputs and decides:

     * What data sources to check first.
     * Whether to do a quick scan or a deep dive.
     * In what order to run checks.
   * Displays its **thinking plan** before executing.

---

3. **Data Collection**

   * Pulls latest prices, recent movements, and basic company info.
   * If data is incomplete or outdated →
     **Agent Decision:** try another source automatically OR ask you whether to wait for fresher data.

---

4. **Fundamentals Check**

   * Filters based on revenue, profits, debt, return on equity, etc.
   * If too few companies pass →
     **Agent Decision:** relax filters slightly OR ask you if you want to adjust criteria.

---

5. **Valuation Check**

   * Compares market price to intrinsic value.
   * Labels each stock:

     * **Undervalued** → possible opportunity.
     * **Fairly Valued** → watchlist candidate.
     * **Overvalued** → caution.
   * If valuations don’t make sense due to unusual data →
     **Agent Decision:** double-check using a different valuation method.

---

6. **Price Movement Check**

   * Finds stocks with your target % drop.
   * Cross-references with valuation:

     * Undervalued + drop → highlight.
     * Overvalued + drop → caution.
   * If no stocks match →
     **Agent Decision:** adjust drop % or timeframe automatically, or ask you.

---

7. **Self-Evaluation Loop**

   * After first run, the agent asks itself:

     * “Do I have enough high-quality candidates?”
     * “Do my conclusions feel reliable based on the data quality?”
   * If **No** →

     * Modify filters, expand the search scope, or try alternative calculations.
     * Run through data collection, fundamentals, valuation, and price checks again.
     * Repeat until results meet quality standards or a max loop limit is reached.
   * At each loop, it tells you what changed and why.

---

8. **Explain Thinking at Every Step**

   * Shows:

     * What it looked at.
     * Why it kept or rejected a stock.
     * Any assumptions it made.
     * Why it changed filters in a loop.

---

9. **User Feedback Checkpoints**

   * Pauses and asks when:

     * No results meet criteria.
     * Data conflicts arise.
     * The agent is unsure whether to relax or tighten filters.
   * Your choice can:

     * Guide the next loop.
     * Approve the current shortlist.

---

10. **Final Suggestions**

    * Gives a concise, ranked list with:

      * Company name & sector.
      * Fundamentals summary.
      * Valuation status.
      * Price movement notes.
      * Why it’s worth attention.
      * Risks to consider.
    * Offers to save or export the results.

---

## **Extra Capabilities**

* **Autonomous Decision-Making** – Can run multiple internal loops without waiting for user input if confident in next steps.
* **Interactive Mode** – Can stop and ask questions when choices involve personal risk preferences.
* **Adaptive Scope** – Can expand beyond initial market or sector if too few matches are found.

---

With this, your agent is basically **self-thinking, self-checking, and self-correcting**, while still keeping you in the loop when human judgment matters.