# 🎓 AI Learn Platform - Complete Setup Guide

## ✨ Features Included

### 1. **Login/Register System** ✅
- User authentication
- Password hashing
- Data persistence
- Demo account: `demo` / `demo123`

### 2. **Professional Blue Theme** ✅
- Modern gradient design
- Smooth animations
- Card-based layout
- Responsive UI

### 3. **Complete Course System** ✅
- Python (7 modules with full content)
- Java, Web Dev, Data Science
- Video tutorials
- Code examples
- Interactive quizzes
- Progress tracking

### 4. **Gamification** ✅
- XP system (+10 XP per lesson)
- Badge system (🥉🥈🥇)
- Streak tracking
- Progress bars

### 5. **Certificates** ✅
- Auto-generated PDFs
- QR codes
- Unique IDs
- Download feature

### 6. **Analytics** ✅
- XP growth charts
- Course completion stats
- Time tracking
- Learning insights

### 7. **Admin Panel** ✅
- Add/edit courses
- View students
- Analytics dashboard
- Data export

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
pip install streamlit streamlit-option-menu plotly pandas python-dotenv reportlab qrcode[pil] Pillow requests gtts
```

### Step 2: Create Demo User
```bash
python create_demo_user.py
```

### Step 3: Run the App
```bash
python -m streamlit run app.py
```

### Step 4: Login
- Username: `demo`
- Password: `demo123`

## 🤖 AI Chatbot Setup

The chatbot requires a Grok API key. You have two options:

### Option A: Use Grok API (Recommended)
1. Your API key is already in `.env` and `config.py`
2. The chatbot will use real AI responses

### Option B: Use Fallback Mode (No API needed)
The chatbot has built-in fallback responses and will work without the API.

## 🔊 Voice Feature

The voice feature uses Google Text-to-Speech (gTTS):
- Toggle "🔊 Voice Guide" in sidebar
- Female voice (British English)
- Speaks page descriptions
- Speaks AI responses

## 📁 Project Structure

```
AI learn/
├── app.py                 # Main application
├── config.py             # Configuration
├── .env                  # Environment variables
├── create_demo_user.py   # Demo user creator
├── requirements.txt      # Dependencies
├── users_data.json       # User database
├── pages/
│   ├── home.py          # Home page
│   ├── courses.py       # Course system
│   ├── progress.py      # Progress tracking
│   ├── certificates.py  # Certificate generation
│   ├── analytics.py     # Analytics dashboard
│   └── admin.py         # Admin panel
└── utils/
    ├── auth.py          # Authentication
    ├── chatbot.py       # AI chatbot
    ├── voice.py         # Voice synthesis
    ├── avatar.py        # AI avatar (optional)
    └── course_content.py # Course database
```

## 🎯 How to Use

### For Students:
1. **Login** - Use demo account or register
2. **Select Course** - Go to Courses page
3. **Learn** - Complete modules sequentially
4. **Earn XP** - Get 10 XP per completed lesson
5. **Unlock Badges** - Earn badges at 50, 150, 300 XP
6. **Get Certificate** - Complete all modules
7. **Chat with AI** - Scroll down on any page
8. **Track Progress** - View My Progress page

### For Admins:
1. Go to Admin page
2. Login with password: `admin123`
3. Add/edit courses
4. View student progress
5. Export analytics

## 🎨 Customization

### Change Colors:
Edit the CSS in `app.py` - search for `#1976d2` (blue) and replace with your color.

### Add Courses:
Use the Admin panel or edit `app.py` session state initialization.

### Modify Content:
Edit `utils/course_content.py` to add more lessons.

## ⚠️ Known Limitations

### Streamlit Limitations:
1. **No Real-time Avatar Animation**: Streamlit doesn't support real-time WebSocket animations like a talking avatar with lip-sync. This requires a full web framework (React, Vue, etc.)

2. **Chatbot Position**: Streamlit doesn't support fixed-position floating elements that persist across page changes. The chatbot appears at the bottom of each page.

3. **Voice Playback**: Voice plays once per page load. For continuous conversation, you'd need a WebRTC solution.

## 🔧 Troubleshooting

### Chatbot Not Responding:
- Check your internet connection
- Verify API key in `.env`
- The fallback mode will still work

### Voice Not Playing:
- Check browser audio permissions
- Try a different browser (Chrome recommended)
- Toggle voice off and on again

### Login Issues:
- Run `python create_demo_user.py` again
- Check `users_data.json` exists

### Module Not Found:
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version (3.8+ required)

## 🚀 Advanced Features (Future)

To add a real animated talking avatar with lip-sync, you would need:

1. **Frontend Framework**: React/Vue with Three.js or Ready Player Me
2. **WebSocket Server**: For real-time communication
3. **Speech Synthesis**: Web Speech API or ElevenLabs
4. **Lip Sync Library**: Oculus LipSync or Rhubarb Lip Sync
5. **3D Avatar**: Ready Player Me, VRoid, or custom model

This would require a complete rewrite outside of Streamlit.

## 📝 What Works Now

✅ Complete learning platform
✅ User authentication
✅ Course system with content
✅ XP and badges
✅ Certificates with QR codes
✅ Analytics dashboard
✅ Admin panel
✅ AI chatbot (text-based)
✅ Voice synthesis
✅ Professional UI

## 🎓 Conclusion

This is a fully functional learning platform with all core features. The only limitation is the animated talking avatar, which requires technologies beyond Streamlit's capabilities.

For a demo/prototype/MVP, this platform is production-ready!

---

**Need Help?** Check the code comments or create an issue.
