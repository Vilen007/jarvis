import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("Hey, I'm jarvis! How may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("abdulrehman7440237@gmail.com", "<3mani<3")
    server.sendmail("",to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        #logic  for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 1)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open lms' in query:
            webbrowser.open("lms.uog.edu.pk/login/index.php")
        elif 'play music' in query:
            mdir = 'D:\\songs'
            song = os.listdir(mdir) 
            os.startfile(os.path.join(mdir, song[0]))
        elif 'play lucifer' in query:
            ldir = 'D:\\lucifer'
            episode = os.listdir(ldir) 
            os.startfile(os.path.join(ldir, episode[0]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir th time is {strtime}")
        elif 'open code' in query:
            cdir = '"D:\\Microsoft VS Code\\Code.exe"'
            os.startfile(cdir)
        elif 'email to' in query:
            try:
                speak("What Shout I Say")
                content = takeCommand()
                to = 'marghoobahmad23@gmail.com'
                sendEmail(to ,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry i'm not able to send this mail")
