# openAI-FUN

Go to openai.com and signup for you API-key. 

All chatbots are currently set to use the davinci-003 engine

```python
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
```
Chatbots using the speech_recognition framework are set to the google speech API. You can use openAI Whisper if you prefer, read the docs at: https://pypi.org/project/SpeechRecognition/.

You need Pyaudio to capture audio from microphone. If you're running macOS, you might run into an error using pip install pyaudio. Remember installing portaudio before pyaudio.

```bash
brew install portaudio
pip install pyaudio
```


