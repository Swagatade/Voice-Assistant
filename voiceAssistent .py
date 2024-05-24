import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Microphone accessed successfully.")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            print("Listening...")
            audio = recognizer.listen(source)
            
            try:
                print("Recognizing...")
                command = recognizer.recognize_google(audio)
                print(f"User said: {command}")
                return command.lower()  # Convert to lowercase for easier comparison
            except sr.UnknownValueError:
                print("Could not understand audio")
                speak("Sorry, I couldn't understand that.")
                return None
            except sr.RequestError:
                print("Could not request results; check your network connection")
                speak("Sorry, there seems to be a network issue.")
                return None
    except Exception as e:
        print(f"Error accessing the microphone: {e}")
        speak("Sorry, I am having trouble accessing the microphone.")
        return None

if __name__ == '__main__':
    speak("Hello, my name is Jarvis, how can I help you today?")
    while True:
        query = recognize_speech()
        if query:
            query = query.lower()  # Ensure query is lowercase for consistent comparison
            print(f"User query: {query}")
            
            if 'time' in query:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The current time is {current_time}")
            elif 'today date' in query:
                current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
                speak(f"Today is {current_date}")
            elif 'play music' in query:
                webbrowser.open("https://music.youtube.com")
                speak("Opening YouTube Music for you. Search for your desired song and enjoy!")
            elif 'play' in query and 'song' in query:
                song_name = query.replace("play", "").replace("song", "").strip()
                webbrowser.open(f"https://music.youtube.com/search?q={song_name}")
                speak(f"Searching for {song_name} on YouTube Music. Have fun listening!")
            elif 'open gmail' in query:
                webbrowser.open("https://mail.google.com")
                speak("Opening Gmail for you.")
            elif 'open facebook' in query:
                webbrowser.open("https://www.facebook.com")
                speak("Opening Facebook for you.")
            elif 'open instagram' in query:
                webbrowser.open("https://www.instagram.com")
                speak("Opening Instagram for you.")
            elif 'open linkedin' in query:
                webbrowser.open("https://www.linkedin.com")
                speak("Opening LinkedIn for you.")
            elif 'open google maps' in query:
                webbrowser.open("https://www.google.com/maps")
                speak("Opening Google Maps for you.")
            elif 'open groww' in query:
                webbrowser.open("https://groww.in")
                speak("Opening Groww for you.")
            elif 'open whatsapp' in query:
                webbrowser.open("https://web.whatsapp.com")
                speak("Opening WhatsApp for you.")
            elif 'open messenger' in query:
                webbrowser.open("https://www.messenger.com")
                speak("Opening Messenger for you.")
            elif 'search google map' in query:
                location = query.replace("search google map", "").strip()
                webbrowser.open(f"https://www.google.com/maps/search/{location}")
                speak(f"Showing {location} on Google Maps.")
            elif any(word in query for word in ['bye', 'exit', 'quit', 'goodbye']):
                speak("Goodbye!")
                break
            else:
                webbrowser.open("https://www.google.com/search?q=" + query.replace(" ", "+"))
                speak("Searching the web for you.")
