import speech_recognition as sr

# Initialize recognizer class (f
r = sr.Recognizer()

# Reading Microphone as source
with sr.Microphone() as source:
    print("Please talk now")

    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.listen(source)
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio))
    except:
         print("Sorry, audio not recognized")
