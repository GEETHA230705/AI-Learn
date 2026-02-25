# 🎭 Talking Avatar Setup Guide

## Options for Realistic Talking Avatars

### Option 1: D-ID API (Recommended) ⭐

**What it does:** Creates realistic talking avatar videos with perfect lip-sync

**Pricing:**
- Free Trial: 20 credits (20 videos)
- Lite: $5.90/month (15 minutes)
- Pro: $49/month (90 minutes)

**Setup Steps:**

1. **Get API Key:**
   - Go to https://studio.d-id.com/
   - Sign up for free account
   - Go to Settings → API Keys
   - Create new API key
   - Copy the key

2. **Add to Project:**
   ```python
   # In utils/talking_avatar.py, replace:
   DID_API_KEY = "your_did_api_key_here"
   # With your actual key:
   DID_API_KEY = "your_actual_key_here"
   ```

3. **Use in App:**
   ```python
   from utils.talking_avatar import show_talking_avatar_widget
   
   show_talking_avatar_widget("Hello! I'm Sophia, your AI learning assistant.")
   ```

**Features:**
- ✅ Realistic lip-sync
- ✅ Multiple avatar options
- ✅ Natural voice
- ✅ Fast generation (10-30 seconds)
- ✅ HD quality

---

### Option 2: HeyGen API

**What it does:** Professional AI avatar videos

**Pricing:**
- Creator: $24/month (3 minutes)
- Business: $72/month (15 minutes)
- Enterprise: Custom pricing

**Setup Steps:**

1. **Get API Key:**
   - Go to https://heygen.com/
   - Sign up
   - Go to API section
   - Get API key

2. **Add to Project:**
   ```python
   # In utils/talking_avatar.py:
   HEYGEN_API_KEY = "your_heygen_key_here"
   ```

3. **Use:**
   ```python
   from utils.talking_avatar import create_heygen_avatar
   
   success, video_url = create_heygen_avatar("Your message here")
   if success:
       st.video(video_url)
   ```

---

### Option 3: Simple Animated Avatar (Free) 💰

**What it does:** CSS-animated avatar with speech bubble

**Setup:** Already included! No API needed.

**Use:**
```python
from utils.talking_avatar import show_simple_talking_avatar

show_simple_talking_avatar("Hello! I'm here to help you learn.")
```

**Features:**
- ✅ Free
- ✅ No API required
- ✅ Instant (no generation time)
- ✅ Animated talking effect
- ✅ Sound wave visualization
- ⚠️ Not realistic (emoji-based)

---

### Option 4: Synthesia API

**What it does:** Enterprise-grade AI avatars

**Pricing:**
- Personal: $30/month (10 minutes)
- Enterprise: Custom

**Setup:**
- Contact Synthesia for API access
- Enterprise only

---

### Option 5: ElevenLabs + Ready Player Me

**What it does:** Combine voice AI with 3D avatar

**Components:**
1. **ElevenLabs** - Realistic voice ($5-$99/month)
2. **Ready Player Me** - 3D avatar (Free)
3. **Custom Integration** - Requires development

**Complexity:** High (requires React/Three.js)

---

## 🚀 Quick Start (Recommended Path)

### Step 1: Start with Simple Avatar (Free)

Update your `app.py`:

```python
# At the bottom of each page, add:
from utils.talking_avatar import show_simple_talking_avatar

st.markdown("---")
show_simple_talking_avatar("Welcome! I'm Sophia, your AI learning assistant. How can I help you today?")
```

### Step 2: Upgrade to D-ID (When Ready)

1. Get D-ID API key (free trial)
2. Update `utils/talking_avatar.py` with your key
3. Replace `show_simple_talking_avatar` with `show_talking_avatar_widget`

```python
from utils.talking_avatar import show_talking_avatar_widget

show_talking_avatar_widget("Your message here")
```

---

## 💡 Integration Examples

### Example 1: Avatar on Home Page

```python
# In pages/home.py

from utils.talking_avatar import show_simple_talking_avatar

def show():
    st.markdown("...")  # Your existing code
    
    # Add avatar at bottom
    st.markdown("---")
    st.markdown("### 👩‍🏫 Meet Sophia")
    
    show_simple_talking_avatar(
        "Welcome to AI Learn! I'm Sophia, your personal learning assistant. "
        "I'm here to guide you through your courses and answer any questions you have!"
    )
```

### Example 2: Avatar in Chatbot

```python
# In app.py, in the chat section:

if st.session_state.show_chat:
    # Show avatar
    from utils.talking_avatar import show_simple_talking_avatar
    
    if st.session_state.chat_history:
        last_response = st.session_state.chat_history[-1]['assistant']
        show_simple_talking_avatar(last_response)
```

### Example 3: Avatar on Every Page

```python
# In app.py, after page routing:

from utils.talking_avatar import show_simple_talking_avatar

# Show avatar with page-specific message
page_messages = {
    "Home": "Welcome! Ready to start learning?",
    "Courses": "Choose a course and let's begin your journey!",
    "My Progress": "Great job on your progress! Keep it up!",
    "Certificates": "Earn certificates by completing courses!",
    "Analytics": "Let's analyze your learning patterns!",
    "Admin": "Manage your platform here."
}

st.markdown("---")
show_simple_talking_avatar(page_messages.get(selected, "How can I help you?"))
```

---

## 📊 Comparison Table

| Feature | Simple Avatar | D-ID | HeyGen | Synthesia |
|---------|--------------|------|---------|-----------|
| Cost | Free | $5.90/mo | $24/mo | $30/mo |
| Realism | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Speed | Instant | 10-30s | 30-60s | 30-60s |
| Setup | Easy | Easy | Medium | Hard |
| Lip-Sync | No | Yes | Yes | Yes |
| API Required | No | Yes | Yes | Yes |
| Best For | MVP/Demo | Production | Business | Enterprise |

---

## 🎯 Recommendation

### For Your Project:

1. **Start Now:** Use Simple Avatar (free, works immediately)
2. **For Demo:** Simple Avatar is impressive enough
3. **For Production:** Upgrade to D-ID ($5.90/month)
4. **For Enterprise:** Consider HeyGen or Synthesia

### Why Simple Avatar is Good Enough:

- ✅ Works immediately (no API setup)
- ✅ No costs
- ✅ Animated and engaging
- ✅ Professional appearance
- ✅ Perfect for demos/hackathons
- ✅ Can upgrade later

---

## 🔧 Troubleshooting

### D-ID API Issues:

**Error: "Invalid API key"**
- Check key is correct
- Ensure no extra spaces
- Verify account is active

**Error: "Insufficient credits"**
- Check your D-ID dashboard
- Upgrade plan or add credits

**Video takes too long:**
- Normal: 10-30 seconds
- If >60 seconds, check API status

### Simple Avatar Not Showing:

**Check:**
- `unsafe_allow_html=True` is set
- No ad blockers interfering
- Browser supports CSS animations

---

## 📝 Next Steps

1. **Try Simple Avatar First:**
   ```bash
   # Already integrated! Just run:
   python -m streamlit run app.py
   ```

2. **Test with D-ID (Optional):**
   - Get free trial key
   - Update `talking_avatar.py`
   - Test with one message

3. **Deploy:**
   - Simple avatar works everywhere
   - D-ID requires API key in production

---

## 🎓 Conclusion

You have **3 working options**:

1. **Simple Avatar** (Free) - Ready now! ✅
2. **D-ID API** ($5.90/mo) - Realistic lip-sync
3. **HeyGen API** ($24/mo) - Professional quality

**Start with Simple Avatar** - it's impressive and works perfectly for your use case!

---

**Questions?** Check the code in `utils/talking_avatar.py` for examples.
