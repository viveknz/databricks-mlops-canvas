import streamlit as st

# --- INITIALIZATION & LAYOUT CONFIG ---
st.set_page_config(layout="wide", page_title="Databricks MLOps Academy")

# Initialize persistent session states
if 'current_module' not in st.session_state:
    st.session_state.current_module = "1. Introduction to MLOps"
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = None
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

# --- PLAIN ENGLISH CURRICULUM DATA ---
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
    "6. Deploying model serving endpoint": {
        "summary": "An endpoint is the physical web address where your serving architecture lives. Deploying it means making that address active so apps can securely send data and receive predictions over HTTPS.",
        "analogy": "It's like turning on a store's telephone hotline. Once deployed, anyone with the correct phone number (the endpoint URL) and permission can call up and ask the model questions.",
        "keywords": ["Endpoint URL", "Payload", "JSON response", "Scaling"]
    },
    "7. Databricks Asset Bundles": {
        "summary": "Databricks Asset Bundles allow you to bundle all your code, notebooks, test settings, and infrastructure configs into a single, structured project package. This makes moving code across different spaces predictable.",
        "analogy": "Imagine you are moving houses. Instead of carrying individual clothes, books, and plates loosely in your arms, you pack them cleanly into a standard moving crate. DABs are that moving crate for your machine learning project.",
        "keywords": ["Infrastructure as Code", "Project Structure", "Configuration", "DABs"]
    },
    "8. CI/CD and deployment strategies": {
        "summary": "CI/CD (Continuous Integration & Continuous Deployment) means using automated rules to test and ship code. Instead of manually clicking deploy, a robot automatically checks your work for errors every time you update it.",
        "analogy": "It's like an automated factory assembly line. Before a car leaves the factory, automated arms shake the doors and test the brakes. If anything fails, the line stops automatically before the broken car can reach a customer.",
        "keywords": ["GitHub Actions", "Automation", "Unit Testing", "Rollback"]
    },
    "9. Intro to monitoring": {
        "summary": "Once a model goes live, it encounters real-world data, which constantly changes. Monitoring means tracking the incoming data and the model’s answers to ensure the model isn't slowly losing its accuracy.",
        "analogy": "Imagine you train a weather bot in winter, and suddenly summer arrives. The data looks completely different. Monitoring is the alarm system that rings when your bot starts making weird summer predictions based on winter logic.",
        "keywords": ["Data Drift", "Model Decay", "Alerts", "Performance"]
    },
    "10. Lakehouse monitoring": {
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

# --- TEXT SIMULATION ENGINE ---
def get_ai_response(user_text, active_module):
    text_lower = user_text.lower()
    module_data = COURSE_MODULES[active_module]
    
    if "why" in text_lower or "purpose" in text_lower:
        return f"The main purpose of **{active_module}** is stability. It prevents the common friction point where a machine learning system works fine on an individual's machine but breaks instantly when launched live."
    elif "example" in text_lower or "analogy" in text_lower:
        return f"Here is another way to picture it: {module_data['analogy']}"
    else:
        return f"Regarding **{active_module}**: This layer fundamentally centers on safeguarding your operational system while managing {module_data['keywords'][0].lower()} and {module_data['keywords'][1].lower()} safely."

# --- APP INTERFACE BUILD ---
st.title("🎓 Databricks MLOps Canvas Academy")
st.write("---")

# Setup layout columns
left_col, right_col = st.columns([2, 3], gap="large")

# Left Column: Navigation Sidebar Panel
with left_col:
    st.header("🗺️ Module Navigator")
    st.caption("Select a topic below to explore its plain-English blueprint on the right.")
    
    for mod_title in COURSE_MODULES.keys():
        is_active = (st.session_state.current_module == mod_title)
        if st.button(mod_title, use_container_width=True, type="primary" if is_active else "secondary"):
            st.session_state.current_module = mod_title
            st.rerun()

# Right Column: The Core Content Canvas Workspace
with right_col:
    tab_explain, tab_chat, tab_quiz = st.tabs(["📖 Plain-English Concept", "💬 Ask Questions", "🧠 Quiz Me"])
    selected_data = COURSE_MODULES[st.session_state.current_module]
    
    # 1. Explanation Panel
    with tab_explain:
        st.subheader(st.session_state.current_module)
        
        st.markdown("### 🔍 What is this?")
        st.write(selected_data["summary"])
        
        st.markdown("### 💡 Real-World Analogy")
        st.info(selected_data["analogy"])
        
        st.markdown("### 🔑 Key Concepts")
        for kw in selected_data["keywords"]:
            st.markdown(f"**• {kw}**")
            
    # 2. Plain English Chat Panel
    with tab_chat:
        st.subheader("💬 Interactive Explanations")
        st.caption(f"Ask anything about '{st.session_state.current_module}' without worrying about technical jargon.")
        
        # Render historical interaction logs
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.chat_message("user").write(msg["content"])
            else:
                st.chat_message("assistant").write(msg["content"])
                
        # Question input structure
        with st.form(key="chat_form", clear_on_submit=True):
            user_query = st.text_input("Your question:", placeholder="e.g., 'Give me an analogy' or 'Why do we need this?'")
            if st.form_submit_button("Ask Tutor"):
                if user_query.strip():
                    st.session_state.chat_history.append({"role": "user", "content": user_query})
                    answer = get_ai_response(user_query, st.session_state.current_module)
                    st.session_state.chat_history.append({"role": "bot", "content": answer})
                    st.rerun()

    # 3. Quiz Module Panel
    with tab_quiz:
        st.subheader("🧠 Concept Check-In")
        st.write("Test your understanding of the core concepts.")
        
        with st.form(key="quiz_form"):
            for q in QUIZ_QUESTIONS:
                st.write(f"**Question {q['id']}:** {q['question']}")
                st.session_state.user_answers[q['id']] = st.radio(
                    "Choose one:", options=q['options'], key=f"ans_{q['id']}", label_visibility="collapsed"
                )
                st.write("")
                
            if st.form_submit_button("Submit Quiz"):
                score = sum(1 for q in QUIZ_QUESTIONS if st.session_state.user_answers[q['id']] == q['correct'])
                st.session_state.quiz_score = f"{score} / {len(QUIZ_QUESTIONS)}"
                
        if st.session_state.quiz_score is not None:
            st.markdown("---")
            st.metric("Your Score", st.session_state.quiz_score)
            if "3" in st.session_state.quiz_score:
                st.success("Excellent work! You perfectly grasp how models move from tracking to live deployment environments.")
            else:
                st.warning("Take another look through the module explanations on the left side to master these concepts!")
