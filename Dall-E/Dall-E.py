import requests
import json
import webbrowser

# API endpoint for DALL-E
endpoint = "https://api.openai.com/v1/images/generations"

# Your API key
api_key = "OPENAI_API_KEY"

while True:
# The prompt for DALL-E
    prompt = input("Enter a prompt: ")

# Define the request headers
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Define the request data
    data = {
    "model": "dall-e-3",
    "prompt": prompt,
    "num_images":1,
    "size":"1024x1024",
    "response_format":"url"
}

# Send the request to the API
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

# Check if the request was successful
    if response.status_code == 200:
    # Extract the URL of the generated image
        image_url = response.json()['data'][0]['url']
        webbrowser.open(image_url)
    else:
    # Print the error message
        print(f"Error generating image: {response.json()}")

