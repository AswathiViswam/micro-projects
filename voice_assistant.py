import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time
import wikipedia

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try :
              print("recognizing...")
              data = recognizer.recognize_google(audio)
              print(data)
              return data
        except sr.UnknownValueError :
             print("didn't understand")
             speechtxt("didn't understand")
             return ""

def speechtxt(x):
     engine = pyttsx3.init()
     voices = engine.getProperty('voices')
     engine.setProperty('voices',voices[0].id)
     rate = engine.getProperty('rate')
     engine.setProperty('rate',150)
     engine.say(x)
     engine.runAndWait()

if __name__ == '__main__':
    if "hey linda" in sptext().lower():
        while True:
            speech = sptext().lower()
            if "your name" in speech:
                name = "my name is linda"
                speechtxt(name)
            elif "age" in speech:
                age = "i am 1 month old"
                speechtxt(age)
            elif "time" in speech:
                cur_time = datetime.datetime.now().strftime("%I%M%p")   
                speechtxt(cur_time)    
            elif "youtube" in speech:
                webbrowser.open("https://www.youtube.com/")
            elif "song" in speech :
                webbrowser.open("https://open.spotify.com/track/1aEsTgCsv8nOjEgyEoRCpS?si=5c9d9df749d24233")
            elif "joke" in speech:
                joke = pyjokes.get_joke(language = "en",category = "neutral") 
                print(joke)
                speechtxt(joke)  
            elif "exit" in speech :
                speechtxt("thank you")    
                break
            else:
                # Treat as GK question
                try:
                    result = wikipedia.summary(speech, sentences=2)
                    print("Answer:", result)
                    speechtxt(result)
                except wikipedia.exceptions.DisambiguationError:
                    speechtxt("Your question is too broad. Please be more specific.")
                except wikipedia.exceptions.PageError:
                    speechtxt("I couldn't find an answer to that question.")


            time.sleep(5)
    else:
        print("thank you")

             

