import speech_recognition as sr
from googletrans import Translator

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

# Use the microphone as source
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

    try:
        # Recognize speech in native language (auto-detect)
        text = recognizer.recognize_google(audio, show_all=False)
        print(f"Original Speech Recognized: {text}")

        # Translate to English
        translation = translator.translate(text, dest='en')
        print(f"Translated to English: {translation.text}")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError:
        print("Speech recognition service is unavailable.")
