import pyttsx3

def speak(text):
    try:
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)

        engine.say(str(text)[:200])
        engine.runAndWait()

    except Exception as e:
        print("Voice Error:", e)