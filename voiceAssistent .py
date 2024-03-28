import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, my name is Jarvis, how can I help you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print("You Said: {} \n".format(query))
        return query.lower()
    except Exception as e:
        print("Say That Again....")
        return None

if __name__ == '__main__':
    while True:
        query = takeCommand()
        print(query)  # Print the recognized query for debugging

        if query:
            if 'time' in query:
                current_time = datetime.datetime.now().strftime("%I:%M %p")  # Get current time
                speak(f"The current time is {current_time}")
            elif 'today date' in query:
                current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")  # Get current date
                speak(f"Today is {current_date}")
            elif 'play music' in query:
                webbrowser.open("https://music.youtube.com")
                speak("Opening YouTube Music for you. Search for your desired song and enjoy!")
            elif 'play' in query and 'song' in query:
                # Extracting the song name from the query
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
                # Additional logic might be needed to navigate to specific user/account
            elif 'open messenger' in query:
                webbrowser.open("https://www.messenger.com")
                speak("Opening Messenger for you.")
                # Additional logic might be needed to navigate to specific user/account
            elif 'bye' in query:
                speak("Goodbye!")
                break     
            elif 'search google map' in query:
                # Extracting the location from the query
                location = query.replace("search google map", "").strip()
                # Opening Google Maps with the specified location
                webbrowser.open(f"https://www.google.com/maps/search/{location}")
                speak(f"Showing {location} on Google Maps.")
    
            else:
                webbrowser.open("https://www.google.com/search?q=" + query.replace(" ", "+"))         