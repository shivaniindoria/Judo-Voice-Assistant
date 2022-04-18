# from asyncio import exceptions
import pyttsx3
import datetime 
import speech_recognition as sr  
import wikipedia
import webbrowser
import googlesearch
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    # speak("i am judo, your voice assistant, how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 300
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again, Please...")
        return "none"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com','your-password')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close

if __name__ == "__main__":
    wishMe() 
    speak("i am judo , your voice assistant. ")
    while True:
    # if 1:
        query = takeCommand().lower()
    # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'hello' in query:
            speak("hi, how can i help you ?")
        elif 'hai' in query:
            speak("hello , how can i help you ?")
        elif 'how are you' in query:
            speak(" i am good, how can i help you ? ")
        elif 'github' in query:
            googlesearch("github.com")
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Dell\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")
        elif 'code' in query:
            codePath = "E:\\colorpicker\\draw.html"
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak('what should i say?')
                content = takeCommand()
                to = "emailreciever@gmail.com"
                sendEmail(to, content)
                speak('Email has been sent.')
            except Exception as e:
                print(e)
                speak('sorry my friend, i am not able to send this email at the moment')
