import os 
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random

engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice' ,voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good mornig sir ")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir ")
    else:
        speak("good evening sir")
    speak("how may i help you")

def takecommand():
    #it takes microphone input and and returns it as string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("sun raha hu....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said :{query}\n")
    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query

if __name__=="__main__":
    #speak("yo yo honey singh")
    wishme()
    while True:
        query=takecommand().lower()

        if "wikipedia" in query:
            speak("searching wikipedia results")
            query= query.replace("wikipedia","")
            result= wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        
        elif "play music" in query:
            music_dir='D:\\music'
            num= random.randrange(1, 30)
            songs= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[num]))
        
        elif "the time" in query:
            str_time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {str_time}")
        
        elif "open my email" in query:
            url = 'https://mail.google.com'
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)
        
        elif "google search" in query:
            query=query.replace("google search","")
            g_q=f"https://www.google.com/search?q={query}"
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(g_q)
        
        elif "shutdown" in query:
            speak("shutting down have a nice day")
            exit()