import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechrecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
import re
url = "https://covidapi.info/api/v1/global"

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)
            x = takeCommand()
            Y = re.search ('confirmed:(\d+)',x)
            print ('this is the number of cases:-',Y)
            print(response.text)
            speak(response.text)
 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("i am Alien sir. please tell me how may i help you") 

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognising..")
        query = r.recognize_google(audio ,language='en-in')
        print("User said:",query)

    except Exception as e:
        #print(e)
        print("please say again..")
        return "none"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmailcom',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    speak("HEllo Astronuts")
    wishMe()
    
    
    
    #while True:
    if 1 :
        query = takeCommand().lower()
    # logic fot executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

        elif 'email to isha' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "ishayourEmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry, i am not able to send your email")

        elif 'precautions' in query:
            webbrowser.open("file:///C:/hackathon/precautions.html")

        elif 'open historical data'in query:
            url = "https://covidapi.info/api/v1/country/IND"

            payload = ""
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            print(response.text)
     
        elif 'open current data' in query:
            url = "https://covidapi.info/api/v1/global"

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)
            x = takeCommand()
            Y = re.search ('confirmed:(\d+)',x)
            print ('this is the number of cases:-',Y)
            print(response.text)
            speak(response.text)