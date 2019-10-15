import os
import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

class SpeechRecognitions:
    @staticmethod
    def play_welcome_message(username):
        try:
            language = 'en'
            dt = datetime.datetime.now()
            if(dt.hour <= 12):
                greating = "good morning"
            elif (dt.hour > 12):
                greating = "good after noon"
            message = "Hay" + greating + "welcome to skfweb"
            #myobj = gTTS(text=message, lang=language, slow=False)
            #myobj.save("welcome.mp3")
            playsound("welcome.mp3", block = False)
        except Exception as e:
            pass
       
        

    def speech_recognition(s):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak:")
            audio = r.listen(source)

        try:
            print("You said " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

class dropbox_upload:
    def __init__(self):
        pass
    def upload(self):
        
        pass
