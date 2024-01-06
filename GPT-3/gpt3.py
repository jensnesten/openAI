import json
import time
import requests

api_key = "OPENAI_API_KEY"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}


def generate_text(prompt):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))
    response_json = response.json()
    message = response_json['choices'][0]['message']['content']
    return message



while True:
    user_input = input("\n Enter a prompt: ")
    print("\n")
    response = generate_text(user_input)
    for char in response:
        print(char, end="", flush=True)
        time.sleep(0.01)
    print("")
