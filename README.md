<div align="center">
  <h1>🤖 AutoDev Agent</h1>
  <p><strong>An autonomous AI software engineer that writes, tests, and deploys full-stack applications.</strong></p>
</div>

## 🚀 Overview
AutoDev Agent is a state-of-the-art autonomous coding assistant powered by LangGraph. Give it a natural language prompt (e.g., "Build a fastAPI todo app with SQLite") and it will orchestrate Planner, Architect, Coder, and Reviewer agents to generate a complete, working codebase.

## ✨ Features
- **Multi-Agent Architecture:** Specialized nodes for planning, coding, reviewing, and Dockerizing.
- **Full-Stack Generation:** Capable of scaffolding React, FastAPI, Node.js, and Python CLI tools.
- **Automated Testing & CI:** Generates Pytest/Jest suites and GitHub Actions workflows alongside application code.
- **Interactive UI:** A sleek Streamlit dashboard that visualizes the agent's thought process and outputs the generated files.

## 🛠️ Tech Stack
- **Agent Framework:** [LangGraph](https://python.langchain.com/v0.1/docs/langgraph/)
- **LLM Backbone:** GPT-4o / Claude 3.5 Sonnet
- **Containerization:** Docker integration
- **Frontend UI:** [Streamlit](https://streamlit.io/)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhammad08-dot/autodev-agent.git
   cd autodev-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install langgraph langchain openai streamlit docker
   ```

3. **Configure Environment:**
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

4. **Run the application:**
   ```bash
   streamlit run streamlit_app.py
   ```

## 📄 License
This project is licensed under the MIT License.
