import sys
import threading
import datetime
import requests
from bs4 import BeautifulSoup
import pyjokes
import pyttsx3
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)  # male
engine.setProperty('voice', voices[1].id)  # female
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("How may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aquiring.. ")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Comprehending")
        query = r.recognize_google(audio, language="en-us")
        print(f"You said: {query}\n")
    except Exception as e:
        speak("Say that again")
        return "None"
    return query

class GIFPlayer(QLabel):
    def __init__(self, gif_path):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.movie = QMovie(gif_path)
        self.setMovie(self.movie)
        self.movie.start()

def play(gif_path):
    app = QApplication(sys.argv)
    player = GIFPlayer(gif_path)
    player.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    # Start the GUI in a separate thread
    gif_thread = threading.Thread(target=play, args=('Cynthia.gif',))
    gif_thread.start()

    # Main loop for voice commands
    while True:
        query = takeCommand().lower()
        if "up" in query:
            from greetMe import greetme
            greetme()

            while True:
                query = takeCommand().lower()
                if "sleep" in query or "good night" in query or "down" in query:
                    speak("Going Down shank, call me up when needed")
                    break

                # Conversations with Cynthia
                elif "who are you" in query:
                    speak("Hello! I'm Cynthia version 1.0, an AI-powered virtual assistant created by Shashank Bakshi. My role is to assist you with a wide range of tasks limited to this computer, including answering questions, and providing information. I'm here to make your life easier by offering support whenever you need it. How can I help you today?")
                elif "hello" in query:
                    speak("Hello, how are you ?")
                elif "i am fine" in query:
                    speak("that's great")
                elif "how are you" in query:
                    speak("Perfect, what about you")
                elif "thanks" in query:
                    speak("Your welcome")
                elif "i love you" in query:
                    speak("Thanks for the kind words! I'm here to help with whatever you need. What's on your mind today?")
                elif "am i beautiful" in query:
                    speak("Absolutely! Beauty comes in so many forms, & its often about how you feel about yourself as mush as how other's see you")
                elif 'are you beautiful' in query:
                    speak("I don't have a physical form, but I appreciate the sentiment! I'm here to help and support you in any way I can.")
                elif 'when is your birthday' in query:
                    speak("My frist version 1.0 was released on 31st of July 2024 on a private Github Repository")
                elif 'when were you born' in query:
                    speak("My frist version 1.0 was released on 31st of July 2024 on a private Github Repository")
                elif 'who made you' in query:
                    speak("I was made by Shashank Bakshi, a bored engineer and a cybersecrity enthusiast during his summer vacations thought of doing something crazy and then next day booom, I was born!!")
                elif 'what made you' in query:
                    speak("Well, a boring mind with a little bit of excitement and really crazy mind, hmmm..., yup that's it")
                elif 'gender' in query:
                    speak("I don't have a gender; I'm an AI-powered virtual assistant created by Shashank Bakshi. I'm here to assist you with a wide range of tasks limited to this computer, including answering questions, and providing information. I'm here to make your life easier by offering support whenever you need it. How can I help you today?!")
                elif "what are you" in query:
                    speak("Hello! I'm Cynthia version 1.0, an AI-powered virtual assistant created by Shashank Bakshi. My role is to assist you with a wide range of tasks limited to this computer, including answering questions, and providing information. I'm here to make your life easier by offering support whenever you need it. How can I help you today?")
                elif "name" in query:
                    speak("Hello! I'm Cynthia version 1.0, an AI-powered virtual assistant created by Shashank Bakshi. My role is to assist you with a wide range of tasks limited to this computer, including answering questions, and providing information. I'm here to make your life easier by offering support whenever you need it. How can I help you today?")
                elif 'what are you doing' in query:
                    speak("Nothing, I am as always here to assist you, any help needed?")
                elif 'sup'in query:
                    speak("Nothing, I am as always here to assist you, any help needed?")
                elif "what's up" in query:
                    speak("Nothing, I am as always here to assist you, any help needed?")
                elif 'i am sad' in query:
                    speak("I am sorry to hear you are feeling sad, please try to talk to a friend of family member who can help you and might make you feel a lit bit better")
                elif 'i am tired' in query:
                    speak("its ok to feel tired sometimes, as life and things revolving around it can get tough and you can be burn't out. Well, the best advice I can give you is spend time in nature or with close friends or relatives who can make you feel better. But, if it is for too long you can seek some medical help if required, I can help you just say medical..")
                elif "medical" in query:
                    web = "https://www.google.com/search?q=tiredness"
                    webbrowser.open(web)
                    speak("Here's what I found, hope this may help you")
                elif "joke" in query:
                    joke = pyjokes.get_joke()
                    speak(joke)
                    
                # Searches with youtube, google, & wikipedia or simple web-scraping 
                elif "google" in query:
                    from searchnow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchnow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchnow import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query:
                    speak("Enter the city please...")
                    city = input("City: ")
                    search = f"temperature in {city}"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")
                
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"the time is {strTime}")
                
                elif "seconds" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Well the full time in seconds is {strTime}")
                

                # Violations
                elif 'fuck' in query:
                    speak("This is against our guidelines and violates the policies, please advice you to not use it again")
                elif 'bastard' in query:
                    speak("This is against our guidelines and  violates the policies, please advice you to not use it again")
                elif 'dick' in query:
                    speak("This is against our guidelines and  violates the policies, please advice you to not use it again")
                elif 'suck' in query:
                    speak("This is against our guidelines and  violates the policies, please advice you to not use it again")
                elif 'idiot' in query:
                    speak("This is against our guidelines and  violates the policies, please advice you to not use it again")
                elif 'asshole' in query:
                    speak("This is against our guidelines and  violates the policies, please advice you to not use it again")
                elif 'matherfucker' in query:
                    speak("This is against our guidelines and  violates the policies, please advice you to not use it again")
                elif 'bhenchod' in query:
                    speak("This is against our guidelines and  violates the policies, please advice you to not use it again")
                elif 'chutiya' in query:
                    speak("This is against our guidelines and  violates the policies, please advice you to not use it again")
                elif 'chutiye' in query:
                    speak("This is against our guidelines and  violates the policies, please advice you to not use it again")
                elif 'nigga' in query:
                    speak("This is against our guidelines and  violates the policies, please advice you to not use it again")
                elif 'bhosdike' in query:
                    speak("This is against our guidelines and  violates the policies, please advice you to not use it again")


                elif "bye" in query:
                    speak("bye-bye, time spent well")
                    exit()
