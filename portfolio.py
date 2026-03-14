import streamlit as st
import pandas as pd
from PIL import Image
import base64
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Muhammad Sohail - Data Scientist",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
def local_css():
    st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Header styling */
    .big-font {
        font-size: 3rem !important;
        font-weight: 700;
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .subtitle-font {
        font-size: 1.2rem !important;
        color: #94a3b8;
    }
    
    /* Section headers */
    .section-header {
        font-size: 2rem !important;
        font-weight: 600;
        color: white;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #2563eb;
    }
    
    /* Project cards */
    .project-card {
        background: #1e293b;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #334155;
        transition: transform 0.3s;
        height: 100%;
    }
    .project-card:hover {
        transform: translateY(-5px);
        border-color: #2563eb;
    }
    
    /* Unified skill tags */
    .skill-tag, .soft-skill-tag {
        display: inline-block;
        background: #10b98120;
        color: #10b981;
        padding: 0.4rem 1.2rem;
        border-radius: 30px;
        font-size: 0.9rem;
        margin: 0.3rem;
        border: 1px solid #10b98140;
        font-weight: 500;
    }
    
    /* Metrics styling */
    .metric-container {
        background: #0f172a;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #334155;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2563eb;
    }
    .metric-label {
        color: #94a3b8;
        font-size: 0.9rem;
    }
    
    /* Education card */
    .education-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #334155;
        margin-bottom: 1rem;
    }
    
    /* Achievement badges */
    .achievement-badge {
        display: inline-block;
        background: #f59e0b20;
        color: #f59e0b;
        padding: 0.3rem 1rem;
        border-radius: 30px;
        font-size: 0.8rem;
        margin: 0.2rem;
        border: 1px solid #f59e0b40;
        font-weight: 600;
    }
    
    /* Language badges */
    .language-badge {
        display: inline-block;
        background: #3b82f620;
        color: #3b82f6;
        padding: 0.5rem 1.5rem;
        border-radius: 30px;
        font-size: 1rem;
        margin: 0.5rem;
        border: 1px solid #3b82f640;
        font-weight: 500;
    }
    
    /* Professional skills tags */
    .professional-tag {
        display: inline-block;
        background: #f59e0b20;
        color: #f59e0b;
        padding: 0.4rem 1.2rem;
        border-radius: 30px;
        font-size: 0.9rem;
        margin: 0.3rem;
        border: 1px solid #f59e0b40;
        font-weight: 500;
    }

    /* Contact info styling */
    .contact-info {
        color: #94a3b8;
        margin: 0.8rem 0;
        font-size: 1rem;
    }
    
    /* Open to section styling */
    .open-to-badge {
        display: inline-block;
        background: #10b98120;
        color: #10b981;
        padding: 0.5rem 1.2rem;
        border-radius: 30px;
        font-size: 0.95rem;
        border: 1px solid #10b98140;
        font-weight: 500;
        transition: transform 0.2s;
    }
    .open-to-badge:hover {
        transform: translateY(-2px);
        background: #10b98130;
    }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Helper function to create buttons
def create_button(text, url, icon="🔗"):
    return f'<a href="{url}" target="_blank" style="background: linear-gradient(90deg, #2563eb, #7c3aed); color: white; padding: 0.5rem 1rem; border-radius: 5px; text-decoration: none; display: inline-block; margin: 0.2rem; font-size: 0.9rem; font-weight: 500; transition: all 0.3s;"><span style="margin-right: 0.3rem;">{icon}</span>{text}</a>'

# ==================== HERO SECTION ====================
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <h1 class="big-font">Muhammad Sohail</h1>
    <p class="subtitle-font">Data Scientist | Machine Learning Engineer | AI Developer</p>
    <div style="margin: 1rem auto; max-width: 700px;">
        <span class="achievement-badge">⭐ Best Project Award</span>
        <span class="achievement-badge">🚀 5 Apps in 5 Weeks</span>
    </div>
    <p style="color: #94a3b8; max-width: 650px; margin: 2rem auto; font-size: 1.1rem; line-height: 1.6;">
        Passionate Data Science graduate with hands-on experience in building AI solutions.
        Looking for opportunities to apply my skills in real-world projects.
    </p>
</div>
""", unsafe_allow_html=True)

# ==================== QUICK STATS ====================
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="metric-container">
        <div class="metric-value">15+</div>
        <div class="metric-label">Projects</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="metric-container">
        <div class="metric-value">10+</div>
        <div class="metric-label">Technologies</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="metric-container">
        <div class="metric-value">5</div>
        <div class="metric-label">Live Demos</div>
    </div>
    """, unsafe_allow_html=True)

# ==================== ABOUT SECTION ====================
st.markdown('<h2 class="section-header">📋 About Me</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    # Profile photo - make sure this URL is correct
    profile_img = "https://raw.githubusercontent.com/sohail189/portfolio/main/profile.png"
    st.image(profile_img, caption="Muhammad Sohail", use_column_width=True)
with col2:
    st.markdown("""
    I'm a **Data Science graduate** with a strong foundation in machine learning, 
    statistical analysis, and AI development. During my academic journey, I've completed 
    multiple hands-on projects that demonstrate my ability to solve real-world problems 
    using data-driven approaches.
    
    **🎯 What I Bring:**
    - Strong problem-solving skills and analytical thinking
    - Hands-on experience with modern AI/ML technologies
    - Passion for learning and staying updated with latest trends
    - Ability to work both independently and in teams
    - Excellent communication and presentation skills
    
    **🎓 Education:** Bachelor in Data Science - Government College University, Faisalabad (2021-2025)
    
    **📚 Coursework:** Machine Learning, Deep Learning, Statistical Analysis, Database Systems, Big Data Analytics, Cloud Computing, Python Programming, Linear Algebra
    
    **🐙 GitHub:** [github.com/sohail189](https://github.com/sohail189)
    """)

# ==================== EDUCATION DETAILS ====================
st.markdown('<h2 class="section-header">🎓 Education</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="education-card">
        <h3 style="color: #2563eb;">Bachelor in Data Science</h3>
        <p style="color: white; font-size: 1.1rem;">Government College University, Faisalabad</p>
        <p style="color: #94a3b8;">2021 - 2025</p>
        <p style="color: #94a3b8; margin-top: 0.5rem;">
            <strong>Relevant Coursework:</strong><br>
            • Machine Learning & Deep Learning<br>
            • Statistical Analysis & Probability<br>
            • Database Systems & SQL<br>
            • Big Data Analytics<br>
            • Cloud Computing Basics<br>
            • Data Visualization<br>
            • Python Programming<br>
            • Linear Algebra & Calculus
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="education-card">
        <h3 style="color: #10b981;">🏆 Academic Achievements</h3>
        <p style="color: #94a3b8; margin-top: 0.5rem;">
            • <strong>Best Project Award</strong> - Data Science Final Year Project<br>
            • <strong>5-Week AI Sprint</strong> - Completed 5 AI projects in 5 weeks
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== TECHNICAL SKILLS ====================
st.markdown('<h2 class="section-header">🛠️ Technical Skills</h2>', unsafe_allow_html=True)

skills_data = {
    "Programming Languages": ["Python", "SQL", "R"],
    "ML/AI Frameworks": ["TensorFlow", "Scikit-learn", "LangChain", "OpenAI API"],
    "Data Science": ["Pandas", "NumPy", "Feature Engineering", "Statistical Analysis"],
    "Visualization": ["Power BI", "Matplotlib", "Seaborn", "Plotly"],
    "Deployment": ["Streamlit", "FastAPI", "Git/GitHub"],
    "Tools": ["Jupyter", "VS Code", "Google Colab"]
}

for category, skills in skills_data.items():
    st.markdown(f"**{category}**")
    skills_html = ""
    for skill in skills:
        skills_html += f'<span class="skill-tag">{skill}</span>'
    st.markdown(skills_html, unsafe_allow_html=True)
    st.markdown("")

# ==================== SOFT SKILLS ====================
st.markdown('<h2 class="section-header">🤝 Soft Skills</h2>', unsafe_allow_html=True)

soft_skills = [
    "Quick Learner", "Problem Solving", "Critical Thinking", "Team Collaboration",
    "Communication", "Time Management", "Adaptability", "Attention to Detail",
    "Presentation Skills", "Technical Writing", "Creativity", "Work Ethic"
]

soft_skills_html = ""
for skill in soft_skills:
    soft_skills_html += f'<span class="soft-skill-tag">{skill}</span>'

st.markdown(f"""
<div style="background: #0f172a; padding: 1.5rem; border-radius: 10px; border: 1px solid #334155;">
    <div>
        {soft_skills_html}
    </div>
</div>
""", unsafe_allow_html=True)

# ==================== LANGUAGES ====================
st.markdown('<h2 class="section-header">🗣️ Languages</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div style="text-align: center;">
        <span class="language-badge">🇵🇰 Urdu - Native</span>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style="text-align: center;">
        <span class="language-badge">🇬🇧 English - Professional</span>
    </div>
    """, unsafe_allow_html=True)

# ==================== ACADEMIC PROJECTS ====================
st.markdown('<h2 class="section-header">🚀 Academic Projects</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="project-card">
        <h3>🏥 Medical Risk Prediction System</h3>
        <p style="color: #94a3b8;"><strong>Final Year Project</strong> - Dual ML model system for early detection of heart and liver diseases.</p>
        <div>
            <span class="skill-tag">Python</span>
            <span class="skill-tag">CatBoost</span>
            <span class="skill-tag">SVM</span>
            <span class="skill-tag">Streamlit</span>
        </div>
        <p style="margin-top: 1rem; color: #e2e8f0;">
            <strong>Outcome:</strong> Developed a working prototype. Presented at university symposium.
        </p>
        <div style="margin-top: 1.5rem;">
            {create_button('View Code', 'https://github.com/sohail189/medical-risk-prediction', '📁')}
            {create_button('Live Demo', 'https://medical-predictor.streamlit.app', '🚀')}
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-card">
        <h3>📊 Customer Churn Prediction</h3>
        <p style="color: #94a3b8;"><strong>Class Project</strong> - Analyzing customer data to predict churn for telecom dataset.</p>
        <div>
            <span class="skill-tag">Python</span>
            <span class="skill-tag">Power BI</span>
            <span class="skill-tag">Scikit-learn</span>
            <span class="skill-tag">Pandas</span>
        </div>
        <p style="margin-top: 1rem; color: #e2e8f0;">
            <strong>Outcome:</strong> Built interactive dashboard and ML model.
        </p>
        <div style="margin-top: 1.5rem;">
            {create_button('View Code', 'https://github.com/sohail189/churn-prediction', '📁')}
            {create_button('Live Demo', 'https://churn-dashboard.streamlit.app', '🚀')}
        </div>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="project-card">
        <h3>✈️ AI Travel Intelligence Assistant</h3>
        <p style="color: #94a3b8;"><strong>Personal Project</strong> - LLM-powered travel planner using LangChain.</p>
        <div>
            <span class="skill-tag">LangChain</span>
            <span class="skill-tag">OpenAI API</span>
            <span class="skill-tag">Streamlit</span>
            <span class="skill-tag">Python</span>
        </div>
        <p style="margin-top: 1rem; color: #e2e8f0;">
            <strong>Outcome:</strong> Built functional travel planner with 3-second response time.
        </p>
        <div style="margin-top: 1.5rem;">
            {create_button('View Code', 'https://github.com/sohail189/ai-travel-planner', '📁')}
            {create_button('Live Demo', 'https://travel-planner.streamlit.app', '🚀')}
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-card">
        <h3>📄 Resume ATS Scanner</h3>
        <p style="color: #94a3b8;"><strong>NLP Project</strong> - Analyze resume compatibility with job descriptions.</p>
        <div>
            <span class="skill-tag">NLP</span>
            <span class="skill-tag">spaCy</span>
            <span class="skill-tag">Python</span>
            <span class="skill-tag">Streamlit</span>
        </div>
        <p style="margin-top: 1rem; color: #e2e8f0;">
            <strong>Outcome:</strong> Built during NLP coursework. Helps students optimize resumes.
        </p>
        <div style="margin-top: 1.5rem;">
            {create_button('View Code', 'https://github.com/sohail189/ats-resume-scanner', '📁')}
            {create_button('Live Demo', 'https://resume-scanner.streamlit.app', '🚀')}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==================== OTHER PROJECTS ====================
st.markdown('<h2 class="section-header">📚 Other Projects</h2>', unsafe_allow_html=True)

other_projects = [
    {
        "title": "📈 Sales Dashboard",
        "desc": "Interactive dashboard using Power BI for sales data analysis",
        "tech": "Power BI, Excel"
    },
    {
        "title": "📊 COVID-19 Analysis",
        "desc": "Exploratory data analysis of COVID-19 trends using Python",
        "tech": "Python, Pandas, Matplotlib"
    },
    {
        "title": "🎬 Movie Recommendation",
        "desc": "Content-based recommendation system",
        "tech": "Python, Scikit-learn, Streamlit"
    },
    {
        "title": "📝 Sentiment Analysis",
        "desc": "Twitter sentiment analysis using NLP",
        "tech": "Python, NLTK"
    }
]

cols = st.columns(4)
for i, project in enumerate(other_projects):
    with cols[i]:
        st.markdown(f"""
        <div class="project-card" style="padding: 1rem; text-align: center;">
            <h4 style="color: white; font-size: 1.2rem; margin-bottom: 0.5rem;">{project['title']}</h4>
            <p style="color: #94a3b8; font-size: 0.85rem;">{project['desc']}</p>
            <p style="color: #10b981; font-size: 0.8rem; margin-top: 0.5rem;">{project['tech']}</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== PROFESSIONAL SKILLS ====================
st.markdown('<h2 class="section-header">💼 Professional Skills</h2>', unsafe_allow_html=True)

professional_skills = [
    "Data-Driven Storytelling", "Business Impact Focus", "Agile Problem-Solving",
    "Proactive Learner", "Cross-functional Collaboration", "Technical Documentation"
]

prof_skills_html = ""
for skill in professional_skills:
    prof_skills_html += f'<span class="professional-tag">{skill}</span>'

st.markdown(f"""
<div style="background: #0f172a; padding: 1.5rem; border-radius: 10px; border: 1px solid #334155;">
    <div>
        {prof_skills_html}
    </div>
</div>
""", unsafe_allow_html=True)

# ==================== GITHUB ====================
st.markdown('<h2 class="section-header">📁 GitHub</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <div style="text-align: center; background: #1e293b; padding: 2rem; border-radius: 10px; border: 1px solid #334155;">
        <h3 style="color: white;">🐙 GitHub Profile</h3>
        <p style="color: #94a3b8; margin: 1rem 0;">Check out all my projects and code repositories</p>
        {create_button('Visit GitHub', 'https://github.com/sohail189', '🔗')}
    </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown(f"""
    <div style="text-align: center; background: #1e293b; padding: 2rem; border-radius: 10px; border: 1px solid #334155;">
        <h3 style="color: white;">📊 Portfolio Stats</h3>
        <p style="color: #94a3b8; margin: 0.5rem 0;">⭐ 15+ Public Repositories</p>
        <p style="color: #94a3b8; margin: 0.5rem 0;">🍴 10+ Projects Deployed</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== CONTACT SECTION ====================
st.markdown('<h2 class="section-header">📫 Contact Me</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("""
    <div style="background: #1e293b; padding: 2rem; border-radius: 10px; border: 1px solid #334155;">
        <h3 style="color: white; margin-bottom: 1.5rem;">Contact Information</h3>
        <p class="contact-info">📧 <strong>Email:</strong> sm7933494@gmail.com</p>
        <p class="contact-info">📱 <strong>Phone:</strong> +92 340 7788425</p>
        <p class="contact-info">📍 <strong>Location:</strong> Faisalabad, Pakistan</p>
        <p class="contact-info">🌐 <strong>GitHub:</strong> github.com/sohail189</p>
        <p class="contact-info">💼 <strong>LinkedIn:</strong> /in/muhammad-sohail-14a839354</p>
        
        
    </div>
    """, unsafe_allow_html=True)

with col2:
    with st.form("contact_form"):
        st.markdown("""
        <div style="background: #1e293b; padding: 2rem; border-radius: 10px; border: 1px solid #334155;">
            <h3 style="color: white; margin-bottom: 1.5rem;">📝 Send Message</h3>
        """, unsafe_allow_html=True)
        
        name = st.text_input("Your Name", placeholder="John Doe")
        email = st.text_input("Your Email", placeholder="john@example.com")
        message = st.text_area("Message", placeholder="Tell me about your requirement...", height=150)
        
        col1, col2, col3 = st.columns(3)
        with col2:
            submitted = st.form_submit_button("📤 Send Message", use_container_width=True)
        
        if submitted:
            st.success("✅ Thanks for reaching out! I'll respond within 24-48 hours.")
            st.balloons()
        
        st.markdown("</div>", unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("""
<hr style="border: 1px solid #334155; margin: 3rem 0 1rem 0;">
<div style="display: flex; justify-content: space-between; align-items: center; color: #94a3b8; font-size: 0.9rem;">
    <p>© 2024 Muhammad Sohail | Data Scientist</p>
    <p>⚡ Built with Streamlit | <a href="https://github.com/sohail189" style="color: #94a3b8;">GitHub</a></p>
</div>
""", unsafe_allow_html=True)