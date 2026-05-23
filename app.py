import streamlit as st
import os
import glob

# --- MULTI-PAGE LAYOUT INITIALIZATION ---
st.set_page_config(
    page_title="Databricks MLOps Enterprise Academy",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DIRECTORY SANITY ASSURANCE ---
MODULES_DIR = os.path.join("content", "modules")
QUIZZES_DIR = os.path.join("content", "quizzes")

os.makedirs(MODULES_DIR, exist_ok=True)
os.makedirs(QUIZZES_DIR, exist_ok=True)

# --- FILE DISCOVERY & PARSING ENGINES ---
def discover_modules():
    """Scans the directory structure to organically build the course roadmap."""
    search_path = os.path.join(MODULES_DIR, "*.md")
    files = glob.glob(search_path)
    modules = {}
    
    for filepath in sorted(files):
        filename = os.path.basename(filepath)
        # Extract prefix index (e.g. '01') and create a clean display name
        prefix = filename.split("_")[0]
        display_name = filename.replace(".md", "").replace("_", " ")
        
        modules[display_name] = {
            "prefix": prefix,
            "md_path": filepath,
            "quiz_path": os.path.join(QUIZZES_DIR, f"{prefix}_quiz.md")
        }
    return modules

def load_markdown(filepath):
    """Safely extracts markdown text documentation strings."""
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return "⚠️ Concept documentation file asset missing from repository space."

def parse_module_quiz(filepath):
    """Processes pipeline delimited structures into production interactive quiz dictionaries."""
    quiz_questions = []
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() and "|" in line:
                    parts = [p.strip() for p in line.split("|")]
                    if len(parts) >= 5:
                        quiz_questions.append({
                            "question": parts[0],
                            "options": [parts[1], parts[2], parts[3]],
                            "correct": parts[4]
                        })
    return quiz_questions

# --- APP SYSTEM STATE TRACKER ---
discovered_coursework = discover_modules()

if 'active_track' not in st.session_state and discovered_coursework:
    st.session_state.active_track = list(discovered_coursework.keys())[0]
if 'chat_records' not in st.session_state:
    st.session_state.chat_records = {}
if 'quiz_submission_states' not in st.session_state:
    st.session_state.quiz_submission_states = {}

# Handle fallback if repository folders are empty
if not discovered_coursework:
    st.title("🛡️ Databricks MLOps Enterprise Academy")
    st.warning("No curriculum modules discovered. Please populate your `content/modules/` and `content/quizzes/` directories on GitHub.")
    st.stop()

# Ensure active history track key exists
if st.session_state.active_track not in st.session_state.chat_records:
    st.session_state.chat_records[st.session_state.active_track] = []

# --- HAMBURGER SLIDEOUT NAVIGATION SIDEBAR ---
with st.sidebar:
    st.title("🛡️ MLOps Workspace")
    st.caption("Course Playlist Index Engine")
    st.write("---")
    
    st.subheader("📋 Lecture Syllabus")
    
    # Render native selections
    selected_selection = st.radio(
        "Navigate Syllabus Node:",
        options=list(discovered_coursework.keys()),
        index=list(discovered_coursework.keys()).index(st.session_state.active_track)
    )
    
    # State mutation handler
    if selected_selection != st.session_state.active_track:
        st.session_state.active_track = selected_selection
        st.rerun()

    st.write("---")
    st.caption("🔒 Dynamic Mode: Content layers parsed on-demand from independent folder assets.")

# --- MAIN ENGINE CANVAS CONTAINER WORKSPACE ---
active_node = discovered_coursework[st.session_state.active_track]

st.title("🎯 Enterprise Training Canvas")
st.markdown(f"Syllabus Topic Area: **{st.session_state.active_track}**")
st.write("---")

# Setup layout tabs
tab_concepts, tab_chat, tab_quiz = st.tabs([
    "📖 Core Concepts", 
    "💬 Ask Questions", 
    "🧠 Quiz Me"
])

# --- TAB 1: CORE CONCEPTS GENERATOR ---
with tab_concepts:
    markdown_body = load_markdown(active_node["md_path"])
    st.markdown(markdown_body)

# --- TAB 2: CONVERSATIONAL TUTOR ENGINE ---
with tab_chat:
    st.subheader("💬 Conceptual Dialogue Engine")
    st.caption("Ask questions or request clarifications in plain English regarding this chapter.")
    
    # Load history file metrics specifically bound to this module context
    track_history = st.session_state.chat_records[st.session_state.active_track]
    
    for message in track_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            
    with st.form(key="chat_entry_form", clear_on_submit=True):
        input_text = st.text_input("Ask a question in plain English:", placeholder="e.g., Explain the business importance of this mechanism...")
        if st.form_submit_button("Submit Question") and input_text.strip():
            track_history.append({"role": "user", "content": input_text})
            
            # Context-aware simulated assistant logic
            simulated_response = f"Analyzing your inquiry regarding **{st.session_state.active_track}**: Conceptually, this phase removes complexity and human error. It creates an isolated, automated safety layer so your system runs without manual friction."
            
            track_history.append({"role": "assistant", "content": simulated_response})
            st.rerun()

# --- TAB 3: QUIZ SUITE ENGINE (SEGREGATED BY MODULE) ---
with tab_quiz:
    st.subheader(f"🧠 Section Assessment: Chapter {active_node['prefix']}")
    module_quizzes = parse_module_quiz(active_node["quiz_path"])
    
    if not module_quizzes:
        st.info("No localized quiz question files have been uploaded yet for this chapter node. Create a matching quiz file to activate this canvas panel.")
    else:
        user_responses = {}
        # Scrape and render only questions belonging to this file asset
        with st.form(key=f"quiz_form_{active_node['prefix']}"):
            for idx, q_data in enumerate(module_quizzes):
                st.markdown(f"**Question {idx+1}:** {q_data['question']}")
                user_responses[idx] = st.radio(
                    "Select choice:", 
                    options=q_data['options'], 
                    key=f"quiz_item_{active_node['prefix']}_{idx}", 
                    label_visibility="collapsed"
                )
                st.write("")
                
            if st.form_submit_button("Grade Assessment Block"):
                total_correct = sum(1 for idx, q_data in enumerate(module_quizzes) if user_responses[idx] == q_data['correct'])
                st.session_state.quiz_submission_states[st.session_state.active_track] = f"{total_correct} / {len(module_quizzes)}"
                
        # Display localized, targeted grading metric panels
        if st.session_state.active_track in st.session_state.quiz_submission_states:
            calculated_score = st.session_state.quiz_submission_states[st.session_state.active_track]
            st.write("---")
            st.metric("Section Score Result", calculated_score)
            
            raw_correct = int(calculated_score.split(" / ")[0])
            if raw_correct == len(module_quizzes):
                st.success("Perfect result! You've completely mastered the nuances of this course lecture material.")
            else:
                st.warning("Some answers were incorrect. Review the 'Core Concepts' tab documentation to brush up on this lecture section.")
