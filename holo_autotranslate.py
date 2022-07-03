import speech_recognition as sr
import pyaudio
from googletrans import Translator, constants

translator = Translator()
init_rec = sr.Recognizer()
mic=sr.Microphone(device_index=3)
with sr.Microphone(device_index=0) as source:
    while True:
        
            audio_data = init_rec.listen(source, phrase_time_limit=5)
            try:
                print("Recognizing your text.............")
                text = init_rec.recognize_google(audio_data,language="ja-JP")
                print(text)
                translation=translator.translate(text,src='ja',dest='en')
                print("translation")
                print(translation.text)
            except:
                print("failed this time")
