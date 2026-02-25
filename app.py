import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
from config import GROK_API_KEY
from utils.auth import show_auth_page, update_user_data
from utils.chatbot import chat_with_grok
from gtts import gTTS
import base64
import tempfile
import os

# Page config
st.set_page_config(
    page_title="AI Learn - Smart Learning Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Check authentication
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    show_auth_page()
    st.stop()

# Professional Dark Theme CSS (Kiro-style)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main app background - Dark */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
    }
    
    /* Sidebar - Dark */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f1419 0%, #1a1f2e 100%);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: #e0e0e0;
    }
    
    /* Main content area */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Cards - Dark */
    .pro-card {
        background: linear-gradient(135deg, #1e2139 0%, #252a42 100%);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        margin: 15px 0;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    .pro-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.3);
        border-color: rgba(102, 126, 234, 0.4);
    }
    
    /* Gradient headers - Dark */
    .gradient-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 40px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* XP Badge */
    .xp-badge {
        background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
        padding: 10px 20px;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
        margin: 5px;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3);
        color: #1a1f3a;
    }
    
    /* Progress bars - Dark */
    .progress-bar {
        background: rgba(102, 126, 234, 0.1);
        border-radius: 10px;
        height: 25px;
        overflow: hidden;
        margin: 10px 0;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        height: 100%;
        transition: width 0.8s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 600;
    }
    
    /* Module items - Dark */
    .module-item {
        background: linear-gradient(135deg, #1e2139 0%, #252a42 100%);
        padding: 15px 20px;
        margin: 10px 0;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        transition: all 0.3s;
        border-left: 3px solid #667eea;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    .module-item:hover {
        transform: translateX(10px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        border-color: rgba(102, 126, 234, 0.4);
    }
    
    .module-item.completed {
        border-left-color: #4caf50;
        background: linear-gradient(135deg, #1a2e1f 0%, #243329 100%);
    }
    
    .module-item.locked {
        opacity: 0.5;
        cursor: not-allowed;
    }
    
    /* Stat cards - Dark */
    .stat-card {
        background: linear-gradient(135deg, #1e2139 0%, #252a42 100%);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        margin: 10px;
        border-top: 3px solid #667eea;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    .stat-number {
        font-size: 36px;
        font-weight: 700;
        color: #667eea;
    }
    
    /* Buttons - Dark */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 10px 25px;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
    }
    
    /* Text colors - Dark */
    h1, h2, h3, h4, h5, h6 {
        color: #e0e0e0 !important;
    }
    
    p, span, div, label {
        color: #b0b0b0;
    }
    
    /* Input fields - Dark */
    .stTextInput>div>div>input {
        background: #1e2139;
        color: #e0e0e0;
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-radius: 8px;
    }
    
    /* Chat messages - Dark */
    .chat-message-user {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 16px;
        border-radius: 15px;
        margin: 10px 0;
        text-align: right;
        border-bottom-right-radius: 5px;
    }
    
    .chat-message-assistant {
        background: linear-gradient(135deg, #1e2139 0%, #252a42 100%);
        color: #e0e0e0;
        padding: 12px 16px;
        border-radius: 15px;
        margin: 10px 0;
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-bottom-left-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        'name': st.session_state.username,
        'xp': 0,
        'completed_lessons': [],
        'badges': [],
        'current_course': None,
        'streak': 0,
        'quiz_scores': [],
        'time_spent': {},
        'last_login': datetime.now().strftime("%Y-%m-%d")
    }

if 'courses' not in st.session_state:
    st.session_state.courses = {
        'Python': {
            'modules': ['Introduction', 'Variables', 'Conditions', 'Loops', 'Functions', 'OOP', 'Projects'],
            'icon': '🐍',
            'description': 'Master Python programming from basics to advanced'
        },
        'Java': {
            'modules': ['Basics', 'OOP', 'Collections', 'Multithreading', 'Projects'],
            'icon': '☕',
            'description': 'Learn Java and object-oriented programming'
        },
        'Web Development': {
            'modules': ['HTML', 'CSS', 'JavaScript', 'React', 'Backend', 'Projects'],
            'icon': '🌐',
            'description': 'Build modern web applications'
        },
        'Data Science': {
            'modules': ['NumPy', 'Pandas', 'Visualization', 'ML Basics', 'Projects'],
            'icon': '📊',
            'description': 'Analyze data and build ML models'
        }
    }

if 'voice_enabled' not in st.session_state:
    st.session_state.voice_enabled = False

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'show_chat' not in st.session_state:
    st.session_state.show_chat = False

# Voice function
def speak_text(text):
    """Generate and play voice"""
    if st.session_state.voice_enabled:
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                temp_file = fp.name
            
            tts = gTTS(text=text[:200], lang='en', tld='co.uk', slow=False)
            tts.save(temp_file)
            
            with open(temp_file, 'rb') as audio_file:
                audio_bytes = audio_file.read()
            
            os.unlink(temp_file)
            audio_base64 = base64.b64encode(audio_bytes).decode()
            
            audio_html = f'<audio autoplay><source src="data:audio/mp3;base64,{audio_base64}"></audio>'
            st.markdown(audio_html, unsafe_allow_html=True)
        except:
            pass

# Sidebar
with st.sidebar:
    selected = option_menu(
        "AI Learn Platform",
        ["Home", "Courses", "Challenges", "Playground", "My Progress", "Certificates", "Analytics", "Leaderboard", "Reviews", "Admin"],
        icons=['house-fill', 'book-fill', 'trophy-fill', 'code-slash', 'graph-up-arrow', 'award-fill', 'bar-chart-fill', 'star-fill', 'chat-left-text-fill', 'gear-fill'],
        menu_icon="mortarboard-fill",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f0f8ff"},
            "icon": {"color": "#1976d2", "font-size": "20px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px", "--hover-color": "#e3f2fd"},
            "nav-link-selected": {"background": "linear-gradient(135deg, #1976d2 0%, #2196f3 100%)", "color": "white"},
        }
    )
    
    st.markdown("---")
    
    # User info - compact
    st.markdown(f"**👤 {st.session_state.user_data['name']}**")
    st.markdown(f"⭐ {st.session_state.user_data['xp']} XP • 🔥 {st.session_state.user_data['streak']} days")
    
    st.markdown("---")
    
    # AI Guide toggle
    st.session_state.guide_enabled = st.checkbox("👩‍🏫 AI Guide", value=st.session_state.get('guide_enabled', True))
    st.session_state.voice_enabled = st.checkbox("🔊 Voice", value=st.session_state.get('voice_enabled', False))
    
    # Show AI Guide in sidebar if enabled
    if st.session_state.guide_enabled:
        from utils.ai_guide import show_ai_guide
        show_ai_guide(selected, position="sidebar")
    
    st.markdown("---")
    if st.button("🚪 Logout", width="stretch"):
        update_user_data(st.session_state.username, st.session_state.user_data)
        st.session_state.authenticated = False
        st.rerun()

# Main content routing
if selected == "Home":
    from pages import home
    home.show()
elif selected == "Courses":
    from pages import courses
    courses.show()
elif selected == "Challenges":
    from pages import challenges
    challenges.show()
elif selected == "Playground":
    from pages import playground
    playground.show()
elif selected == "My Progress":
    from pages import progress
    progress.show()
elif selected == "Certificates":
    from pages import certificates
    certificates.show()
elif selected == "Analytics":
    from pages import analytics
    analytics.show()
elif selected == "Leaderboard":
    from pages import leaderboard
    leaderboard.show()
elif selected == "Reviews":
    from pages import reviews
    reviews.show()
elif selected == "Admin":
    from pages import admin
    admin.show()

# Chatbot at bottom - improved format
st.markdown("---")

# Chat container with better styling
st.markdown("""
<div style="background: linear-gradient(135deg, #1976d2 0%, #2196f3 100%); 
            padding: 20px; border-radius: 15px; margin: 20px 0;">
    <h2 style="color: white; margin: 0; display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 32px;">💬</span>
        <span>Chat with Sophia - AI Assistant</span>
    </h2>
    <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0; font-size: 14px;">
        Ask me anything about programming, courses, or learning tips!
    </p>
</div>
""", unsafe_allow_html=True)

# Chat history display
if st.session_state.chat_history:
    st.markdown("### 💭 Recent Conversation")
    
    # Show last 5 messages
    for chat in st.session_state.chat_history[-5:]:
        # User message
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #1976d2 0%, #2196f3 100%); 
                    color: white; padding: 15px 20px; border-radius: 15px; 
                    margin: 10px 0; border-bottom-right-radius: 5px;
                    box-shadow: 0 2px 8px rgba(25, 118, 210, 0.3);">
            <div style="font-weight: 600; margin-bottom: 5px; opacity: 0.9;">👤 You</div>
            <div style="font-size: 15px;">{chat['user']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Assistant message
        st.markdown(f"""
        <div style="background: white; color: #333; padding: 15px 20px; 
                    border-radius: 15px; margin: 10px 0; border-bottom-left-radius: 5px;
                    border: 2px solid #e3f2fd;
                    box-shadow: 0 2px 8px rgba(25, 118, 210, 0.1);">
            <div style="font-weight: 600; margin-bottom: 5px; color: #1976d2;">👩‍🏫 Sophia</div>
            <div style="font-size: 15px; line-height: 1.6;">{chat['assistant']}</div>
        </div>
        """, unsafe_allow_html=True)

# Chat input form
st.markdown("### ✍️ Ask a Question")

col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input(
        "Your question:",
        placeholder="e.g., Explain Python loops, What is OOP?, How do I earn badges?",
        label_visibility="collapsed",
        key="chat_input_field"
    )

with col2:
    send_button = st.button("📤 Send", width="stretch", type="primary")

if send_button and user_input:
    with st.spinner("🤔 Sophia is thinking..."):
        success, response = chat_with_grok(user_input, [])
        if success:
            st.session_state.chat_history.append({'user': user_input, 'assistant': response})
            st.rerun()
        else:
            st.error(f"❌ Chat error: {response}")
