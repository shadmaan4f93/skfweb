import os
import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from django.contrib import messages

class SpeechRecognitions:
    @staticmethod
    def play_welcome_message(username):
       
        language = 'en'
        dt = datetime.datetime.now()
        if(dt.hour <= 12):
            greating = "good morning"
        elif (dt.hour > 12):
            greating = "good after noon"
        message = "Hay" + greating + "welcome to skfweb"
        #myobj = gTTS(text=message, lang=language, slow=False)
        #myobj.save("welcome.mp3")
        #playsound("welcome.mp3", block = False)

    def speech_recognition(request):
        try:
            # message = ""
            # r = sr.Recognizer()
            # with sr.Microphone() as source:
            #     print("Speak:")
            #     #playsound("welcome.mp3")
            #     messages.add_message(request, messages.INFO, 'Please say somthing.')
            #     audio = r.listen(source, timeout=5, phrase_time_limit=5)
            #     print("You said " + r.recognize_google(audio))
            #     message = r.recognize_google(audio)
            return "Could not recognize your voice"
        except BaseException as e:
            pass
            message = "Could not recognize your voice"
            return message