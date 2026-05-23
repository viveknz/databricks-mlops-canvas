import streamlit as str
import random

# --- CONFIGURATION & STYLING ---
str.set_page_config(layout="wide", page_title="Databricks MLOps Academy")

# Custom CSS to mimic a clean, scannable Canvas environment
str.markdown("""
<style>
    .reportview-container { background: #f5f7f8; }
    .stDeployButton { display:none; }
    footer { visibility: hidden; }
    .main-header { font-size: 32px; font-weight: 700; color: #1b2a47; margin-bottom: 20px; }
    .section-box { padding: 20px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px; }
    .chat-bubble-user { background-color: #e2f0fd; padding: 12px; border-radius: 10px; margin: 5px 0; text-align: right; }
    .chat-bubble-bot { background-color: #f1f3f4; padding: 12px; border-radius: 10px; margin: 5px 0; text-align: left; }
</style>
""", unsafe_allowed_html=True)

# --- APPLICATION STATE INITIALIZATION ---
if 'current_module' not in str.session_state:
    str.session_state.current_module = "1. Introduction to MLOps"
if 'chat_history' not in str.session_state:
    str.session_state.chat_history = []
if 'quiz_score' not in str.session_state:
    str.session_state.quiz_score = None
if 'user_answers' not in str.session_state:
    str.session_state.user_answers = {}

# --- SYLLABUS DATA (Plain English Content) ---
COURSE_MODULES = {
    "1. Introduction to MLOps": {
        "summary": "MLOps is simply 'DevOps for Machine Learning'. While data science focuses on building a model, MLOps provides the safety nets, automation, and structure to ensure that the model actually runs reliably in production without breaking.",
        "analogy": "Think of it like running a restaurant. A data scientist is the chef who invents a brilliant new recipe (the model). MLOps is the supply chain, the kitchen workflow, and the health inspector making sure that recipe can be cooked perfectly 1,000 times a day safely.",
        "keywords": ["Lifecycle", "Production", "Automation", "Reliability"]
    },
    "2. Developing on Databricks": {
        "summary": "Databricks acts as a massive cloud-based playground. It gives teams a single collaborative canvas where you can write code, view data, and spin up powerful computer servers instantly without needing to configure anything locally.",
        "analogy": "Imagine a gigantic, digital whiteboard that has infinite processing power attached to it. You and your team can code together live, and the server infrastructure scales up or down automatically behind the scenes.",
        "keywords": ["Notebooks", "Compute Clusters", "Workspace", "Delta Lake"]
    },
    "3. Getting Started with MLflow": {
        "summary": "MLflow is an open-source tool built to track everything you do when building a model. It records your code versions, configuration settings, and experimental results so you never lose a successful build.",
        "analogy": "Think of MLflow as a digital laboratory notebook. Every time you run an experiment with a different set of ingredients, MLflow automatically writes down the exact measurements and how well the experiment succeeded.",
        "keywords": ["Experiments", "Tracking URI", "Parameters", "Metrics"]
    },
    "4. Logging & Registering Models": {
        "summary": "Logging means saving your trained model files into storage. Registering takes it a step further: it places the model into an organized library where it gets assigned official version numbers and operational states.",
        "analogy": "Logging is like putting your finished painting into a storage closet. Registering is like putting it on display in a museum with a clear tag that reads 'Masterpiece Version 2, currently on display in the Main Hall (Production)'.",
        "keywords": ["Model Registry", "Artifacts", "Versions", "Transitions"]
    },
    "5. Model Serving Architectures": {
        "summary": "Model serving means hosting your registered model so other applications can talk to it over the web. The system needs an architecture that can handle requests instantly (real-time) or process huge piles of data all at once (batch).",
        "analogy": "Real-time serving is like an automated drive-thru window: an application drops off data, and the model instantly hands back a prediction. Batch serving is like mail delivery: you pile up a thousand letters, and process them all in one big trip once a day.",
        "keywords": ["Real-time", "Batch Processing", "API", "Latency"]
    },
    "6. Deploying serving endpoints": {
        "summary": "An endpoint is the physical web address where your serving architecture lives. Deploying it means making that address active so apps can securely send data and receive predictions over HTTPS.",
        "analogy": "It's like turning on a store's telephone hotline. Once deployed, anyone with the correct phone number (the endpoint URL) and permission can call up and ask the model questions.",
        "keywords": ["Endpoint URL", "Payload", "JSON response", "Scaling"]
    },
    "7. Databricks Asset Bundles (DABs)": {
        "summary": "Databricks Asset Bundles allow you to bundle all your code, notebooks, test settings, and infrastructure configs into a single, structured project package. This makes moving code across different spaces predictable.",
        "analogy": "Imagine you are moving houses. Instead of carrying individual clothes, books, and plates loosely in your arms, you pack them cleanly into a standard moving crate. DABs are that moving crate for your machine learning project.",
        "keywords": ["Infrastructure as Code", "Project Structure", "Configuration", "DABs"]
    },
    "8. CI/CD & Deployment Strategies": {
        "summary": "CI/CD (Continuous Integration & Continuous Deployment) means using automated rules to test and ship code. Instead of manually clicking deploy, a robot automatically checks your work for errors every time you update it.",
        "analogy": "It's like an automated factory assembly line. Before a car leaves the factory, automated arms shake the doors and test the brakes. If anything fails, the line stops automatically before the broken car can reach a customer.",
        "keywords": ["GitHub Actions", "Automation", "Unit Testing", "Rollback"]
    },
    "9. Intro to Monitoring": {
        "summary": "Once a model goes live, it encounters real-world data, which constantly changes. Monitoring means tracking the incoming data and the model’s answers to ensure the model isn't slowly losing its accuracy.",
        "analogy": "Imagine you train a weather bot in winter, and suddenly summer arrives. The data looks completely different. Monitoring is the alarm system that rings when your bot starts making weird summer predictions based on winter logic.",
        "keywords": ["Data Drift", "Model Decay", "Alerts", "Performance"]
    },
    "10. Lakehouse Monitoring": {
        "summary": "Lakehouse Monitoring is Databricks' built-in tool that automatically hooks into your data tables. It looks at your training data and compares it directly with real-time production tables to spot shifts without you writing complex tracking code.",
        "analogy": "It is like having a dedicated auditor standing right next to your data pipeline 24/7, continuously running math equations to verify that today's data looks just as healthy as yesterday's data.",
        "keywords": ["Dashboard", "Baseline Table", "Drift Metrics", "Inference Tables"]
    }
}

# --- QUIZ DATA ---
QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "What is the primary role of an 'MLflow Model Registry'?",
        "options": ["To visually clean dirty data tables", "To act as an organized, version-controlled library for your models", "To run automated code style tests"],
        "correct": "To act as an organized, version-controlled library for your models"
    },
    {
        "id": 2,
        "question": "If an application needs an immediate prediction the millisecond a user clicks a button, which architecture should you use?",
        "options": ["A nightly Batch Processing job", "A Databricks Asset Bundle", "A Real-time Serving Endpoint"],
        "correct": "A Real-time Serving Endpoint"
    },
    {
        "id": 3,
        "question": "What does 'Data Drift' mean in the context of Model Monitoring?",
        "options": ["The server hardware is physically overheating", "Real-world data has changed compared to what the model was originally trained on", "The model's code was accidentally deleted by an engineer"],
        "correct": "Real-world data has changed compared to what the model was originally trained on"
    }
]

# --- RESPONSIVE AI CHAT SIMULATOR (Plain English Logic) ---
def get_ai_response(user_text, active_module):
    text_lower = user_text.lower()
    module_data = COURSE_MODULES[active_module]
    
    if "why" in text_lower or "purpose" in text_lower:
        return f"The main purpose of **{active_module}** is to solve a specific friction point: it keeps your work stable and predictable. Without it, you run into environments where code works on one person's machine but breaks instantly when launched live."
    elif "example" in text_lower or "analogy" in text_lower:
        return f"Here is another way to picture it: {module_data['analogy']}"
    elif "code" in text_lower or "syntax" in text_lower:
        return f"We're keeping things plain-English here on the canvas! But conceptually, Databricks handles this behind the scenes using clear configuration parameters. You don't need to write lines of raw infra setup; you just reference your target workspace keywords: {', '.join(module_data['keywords'])}."
    else:
        return f"That's a great question about **{active_module}**. In simple terms, remember that this component focuses directly on managing your {module_data['keywords'][0].lower()} and {module_data['keywords'][1].lower()} seamlessly so production systems remain safe."

# --- APP LAYOUT ---
str.markdown("<div class='main-header'>🎓 Databricks MLOps Canvas Academy</div>", unsafe_allowed_html=True)

# Split screen workspace layout (Canvas Design)
left_col, right_col = str.columns([2, 3], gap="large")

# ==========================================
# LEFT PANEL: MODULE EXPLORER
# ==========================================
with left_col:
    str.markdown("<h3 style='color: #2c3e50;'>🗺️ Module Navigator</h3>", unsafe_allowed_html=True)
    str.write("Select a topic from the course playlist to load its concept blueprint onto the main workspace canvas.")
    
    # Create interactive list of modules
    for mod_title in COURSE_MODULES.keys():
        if str.button(mod_title, use_container_width=True, type="secondary" if str.session_state.current_module != mod_title else "primary"):
            str.session_state.current_module = mod_title
            str.rerun()
            
    str.markdown("---")
    str.caption("💡 Tip: Walk through the items sequentially from Introduction down to Lakehouse Monitoring to see how a model travels from an idea to production.")

# ==========================================
# RIGHT PANEL: INTERACTIVE PLAYGROUND
# ==========================================
with right_col:
    # Setup interactive view tabs
    tab_explain, tab_chat, tab_quiz = str.tabs(["📖 Concept Explanation", "💬 Ask Questions", "🧠 Quiz Me"])
    
    selected_data = COURSE_MODULES[str.session_state.current_module]
    
    # --- TAB 1: PLAIN ENGLISH EXPLANATION ---
    with tab_explain:
        str.markdown(f"<div class='section-box'><h3>Active Concept: {str.session_state.current_module}</h3></div>", unsafe_allowed_html=True)
        
        str.markdown("#### 🔍 What is this in Plain English?")
        str.write(selected_data["summary"])
        
        str.markdown("#### 💡 Real-World Analogy")
        str.info(selected_data["analogy"])
        
        str.markdown("#### 🔑 Key Pillars to Remember")
        cols = str.columns(len(selected_data["keywords"]))
        for idx, kw in enumerate(selected_data["keywords"]):
            cols[idx].markdown(f"**• {kw}**")
            
    # --- TAB 2: INTERACTIVE Q&A ---
    with tab_chat:
        str.markdown(f"### 💬 Conversational Tutor")
        str.caption(f"Ask any question about **{str.session_state.current_module}** using plain language.")
        
        # Display Conversational Canvas history
        for msg in str.session_state.chat_history:
            if msg["role"] == "user":
                str.markdown(f"<div class='chat-bubble-user'><b>You:</b> {msg['content']}</div>", unsafe_allowed_html=True)
            else:
                str.markdown(f"<div class='chat-bubble-bot'><b>Tutor:</b> {msg['content']}</div>", unsafe_allowed_html=True)
                
        # Handle chat inputs
        with str.form(key="chat_input_form", clear_on_submit=True):
            user_query = str.text_input("Ask a question (e.g., 'Why do we need this?', 'Give me an analogy'):", placeholder="Type your question here...")
            submit_query = str.form_submit_button("Send Query")
            
            if submit_query and user_query:
                str.session_state.chat_history.append({"role": "user", "content": user_query})
                bot_ans = get_ai_response(user_query, str.session_state.current_module)
                str.session_state.chat_history.append({"role": "bot", "content": bot_ans})
                str.rerun()

    # --- TAB 3: QUIZ ENGINE ---
    with tab_quiz:
        str.markdown("### 🧠 Conceptual Check-In")
        str.write("Test your understanding of the Databricks MLOps lifecycle with this conceptual quiz.")
        
        # Render quiz forms inside canvas block
        with str.form(key="quiz_evaluation_form"):
            for q in QUIZ_QUESTIONS:
                str.markdown(f"**Question {q['id']}:** {q['question']}")
                str.session_state.user_answers[q['id']] = str.radio(
                    "Select your answer:", 
                    options=q['options'], 
                    key=f"q_radio_{q['id']}",
                    label_visibility="collapsed"
                )
                str.markdown("<br>", unsafe_allowed_html=True)
                
            submit_quiz = str.form_submit_button("Submit My Answers")
            
            if submit_quiz:
                correct_count = 0
                for q in QUIZ_QUESTIONS:
                    if str.session_state.user_answers[q['id']] == q['correct']:
                        correct_count += 1
                str.session_state.quiz_score = f"{correct_count} / {len(QUIZ_QUESTIONS)}"
                
        if str.session_state.quiz_score is not None:
            str.markdown("---")
            str.markdown(f"### 📊 Result: Your Score is `{str.session_state.quiz_score}`")
            if "3" in str.session_state.quiz_score:
                str.success("Perfect score! You've mastered the core architectural concepts of Databricks MLOps.")
            else:
                str.warning("You missed a few spots. Toggle back to the 'Concept Explanation' or explore other modules on the left to brush up on the fundamentals!")
