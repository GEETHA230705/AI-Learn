import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
from config import GROK_API_KEY
from utils.auth import show_auth_page, update_user_data
from utils.chatbot import chat_with_grok

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

# Sidebar
with st.sidebar:
    selected = option_menu(
        "AI Learn Platform",
        ["Home", "Courses", "My Progress", "Certificates", "Analytics", "Admin"],
        icons=['house-fill', 'book-fill', 'graph-up-arrow', 'award-fill', 'bar-chart-fill', 'gear-fill'],
        menu_icon="mortarboard-fill",
        default_index=0,
    )
    
    st.markdown("---")
    st.markdown(f"### 👤 {st.session_state.user_data['name']}")
    st.markdown(f"⭐ **{st.session_state.user_data['xp']} XP**")
    st.markdown(f"🔥 **Streak:** {st.session_state.user_data['streak']} days")
    
    if st.session_state.user_data['badges']:
        st.markdown("### 🏆 Badges")
        st.write(' '.join(st.session_state.user_data['badges']))
    
    st.markdown("---")
    
    # AI Chat in Sidebar
    st.markdown("### 🤖 AI Assistant")
    with st.expander("💬 Chat", expanded=False):
        if st.session_state.chat_history:
            for chat in st.session_state.chat_history[-2:]:
                st.markdown(f"**You:** {chat['user'][:50]}...")
                st.info(f"**AI:** {chat['assistant'][:100]}...")
        
        user_q = st.text_input("Ask anything:", key="sidebar_chat")
        if st.button("Send", key="send_sidebar"):
            if user_q:
                with st.spinner("Thinking..."):
                    success, resp = chat_with_grok(user_q, [])
                    if success:
                        st.session_state.chat_history.append({'user': user_q, 'assistant': resp})
                        st.rerun()
    
    st.markdown("---")
    st.session_state.voice_enabled = st.checkbox("🔊 Voice", value=st.session_state.voice_enabled)
    
    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True):
        update_user_data(st.session_state.username, st.session_state.user_data)
        st.session_state.authenticated = False
        st.rerun()

# Floating Guide
st.markdown("""
<style>
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
}

.floating-guide {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 70px;
    height: 70px;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 35px;
    cursor: pointer;
    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
    z-index: 9999;
    animation: float 3s ease-in-out infinite;
}

.floating-guide:hover {
    transform: scale(1.1);
}
</style>
<div class="floating-guide" title="AI Learning Assistant - Click avatar to chat in sidebar">
    👩‍🏫
</div>
""", unsafe_allow_html=True)

# Main content
if selected == "Home":
    from pages import home
    home.show()
elif selected == "Courses":
    from pages import courses
    courses.show()
elif selected == "My Progress":
    from pages import progress
    progress.show()
elif selected == "Certificates":
    from pages import certificates
    certificates.show()
elif selected == "Analytics":
    from pages import analytics
    analytics.show()
elif selected == "Admin":
    from pages import admin
    admin.show()
