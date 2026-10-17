import openai
import requests
import os  # To load environment variables

# Load your API key from an environment variable
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("API key is missing. Please set it as an environment variable.")

# Define the API endpoint and your request payload
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Print the joke (response content)
    print(response.json()['choices'][0]['message']['content'])

    # Access rate limit headers
    print("Request Limit:", response.headers.get('x-ratelimit-limit-requests'))
    print("Remaining Requests:", response.headers.get('x-ratelimit-remaining-requests'))
    print("Reset Time (Requests):", response.headers.get('x-ratelimit-reset-requests'))

    print("Token Limit:", response.headers.get('x-ratelimit-limit-tokens'))
    print("Remaining Tokens:", response.headers.get('x-ratelimit-remaining-tokens'))
    print("Reset Time (Tokens):", response.headers.get('x-ratelimit-reset-tokens'))
else:
    # Print error details if the request failed
    print(f"Error {response.status_code}: {response.text}")