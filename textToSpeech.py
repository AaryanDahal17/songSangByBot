import pyttsx3
from gtts import gTTS
import os


print('Playing music...')

file = open('lyrics.txt', 'r',encoding='utf-8')
lyricsData = file.read()
file.close()


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)  
    engine.setProperty('volume', 0.9)  
    engine.setProperty('voice', 'en-us')  
    engine.say(text)
    engine.runAndWait()


def singAudio(text):
    
    language = 'hi'
    tts = gTTS(text=text, lang=language)

    tts.save("output.mp3")

    os.system("start output.mp3")



# singAudio(lyricsData)
speak(lyricsData)