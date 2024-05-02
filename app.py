import speech_recognition as sr
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/record', methods=["GET", "POST"])
def home():
    if request.method == 'POST':  # Corrected to uppercase 'POST'
        # Initialize recognizer class 
        r = sr.Recognizer()

        # Reading Microphone as source
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            
            try:
                # using google speech recognition
                output = r.recognize_google(audio)
            except:
                output = "Sorry, audio not recognized"
            
        return render_template("index.html", output=output)
    
if __name__ == "__main__":
    app.run(debug=True)
