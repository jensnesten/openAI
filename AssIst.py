import speech_recognition as sr 
import openai
import time

openai.api_key = "INSERT OPENAI API-KEY"

print("(1) English")
print("(2) Spanish")
print("(3) French")
print("(4) German")
print("(5) Danish")
print("(6) Japanese")

lan = int(input("Language: "))

def transcribe(audio, lan):
    recognizer = sr.Recognizer()
    if lan == 1:
        text = recognizer.recognize_google(audio)
    elif lan == 2:
        text = recognizer.recognize_google(audio, language='es-ES')
    elif lan == 3:
        text = recognizer.recognize_google(audio, language='fr-FR')
    elif lan == 4:
        text = recognizer.recognize_google(audio, language='de-DE')
    elif lan == 5:
        text = recognizer.recognize_google(audio, language='da-DK')
    elif lan == 6:
        text = recognizer.recognize_google(audio, language='ja-JA')
    else:
        print("Language not supported")
    return text 

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text
    return message

while True:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        if lan == 1:
            print("Say something!")
        elif lan == 5:
            print("Sig noget!")
        elif lan == 4:
            print("Sag etwas!")
        elif lan == 3:
            print("Parler!")
        elif lan == 2:
            print("Di algo!")
        elif lan == 6:
            print("何か言って !")
        else:
            print("Error")
        audio = recognizer.listen(source)
        
    prompt = transcribe(audio, lan)
    response = generate_response(prompt)
    for char in response:
        print(char, end="", flush=True)
        time.sleep(0.025)
    print("")