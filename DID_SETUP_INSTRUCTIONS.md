# 🎭 D-ID Realistic Talking Avatar - Setup Instructions

## What You'll Get

A **realistic human avatar** that:
- ✅ Speaks with perfect lip-sync
- ✅ Natural facial expressions
- ✅ HD video quality
- ✅ Professional female voice
- ✅ Looks like a real person talking

## Step-by-Step Setup (5 minutes)

### Step 1: Get Free D-ID API Key

1. **Visit D-ID Studio**
   - Go to: https://studio.d-id.com/
   - Click "Sign Up" (top right)

2. **Create Account**
   - Use your email
   - Verify email
   - Login to dashboard

3. **Get API Key**
   - Click your profile (top right)
   - Go to "Settings"
   - Click "API Keys" tab
   - Click "Create API Key"
   - **Copy the key** (you'll need it next)

4. **Free Trial**
   - You get **20 free credits**
   - Each video = 1 credit
   - Perfect for testing!

### Step 2: Add Key to Your Project

1. **Open the file:**
   ```
   utils/did_avatar.py
   ```

2. **Find this line (line 7):**
   ```python
   DID_API_KEY = "your_did_api_key_here"
   ```

3. **Replace with your actual key:**
   ```python
   DID_API_KEY = "abcd1234your_actual_key_here"
   ```

4. **Save the file**

### Step 3: Restart the App

```bash
python -m streamlit run app.py
```

### Step 4: Test It!

1. Login to the app
2. Scroll down to "Meet Sophia"
3. Select **"D-ID (Realistic)"** mode
4. Click "Chat with Sophia"
5. Ask a question
6. Wait 10-30 seconds
7. **Watch the realistic talking avatar!** 🎉

## How It Works

1. **You ask a question** → Sophia responds with text
2. **D-ID API** → Creates a video of avatar speaking the text
3. **10-30 seconds** → Video is generated
4. **Video plays** → Realistic avatar with perfect lip-sync!

## Example Usage

```python
from utils.did_avatar import show_did_avatar

# Show realistic talking avatar
show_did_avatar("Hello! I'm Sophia, your AI learning assistant.")
```

## Pricing

| Plan | Price | Credits | Minutes |
|------|-------|---------|---------|
| **Free Trial** | $0 | 20 | ~2 min |
| **Lite** | $5.90/mo | - | 15 min |
| **Pro** | $49/mo | - | 90 min |
| **Enterprise** | Custom | - | Custom |

**Recommendation:** Start with free trial (20 videos)

## Features Comparison

| Feature | Simple Avatar | D-ID Avatar |
|---------|--------------|-------------|
| Cost | Free | $5.90/mo |
| Setup | None | 5 minutes |
| Realism | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Lip-Sync | No | Perfect |
| Speed | Instant | 10-30s |
| Quality | Emoji | HD Video |
| Voice | TTS | Natural |

## Troubleshooting

### "API key not configured"
- Check you added the key to `utils/did_avatar.py`
- Make sure no extra spaces
- Restart the app

### "Failed to create video"
- Check your internet connection
- Verify API key is correct
- Check you have credits left

### "Timeout"
- D-ID servers might be busy
- Try again in a few minutes
- Check D-ID status page

### "Insufficient credits"
- Go to https://studio.d-id.com/
- Check your credit balance
- Upgrade plan or add credits

## Advanced Options

### Change Avatar Image

In `utils/did_avatar.py`, change:
```python
DEFAULT_AVATAR = "your_avatar_image_url_here"
```

You can use:
- D-ID's default avatars
- Your own uploaded image
- Any public image URL

### Change Voice

In `utils/did_avatar.py`, change:
```python
"voice_id": "en-US-JennyNeural"  # Female
```

Options:
- `en-US-JennyNeural` - Female (default)
- `en-US-GuyNeural` - Male
- `en-GB-SoniaNeural` - British Female
- `en-AU-NatashaNeural` - Australian Female

### Cache Videos

Videos are automatically cached to save credits:
```python
show_did_avatar(message, use_cache=True)  # Default
```

## Testing Your Setup

Run this test:

```python
from utils.did_avatar import test_did_connection

success, message = test_did_connection()
print(message)
```

## Support

- **D-ID Docs:** https://docs.d-id.com/
- **D-ID Support:** support@d-id.com
- **Status Page:** https://status.d-id.com/

## What's Next?

Once D-ID is working:

1. **Test with different messages**
2. **Try different avatars**
3. **Experiment with voices**
4. **Show it to your users!**

## Alternative: HeyGen

If you prefer HeyGen instead:

1. Get API key from https://heygen.com/
2. Use `utils/talking_avatar.py` HeyGen functions
3. Similar setup process

## Conclusion

With D-ID, you get:
- ✅ Professional realistic avatar
- ✅ Perfect lip-sync
- ✅ Natural voice
- ✅ HD quality
- ✅ Easy integration

**Total setup time: 5 minutes**
**Free trial: 20 videos**

Ready to make Sophia come alive? Follow the steps above! 🚀

---

**Need help?** Check the code comments in `utils/did_avatar.py`
