"""
Test D-ID API to see what's working
"""
import requests

DID_API_KEY = "aGFyc2hhYW1tdTEyMDlAZ21haWwuY29t:XgWvvxW-l7tYxCMbIhWKa"
DID_API_URL = "https://api.d-id.com"

headers = {
    "Authorization": f"Basic {DID_API_KEY}",
    "Content-Type": "application/json"
}

# Test 1: Check API connection
print("=" * 50)
print("TEST 1: Checking API connection...")
print("=" * 50)

try:
    response = requests.get(
        f"{DID_API_URL}/talks",
        headers=headers,
        timeout=10
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}")
except Exception as e:
    print(f"Error: {e}")

# Test 2: Try creating a simple talk without source_url
print("\n" + "=" * 50)
print("TEST 2: Creating talk without image...")
print("=" * 50)

payload = {
    "script": {
        "type": "text",
        "input": "Hello! I'm Sophia, your AI teacher.",
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural"
        }
    }
}

try:
    response = requests.post(
        f"{DID_API_URL}/talks",
        headers=headers,
        json=payload,
        timeout=10
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")

# Test 3: Try with a simple image URL
print("\n" + "=" * 50)
print("TEST 3: Creating talk with image...")
print("=" * 50)

payload_with_image = {
    "source_url": "https://clips-presenters.d-id.com/amy/image.png",
    "script": {
        "type": "text",
        "input": "Hello! I'm Sophia, your AI teacher.",
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural"
        }
    }
}

try:
    response = requests.post(
        f"{DID_API_URL}/talks",
        headers=headers,
        json=payload_with_image,
        timeout=10
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 201:
        print("\n✅ SUCCESS! Video is being created.")
        talk_id = response.json().get("id")
        print(f"Talk ID: {talk_id}")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 50)
print("Tests complete!")
print("=" * 50)
