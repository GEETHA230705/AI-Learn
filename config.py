import os
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.getenv('GROK_API_KEY', 'sk_ebf6231e722649bb5788e719c183414f62222040e8c4204c')
ADMIN_PASSWORD = "admin123"
