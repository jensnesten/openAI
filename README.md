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
You can see the different text models at: https://platform.openai.com/docs/models/gpt-3

Chatbots using the speech_recognition framework are set to the google speech API. You can use openAI 
Whisper if you prefer(it runs offline), 
read the docs at: https://pypi.org/project/SpeechRecognition/.

You need the Pyaudio framework to capture audio from microphone. If you're running macOS, you might run 
into an error using pip install pyaudio. Install portaudio before pyaudio. 

```bash
brew install portaudio
pip install pyaudio
```
I don't know why but it works.
# Dependencies
```bash
pip install openai
pip install SpeechRecognition
pip install requests
```
![GPT3](https://user-images.githubusercontent.com/42718681/218810862-0df0a789-4cfa-4e9a-944b-6e20a1508d6c.gif)


Have fun!
