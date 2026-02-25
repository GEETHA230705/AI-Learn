import json
import hashlib
from datetime import datetime

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create demo user
users = {
    "demo": {
        "email": "demo@ailearn.com",
        "password": hash_password("demo123"),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "xp": 0,
        "completed_lessons": [],
        "badges": [],
        "streak": 0,
        "quiz_scores": [],
        "time_spent": {},
        "last_login": datetime.now().strftime("%Y-%m-%d")
    }
}

with open("users_data.json", "w") as f:
    json.dump(users, f, indent=2)

print("Demo user created!")
print("Username: demo")
print("Password: demo123")
