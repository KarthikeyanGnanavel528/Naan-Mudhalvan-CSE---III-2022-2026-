import speech_recognition as sr

def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 4000  # Adjust this based on your environment
    
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... (Speak now, say 'quit' to exit)")
        
        try:
            while True:
                # Listen for audio input
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=5)
                
                try:
                    # Recognize speech using Google Speech Recognition
                    text = recognizer.recognize_google(audio)
                    print(f"Recognized: {text}")
                    
                    # Exit if user says "quit"
                    if "quit" in text.lower():
                        print("Exiting...")
                        break
                        
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                    
        except KeyboardInterrupt:
            print("\nProgram stopped by user")

if __name__ == "__main__":
    recognize_speech()
