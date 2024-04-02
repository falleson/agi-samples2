import pyttsx3 #pip install pyttsx3 == text data into voice/speech
from dotenv import load_dotenv,find_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())
client = OpenAI()

def generate_result(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": "Hi there! How can I assist you today?"
            },
             {
            "role": "user",
            "content": prompt + ", and translate it to Chinese"
            },
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    #print(response)
    return response.choices[0].message.content

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("Hello, I am AGI assistant. How can I help you?")
#result = generate_result("What is the capital of China?")
#speak(result)
while True:
    user_input = input("Ask a question to ai: ")
    if user_input == "exit":
        break
    result = generate_result(user_input)
    print("AGI:",result)
    speak(result)

