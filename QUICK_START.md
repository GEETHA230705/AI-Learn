# 🚀 Quick Start Guide - AI Learn Platform

## ✅ Setup Complete!

All API keys are configured and ready to use:
- ✅ D-ID Expressive Avatar API
- ✅ Grok AI Chatbot API

## Start the App (3 Steps)

### Step 1: Run the App
```bash
python -m streamlit run app.py
```

### Step 2: Login
Use demo account:
- **Username:** `demo`
- **Password:** `demo123`

Or admin account:
- **Username:** `admin`
- **Password:** `admin123`

### Step 3: Enable AI Teacher
In the sidebar, check:
- ✅ 👩‍🏫 AI Teacher Guide
- ✅ 🔊 Voice (optional)

## What You'll See

### 1. AI Teacher Guide (Sidebar)
- **Sophia** - Your realistic AI teacher
- Appears in left sidebar
- Different emotions for each page:
  - 😊 Friendly on Home
  - 👔 Professional on Courses
  - 🎉 Excited on Progress
  - 💪 Confident on Certificates
- **First time:** Takes 1-5 minutes to generate video
- **After that:** Instant (cached)

### 2. AI Chatbot (Bottom)
- Scroll to bottom of any page
- Click "💬 Chat with AI Assistant"
- Ask questions like:
  - "What is Python?"
  - "Explain loops"
  - "How do I earn badges?"
- Get instant AI responses

## Features to Try

### 1. Browse Courses
- Click "Courses" in sidebar
- Select a course (Python, Java, Web Dev, Data Science)
- See the course roadmap
- Start learning!

### 2. Earn XP & Badges
- Complete lessons → +10 XP
- Complete quizzes → +20 XP
- 7-day streak → +50 XP
- Unlock badges: 🥉 🥈 🥇 🔥

### 3. Track Progress
- Click "My Progress"
- See XP growth chart
- View completed lessons
- Check your badges

### 4. Get Certificates
- Complete all modules in a course
- Click "Certificates"
- Download PDF certificate with QR code
- Share on social media!

### 5. View Analytics
- Click "Analytics"
- See learning patterns
- XP growth over time
- Quiz accuracy trends
- Time spent per course

### 6. Admin Panel
- Click "Admin" (password: `admin123`)
- Add new courses
- Create modules
- View student progress
- Export reports

## AI Teacher Guide Messages

### Home Page
"Welcome to AI Learn Platform! I'm Sophia, your personal AI teacher. On this page, you can see your learning statistics..."

### Courses Page
"Welcome to the Courses page! Here you can choose from our available courses. Select a course from the dropdown menu..."

### My Progress Page
"Great job checking your progress! On this page, you can track your learning achievements..."

### Certificates Page
"Welcome to the Certificates page! Here you can view and download your earned certificates..."

### Analytics Page
"Welcome to your Analytics dashboard! This page provides deep insights into your learning patterns..."

### Admin Page
"Welcome to the Admin Panel! This is where you manage the entire platform..."

## Tips

### Save D-ID Credits
- Videos are cached automatically
- Same message = no new credit used
- 20 free credits = 20 unique videos
- Plan your messages wisely!

### Best Learning Path
1. Start with Python course
2. Complete modules in order
3. Take quizzes to test knowledge
4. Earn badges and XP
5. Get certificate
6. Move to next course

### Voice Feature
- Enable "🔊 Voice" in sidebar
- Sophia speaks page descriptions
- British female voice (gTTS)
- Works with or without D-ID

## Troubleshooting

### "Loading AI teacher..." takes long
- **Normal!** First video takes 1-5 minutes
- D-ID is generating realistic video
- Be patient, it's worth it!
- Subsequent loads are instant (cached)

### Chatbot not responding
- Check internet connection
- Verify Grok API key in `config.py`
- Try asking a different question

### Video not playing
- Check D-ID credits: https://studio.d-id.com/
- Verify API key in `utils/did_expressive.py`
- Try refreshing the page

## What Makes This Special

### 🎭 Realistic AI Teacher
- Not just text or emoji
- Real human-like avatar
- Perfect lip-sync
- Emotional expressions
- Natural voice

### 🤖 Smart AI Chatbot
- Powered by Grok AI
- Contextual responses
- Learns from conversation
- Helpful fallbacks

### 🎮 Gamification
- XP system
- Badges
- Streaks
- Leaderboards (coming soon)

### 📊 Analytics
- Track your progress
- Identify strengths
- Find areas to improve
- Data-driven learning

### 🎓 Professional Certificates
- PDF with unique ID
- QR code verification
- Shareable on social media
- Looks professional

## Demo Flow

1. **Login** → See welcome screen
2. **Home** → View stats, featured courses
3. **Enable AI Guide** → Meet Sophia (wait 1-5 min)
4. **Courses** → Select Python course
5. **Start Module** → Learn Variables
6. **Complete Quiz** → Earn +20 XP
7. **Progress** → See XP growth
8. **Chat** → Ask "What is Python?"
9. **Complete Course** → Get certificate!

## Ready to Start?

```bash
python -m streamlit run app.py
```

Then login with `demo` / `demo123` and explore!

---

**Need Help?**
- Check `API_KEYS_CONFIGURED.md` for setup details
- Read `DID_SETUP_INSTRUCTIONS.md` for D-ID info
- See `FEATURES_SUMMARY.md` for all features

**Enjoy learning with Sophia! 🎓✨**
