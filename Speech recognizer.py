'''Speech Recognizer:'''
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold=1
        audio=recognizer.listen(source)
    try:
        print("Recognizing...")
        command=recognizer.recognize_google(audio)
        command=command.lower()
        print("You said:",command)
        return command
    except Exception:
        print("Sorry,please say that again")
        return ""
def wish_user():
    hour=datetime.datetime.now().hour
    if hour<12:
        speak("Good Morning")
    elif hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Night")
    speak("I am Rabbit")
with_user()
while True:
    command=take_command()
    if "time" in command:
        current_time=datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "who is" in command:
        person=command.replace("who is","")
        info=wikipedia.summary(person,sentences=2)
        print(info)
        speak(info)
    elif "exit" in command:
        speak("Thank you")
        break



















































    
