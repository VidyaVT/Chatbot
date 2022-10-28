from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import sys
from AppOpener import run
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 260)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def salutations():
    
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("How may i Help You?")

def takeinput():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")
    
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query



    
if __name__ == "__main__":
    salutations()
    while True:
        query = takeinput().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak('According To Wikipedia')
            speak(results)

        elif 'open youtube ' in query:
            webbrowser.open('www.youtube.com') 

        elif 'open notepad' in query:
            os.system('Notepad')  
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'open google' in query:
            webbrowser.open('www.google.com')
        
        elif 'open reddit' in query:
            webbrowser.open('www.reddit.com')
        
        elif 'my playlist' in query:
            webbrowser.open('https://www.youtube.com/watch?v=IuUDRU9-HRk&list=PLP0zeA5un-Eaw83emzhnlfzRm7K1g3iu-&index=1&ab_channel=SiriusXM')

        elif 'news updates' in query:
            webbrowser.open('https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en')


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {strTime}")

        elif 'exit now' in query:
            sys.exit()

        
        
        
        
