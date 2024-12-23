import requests
import json
import os

# Ensure your API key is set in the environment variables
api_key = os.getenv("GROQ_API_KEY")  # If using an environment variable
# If not using an environment variable, you can hardcode the key here like this:
# api_key = "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"

# Check if the API key is found
if not api_key:
    raise ValueError("API key is missing")

# Headers for the request
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Define the URL for the Groq API endpoint
url = "https://api.groq.com/openai/v1/chat/completions"

# Define the payload with the correct Llama model and initial chat message
payload = {
    "model": "llama3-8b-8192",  # Ensure this matches the exact model name you're using
    "messages": [{"role": "user", "content": "Hello, how can I assist with sales?"}]
}

# Send the request to the API
response = requests.post(url, headers=headers, json=payload)

# Check if the response is successful
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)
