import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
def SpeakText(commad):
        engine = pyttsx3.init()
        if "love" in commad:
                engine.say("Let me think ")
                engine.runAndWait()
                engine.say("Yes I love you")
        else:
                engine.say(commad)
        engine.runAndWait()

# SpeakText("Love you baby")

# Initialize recognizer
r = sr.Recognizer()

with sr.Microphone() as mic:
    print("Calibrating the background noise, please wait...")
    r.adjust_for_ambient_noise(mic, duration=3)  # Adjusting for ambient noise
    print("Calibrated")
    
    print("Listening...")
    audio = r.listen(mic)  # Capture audio from the microphone

    # Recognize speech using Google Web Speech API
    my_text = r.recognize_google(audio)
    my_text = my_text.lower()  # Convert text to lowercase
    if "jarvis" in my_text:
     SpeakText(my_text)
    else:
     print("Please use jarvis in the command")