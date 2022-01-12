import pyttsx3
import datetime

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
    # Crear menu de opciones para usar anton

time()
date()
greeting()