import pyttsx3
import smtplib
import datetime
import wikipedia
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    zeit = datetime.datetime.now().strftime("%I:%M:%S")
    speak('the current time is')
    speak(zeit)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    dat = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(dat)
    speak(month)
    speak(year)


def greeting():
    speak('welcome back')
    hour = datetime.datetime.now().hour
    if hour >=6 and hour < 12:
        speak('good morning')
    elif hour >=12 and hour < 18:
        speak('good afternoon')
    else:
        speak('good night')
    speak('anton at your service, how can i help you')
    # Create menu to help user use anton


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        # This line probably will only be used in production
        print(query) 
    except Exception as e:
        print(e) # Debug line
        print('Please repeat the command I dindt get it right.')
         # This IS key for multi-threading
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mail@mail.com', 'password') # Configure this with the proper credentials maybe make a db with users and the credentials
    server.sendmail('dest@destination.com', to, content)
    server.close()


if __name__ == "__main__":
    greeting()
    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            query = query.replace('%s wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            print(result) # production
            speak(result)

        elif 'send mail' in query:
            try:
                speak('what shoyld i send')
                content = takeCommand()
                to = 'dest@destination.com'
                sendEmail(to, content)
                speak('Email sent.')
            except Exception as e:
                print(e) # Debug line
                print('[-] Unable to send mail please read message above')

        
        elif 'offline' in query:
            quit()
