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

time()