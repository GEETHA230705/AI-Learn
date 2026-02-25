# 🎓 AI Learn - Smart Structured Learning Platform

A professional, gamified learning platform built with Streamlit featuring **realistic AI teacher with lip-sync**, structured courses, XP system, badges, certificates, and comprehensive analytics.

## 🌟 Highlight Features

### 🎭 Realistic AI Teacher (D-ID Expressive Avatar)
- **Sophia** - Your personal AI teacher with perfect lip-sync
- Realistic human avatar with emotional expressions
- Different emotions for different pages (friendly, professional, excited, confident)
- Natural voice matching emotions
- HD quality video with facial animations
- Appears in sidebar on every page
- Context-aware guidance and tips

### 🤖 AI Chatbot (Grok Integration)
- Smart conversational AI assistant
- Contextual responses about courses and programming
- Powered by Grok AI
- Available on every page
- Chat history tracking

## ✨ Key Features

### 1. 🧑‍🏫 AI Teacher Guide (D-ID Integration)
- Realistic talking avatar with lip-sync
- Emotional expressions (professional, friendly, excited, etc.)
- Context-aware tips and navigation help
- Voice toggle option
- Page-specific guidance messages
- Video caching to save credits

### 2. 📚 Structured Course System
- Dropdown course selection
- Multiple courses: Python, Java, Web Development, Data Science
- Module-based learning path
- Lock/unlock progression system

### 3. 🗺️ Interactive Course Roadmap
- Visual progress tracking
- Lock 🔒 system for sequential learning
- Progress bar with completion percentage
- Module status indicators (✅ completed, 🔒 locked, ▶️ available)

### 4. 🏆 Professional Certificate System
- Auto-generated certificates upon course completion
- PDF download with QR code
- Unique certificate ID
- Professional design with borders and signatures

### 5. 🎮 Gamification System
- XP points for completing lessons (+10 XP per lesson)
- Badge system:
  - 🥉 Beginner (50 XP)
  - 🥈 Intermediate (150 XP)
  - 🥇 Expert (300 XP)
  - 🔥 Consistency King (7-day streak)
  - 🎯 Quiz Master (10 quizzes)
- Streak tracking
- Confetti animations on achievements

### 6. 📊 Learning Analytics
- XP growth chart over time
- Course completion percentage
- Time spent by course (pie chart)
- Quiz accuracy tracking
- Personalized insights and recommendations
- Export learning reports

### 7. 🎨 SaaS-Level UI
- Gradient headers
- Card-based layout
- Smooth animations and transitions
- Hover effects
- Professional color scheme
- Responsive design
- Dark mode toggle (optional)

### 8. 🎉 Course Completion Animations
- Confetti celebration
- XP burst animation
- Badge unlock popups
- Guide congratulations

### 9. 🔐 Admin Panel
- Password-protected access (default: admin123)
- Add/Edit/Delete courses
- Add modules and content
- View student progress
- Platform analytics
- Export reports
- Data management
- Settings customization

## 🚀 Quick Start

### ✅ APIs Already Configured!
- D-ID Expressive Avatar API ✅
- Grok AI Chatbot API ✅

### Run the App (One Command)
```bash
python -m streamlit run app.py
```

### Login
**Demo Account:**
- Username: `demo`
- Password: `demo123`

**Admin Account:**
- Username: `admin`
- Password: `admin123`

### Enable AI Teacher
In the sidebar:
1. Check ✅ "👩‍🏫 AI Teacher Guide"
2. Check ✅ "🔊 Voice" (optional)
3. Wait 1-5 minutes for first video (then instant!)

**That's it!** Start learning with Sophia! 🎓

## 📖 Detailed Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

Or use the provided batch file (Windows):
```bash
install.bat
```

### 2. API Keys (Already Configured)
Both API keys are already set up in the project:
- **D-ID API:** `utils/did_expressive.py` (line 11)
- **Grok API:** `config.py` and `.env`

### 3. Run the Application
```bash
python -m streamlit run app.py
```

Or use the batch file (Windows):
```bash
run.bat
```

### 4. First Time Setup
- First D-ID video takes 1-5 minutes to generate
- After that, videos are cached (instant replay)
- Free trial: 20 video credits
- Each unique message = 1 credit

## 📁 Project Structure

```
ai-learn-platform/
├── app.py                      # Main application file
├── config.py                   # Configuration and API keys
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
├── install.bat                 # Windows installation script
├── run.bat                     # Windows run script
├── QUICK_START.md             # Quick start guide
├── API_KEYS_CONFIGURED.md     # API setup status
├── DID_SETUP_INSTRUCTIONS.md  # D-ID detailed setup
├── pages/
│   ├── __init__.py
│   ├── home.py                # Home page with stats
│   ├── courses.py             # Course selection and roadmap
│   ├── progress.py            # Progress tracking and badges
│   ├── certificates.py        # Certificate generation
│   ├── analytics.py           # Learning analytics
│   └── admin.py               # Admin panel
├── utils/
│   ├── __init__.py
│   ├── auth.py                # Authentication system
│   ├── chatbot.py             # Grok AI chatbot
│   ├── ai_guide.py            # AI teacher guide integration
│   ├── did_expressive.py      # D-ID Expressive Avatar API
│   ├── voice.py               # Voice-over (gTTS)
│   └── course_content.py      # Course content management
└── README.md
```

## 🎯 Usage

### For Students:
1. Navigate to **Courses** page
2. Select a course from the dropdown
3. Follow the roadmap and complete modules sequentially
4. Earn XP and badges
5. Track progress in **My Progress** page
6. View analytics in **Analytics** page
7. Download certificates upon course completion

### For Admins:
1. Go to **Admin** page
2. Login with password (default: admin123)
3. Add new courses and modules
4. View student progress
5. Export analytics reports
6. Manage platform settings

## 🎨 Customization

### Adding New Courses:
Use the Admin Panel or modify `app.py`:
```python
st.session_state.courses['New Course'] = {
    'modules': ['Module 1', 'Module 2', 'Module 3'],
    'icon': '📖',
    'description': 'Course description here'
}
```

### Changing Colors:
Modify the CSS in `app.py` `load_css()` function to change the color scheme.

### Adding Content:
Edit `pages/courses.py` `show_lesson()` function to add:
- Video tutorials
- Text content
- Code examples
- Interactive exercises

## 🔧 Configuration

### Admin Password:
Change in `config.py`:
```python
ADMIN_PASSWORD = "your_secure_password"
```

### Grok API Integration:
The platform is ready for AI-powered features using the Grok API. Add your implementation in the relevant pages.

## 📊 Features for Judges

This platform demonstrates:
- ✅ **AI Integration** - Realistic talking avatar with D-ID Expressive API
- ✅ **Conversational AI** - Grok-powered chatbot
- ✅ **Emotional Intelligence** - Avatar emotions match page context
- ✅ **Professional UI/UX** - SaaS-level design with animations
- ✅ **Gamification** - XP, badges, streaks, achievements
- ✅ **Data Visualization** - Interactive charts and analytics
- ✅ **Certificate System** - PDF generation with QR codes
- ✅ **Admin Panel** - Complete platform management
- ✅ **Structured Learning** - Sequential module progression
- ✅ **Progress Tracking** - Comprehensive analytics dashboard
- ✅ **Responsive Design** - Works on all devices
- ✅ **Scalable Architecture** - Modular and extensible
- ✅ **Export Functionality** - Reports and certificates
- ✅ **Voice Integration** - Text-to-speech support
- ✅ **Video Caching** - Optimized performance

## 🎓 Technologies Used

### Core Framework
- **Streamlit** - Web framework
- **Python 3.8+** - Programming language

### AI & APIs
- **D-ID Expressive Avatar API** - Realistic talking avatars with lip-sync
- **Grok AI API** - Conversational AI chatbot
- **gTTS** - Text-to-speech voice-over

### Data & Visualization
- **Plotly** - Interactive charts and graphs
- **Pandas** - Data manipulation and analytics

### Document Generation
- **ReportLab** - PDF certificate generation
- **QRCode** - QR code generation for certificates

### UI Components
- **streamlit-option-menu** - Professional navigation menu

### Configuration
- **Python-dotenv** - Environment variable management

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## 📧 Support

For questions or support, please open an issue in the repository.

---

Made with ❤️ for smart, structured learning
