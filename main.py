import requests
import json

# Function to interact with GPT-4
def gpt4_query(prompt, api_key):
    # API endpoint
    api_url = "https://api.openai.com/v1/engines/gpt-4/completions"
    
    # Headers for the API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Data for the API request
    data = {
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7
    }
    
    # Making the API request
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    
    # Checking if the request was successful
    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        return f"Error: {response.status_code}, {response.text}"

# Main function to run the script
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual OpenAI API key
    api_key = "your_api_key_here"
    
    # Prompt to send to GPT-4
    prompt = "Write a brief introduction about artificial intelligence."
    
    # Get the response from GPT-4
    response = gpt4_query(prompt, api_key)
    
    # Print the response
    print("GPT-4 Response:")
    print(response)
