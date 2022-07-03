'''y="世界のこの大きさでありたくてその方がさらにもいるって感じ"
from googletrans import Translator, constants
translator = Translator()
print(y)
translation=translator.translate(y,src="ja",dest="en")
print(translation.text)'''
import speech_recognition as sr
while True:
    try:
        init_rec = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:
            audio_data = init_rec.listen(source)
            text = init_rec.recognize_google(audio_data,language="ja-JP")
            print(text)
    except:
        print("number","failed")
