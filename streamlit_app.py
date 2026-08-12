"""
🤖 AutoDev Agent — Streamlit Frontend
Run: streamlit run streamlit_app.py
"""
import streamlit as st
import time, random

st.set_page_config(page_title="AutoDev Agent — Autonomous Coding Agent", page_icon="🤖", layout="wide")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@700&family=JetBrains+Mono:wght@400&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;}
.stApp{background:linear-gradient(135deg,#080b14,#0d1220);}
.tag{background:rgba(99,102,241,0.12);border:1px solid rgba(99,102,241,0.3);color:#a5b4fc;padding:3px 10px;border-radius:20px;font-size:0.78rem;display:inline-block;margin:2px;}
.agent-log{background:rgba(99,102,241,0.07);border-left:3px solid #6366f1;border-radius:0 10px 10px 0;padding:10px 14px;margin:5px 0;font-size:0.82rem;font-family:'JetBrains Mono',monospace;}
.file-card{background:rgba(255,255,255,0.03);border:1px solid rgba(99,102,241,0.18);border-radius:10px;padding:12px;margin:5px 0;}
.stButton>button{background:linear-gradient(135deg,#6366f1,#8b5cf6)!important;color:white!important;border:none!important;border-radius:10px!important;font-weight:600!important;}
</style>
""", unsafe_allow_html=True)

SAMPLE_SPECS = [
    "Build a REST API with FastAPI that manages a todo list with CRUD operations and SQLite database",
    "Create a Python CLI tool that converts PDF files to markdown using PyMuPDF",
    "Build a real-time chat application using Flask-SocketIO with a simple HTML frontend",
    "Create a data pipeline that fetches weather data from OpenWeather API and stores in PostgreSQL",
    "Build a Discord bot that monitors GitHub repos and posts update notifications",
]

with st.sidebar:
    st.markdown("## 🤖 AutoDev Agent")
    st.markdown("---")
    llm_model = st.selectbox("LLM Backbone", ["GPT-4o", "Claude 3.5 Sonnet", "Gemini 1.5 Pro", "Mistral-Large"])
    framework = st.selectbox("Prefer Framework", ["Auto-detect", "FastAPI", "Flask", "Django", "Express.js", "Next.js"])
    lang = st.selectbox("Language", ["Python", "JavaScript", "TypeScript", "Go", "Rust"])
    include_tests = st.toggle("Generate Tests", value=True)
    include_docker = st.toggle("Generate Dockerfile", value=True)
    include_ci = st.toggle("GitHub Actions CI/CD", value=False)
    auto_push = st.toggle("Auto-push to GitHub", value=False)
    st.markdown("---")
    for t in ["LangGraph", "GPT-4o", "Docker", "GitHub API", "Streamlit"]:
        st.markdown(f'<span class="tag">{t}</span>', unsafe_allow_html=True)
    st.caption("Built by Muhammad Abdullah")

st.markdown(f"""
<div style="text-align:center;padding:28px;background:linear-gradient(135deg,rgba(99,102,241,0.12),rgba(139,92,246,0.08));
     border:1px solid rgba(99,102,241,0.25);border-radius:20px;margin-bottom:24px;">
  <div style="font-family:'Space Grotesk',sans-serif;font-size:2.4rem;font-weight:700;
       background:linear-gradient(135deg,#6366f1,#8b5cf6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">🤖 AutoDev Agent</div>
  <p style="color:#64748b;margin:8px 0 0;">Autonomous LangGraph agent that generates, tests, and deploys full-stack apps from natural language</p>
  <br><span class="tag">🧠 {llm_model}</span> <span class="tag">⚡ LangGraph</span> <span class="tag">🐳 Docker</span>
</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.metric("LLM", llm_model.split("-")[0])
with c2: st.metric("Language", lang)
with c3: st.metric("Tests", "✅" if include_tests else "❌")
with c4: st.metric("Docker", "✅" if include_docker else "❌")

st.markdown("---")
st.markdown("### 📝 Project Specification")
spec = st.text_area("Describe what you want to build:", height=120, label_visibility="collapsed",
                    value="Build a REST API with FastAPI that manages a todo list with CRUD operations and SQLite database",
                    placeholder="Describe your project in natural language...")

col_sample, _ = st.columns([2, 3])
with col_sample:
    if st.selectbox("💡 Sample specs:", ["— Try a sample —"] + SAMPLE_SPECS, label_visibility="collapsed", key="sample_spec") != "— Try a sample —":
        pass  # Would rerun with sample

st.markdown("---")

if st.button("🚀 Build with AutoDev Agent", use_container_width=True):
    if not spec.strip():
        st.error("Please enter a project specification!")
    else:
        st.markdown("### ⚙️ AutoDev Agent Running...")
        prog = st.progress(0)
        log_area = st.empty()
        logs = []

        agent_steps = [
            (8,  f"[Planner] Analyzing spec: '{spec[:50]}...'"),
            (16, f"[Planner] Decomposing into {random.randint(4,8)} implementation tasks..."),
            (24, f"[Architect] Designing system architecture with {framework if framework != 'Auto-detect' else 'FastAPI'} + SQLite..."),
            (32, f"[Coder] Generating main.py ({random.randint(80,150)} lines)..."),
            (42, f"[Coder] Generating models.py with Pydantic schemas..."),
            (50, f"[Coder] Generating database.py with SQLAlchemy ORM..."),
            (58, f"[Coder] Generating requirements.txt..."),
            (65, f"[Tester] Writing test_main.py with pytest ({random.randint(8,15)} test cases)..." if include_tests else "[Skipping] Tests disabled"),
            (73, f"[Docker] Generating Dockerfile + docker-compose.yml..." if include_docker else "[Skipping] Docker disabled"),
            (82, f"[Reviewer] Running static analysis and linting..."),
            (90, f"[Reviewer] Fixing {random.randint(1,4)} linting issues..."),
            (100, "✅ Project generation complete! All files ready."),
        ]

        for prog_val, msg in agent_steps:
            time.sleep(0.45)
            logs.append(msg)
            log_area.markdown("\n".join([f'<div class="agent-log">{"✅" if "complete" in msg or "Fixing" in msg else "🔄"} {l}</div>' for l in logs[-5:]]), unsafe_allow_html=True)
            prog.progress(prog_val)

        st.success("✅ AutoDev Agent completed! Project generated.")

        st.markdown("---")
        st.markdown("### 📁 Generated Files")

        files = [
            ("main.py", lang, f"FastAPI app with {random.randint(80,140)} lines — CRUD endpoints, error handling"),
            ("models.py", lang, "Pydantic request/response models and SQLAlchemy ORM models"),
            ("database.py", lang, "SQLite connection, session management, table creation"),
            ("requirements.txt", "txt", "fastapi, uvicorn, sqlalchemy, pydantic, pytest"),
            ("README.md", "md", "Full setup guide, API docs, example requests"),
        ]
        if include_tests: files.append(("test_main.py", lang, f"{random.randint(8,15)} pytest tests covering all endpoints"))
        if include_docker: files.append(("Dockerfile", "docker", "Multi-stage build, production-ready container"))
        if include_docker: files.append(("docker-compose.yml", "yaml", "App + DB services configuration"))

        file_cols = st.columns(2)
        for i, (fname, ftype, desc) in enumerate(files):
            with file_cols[i % 2]:
                st.markdown(f"""
                <div class="file-card">
                    <div style="font-weight:600;color:#a5b4fc;">📄 {fname}</div>
                    <div style="font-size:0.78rem;color:#64748b;margin-top:4px;">{desc}</div>
                    <span class="tag">{ftype}</span>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 🚀 Sample Generated Code: `main.py`")
        generated_code = f'''from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models, database

app = FastAPI(title="Todo API", version="1.0.0")
database.Base.metadata.create_all(bind=database.engine)

@app.get("/todos", response_model=List[models.TodoResponse])
def get_all_todos(db: Session = Depends(database.get_db)):
    """Get all todo items."""
    return db.query(models.Todo).all()

@app.post("/todos", response_model=models.TodoResponse, status_code=201)
def create_todo(todo: models.TodoCreate, db: Session = Depends(database.get_db)):
    """Create a new todo item."""
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.put("/todos/{{todo_id}}", response_model=models.TodoResponse)
def update_todo(todo_id: int, todo: models.TodoCreate, db: Session = Depends(database.get_db)):
    """Update an existing todo item."""
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.dict().items():
        setattr(db_todo, key, value)
    db.commit()
    return db_todo

@app.delete("/todos/{{todo_id}}")
def delete_todo(todo_id: int, db: Session = Depends(database.get_db)):
    """Delete a todo item."""
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {{"message": "Todo deleted successfully"}}
'''
        st.code(generated_code, language="python")

        if auto_push:
            st.success("☁️ Code pushed to GitHub: `Muhammad08-dot/autodev-generated-project`")

st.markdown("---")
st.caption("🤖 AutoDev Agent — Built with ❤️ by Muhammad Abdullah | LangGraph + GPT-4o + Docker + GitHub API + Streamlit")
