import pyttsx3
import datetime as dt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id) #male
engine.setProperty('voice', voices[1].id) #female
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetme():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Shank,")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon Shank,")
    
    else:
        speak("Good Evening Shank,")

    speak("How may I help you")

    
