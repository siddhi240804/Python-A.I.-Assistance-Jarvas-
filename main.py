import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import openai
from config import apikey
import datetime
import random



def say(text):
     engine = pyttsx3.init()
     engine.say(text)
     engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return ("Some Error Occured. Sorry from Jarvis.")

if __name__ == '__main__':
     print('Pycharm')
     say("Hello.. I am Jarvis AI , Good Evening...Hello Maam...............................let's see Jarvas............       ")
     while True:
         print("Listening.............")
         query = takeCommand()
         say(query)
         sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
         for site in sites:
             if f"Open {site[0]}".lower() in query.lower():
                 say(f"Opening {site[0]} maam....")
                 webbrowser.open(site[1])
         if "open music" in query:
             musicPath = "C:/Users/Lenovo/Downloads/kahna ji(music).mp3"
             os.startfile(musicPath)

         if "open song" in query:
             musicPath = "C:/Users/Lenovo/Downloads/Bappa song.mp3"
             os.startfile(musicPath)

         if "the time" in query:
             hour = datetime.datetime.now().strftime("%H")
             min = datetime.datetime.now().strftime("%M")
             say(f"Sir time is {hour} hour and {min} minutes")



