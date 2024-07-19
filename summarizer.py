import requests

# Define your API key and endpoint URL
OLLAMA_API_KEY = 'generate your own pulic ollama key and add that key to your ollama keys for the end point'
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
