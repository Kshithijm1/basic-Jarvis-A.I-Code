import pyttsx3
import speech_recognition as sr

screenshot = [
"take a screenshot", 
"Screenshot", 
"Take picture of screen", 
"SS", 
"Take screenshot", 
"Screen picture"
]

    

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        command.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)
        
        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language = 'en-in')
            print(f"You said : {query}")
        
        except Exception as e:
            return "none"
        
        return query

while True: 
    
    query = takecommand()

    for d in screenshot:
        if d == query:
            print("hi")