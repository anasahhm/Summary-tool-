import requests

# Define your API key and endpoint URL
OLLAMA_API_KEY = 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFu66/lnUQY6fZmIRiyvY5AzXV1MUpgbN45/4sCSp7Ke anas@DESKTOP-LSN9GAS'
OLLAMA_API_URL = 'https://api.ollama.com/v1/qwen2/summarize'

def get_summary(text):
    headers = {
        'Authorization': f'Bearer {OLLAMA_API_KEY}',  # Use Bearer token for API key authorization
        'Content-Type': 'application/json'
    }

    data = {
        'text': text
    }

    response = requests.post(OLLAMA_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()  # Return the summary from the response
    else:
        return {'error': response.text}

if __name__ == "__main__":
    sample_text = "Your text to summarize here"
    result = get_summary(sample_text)
    print(result)
