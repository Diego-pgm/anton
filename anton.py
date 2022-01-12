import os
import psutil
import pyjokes
import pyttsx3
import smtplib
import datetime
import pyautogui
import wikipedia
import webbrowser as wb
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
        print('Please repeat the command I didnt get it right.')
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

def screenshot():
    img = pyautogui.screenshot()
    img.save('ss.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at'+usage)
    speak('percent')
    battery = psutil.sensors_battery()
    speak('Battery is')
    speak(battery.percent)
    speak('percent')

def jokes():
    joke = pyjokes.get_joke()
    speak(joke)


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
        
        elif 'chrome' in query:
            speak('What should i open?')
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s &'
            search = takeCommand().lower()
            try:
                wb.get(chromepath).open_new_tab(search+'.com')
            except Exception as e:
                speak('please install brave browser')
                print(e)

        elif 'brave' in query:
            speak('What should i open?')
            chromepath = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s &'
            search = takeCommand().lower()
            try:
                wb.get(chromepath).open_new_tab(search+'.com')
            except Exception as e:
                speak('please install brave browser')
                print(e)

        elif 'spotify' in query:
            speak('Opening spotify')
            os.system('spotify.exe')

        elif 'play that country music whiteboy' in query:
            songs_dir = 'C:/Music'  #-----> modify this line to get the location of the music in the machine
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        # Work in this option and maybe a db for users so theres an email and use the send email funct too and a table for reminders.
        elif 'remember' in query:
            speak('what should i remember')
            data = takeCommand()
            speak('you want me to remember that'+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak('you told me to remember that'+remember.read())

        # Work this one
        elif 'screenshot' in query:
            screenshot()

        # Implement on this one the disk usage and memory usage
        elif 'cpu' in query:
            cpu()

        elif 'logout' in query:
            os.system('shutdown -l')
        elif 'restart' in query:
            os.system('shutdown /r /t 1')
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

        elif 'joke' in query:
            jokes()
        
        elif 'offline' in query:
            speak('Disconected.')
            quit()
