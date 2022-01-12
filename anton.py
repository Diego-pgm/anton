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

time()
date()