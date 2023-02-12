import openai
import time

openai.api_key = "INSERT OPENAI API-KEY"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

while True:
    user_input = input("Enter a prompt: ")
    response = generate_text(user_input)
    for char in response:
        print(char, end="", flush=True)
        time.sleep(0.025)
    print("")
