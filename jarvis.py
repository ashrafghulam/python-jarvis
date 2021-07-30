import pyttsx3
import speech_recognition as sr
import datetime

NAME = "Jarvis"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")

    elif hour >=12 and hour <18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am {} Sir. Please tell me how may I help you".format(NAME))

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print("User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please...")
        return None



if __name__ == "__main__":
    wishMe()
