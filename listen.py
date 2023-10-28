import speech_recognition as sr
from googletrans import Translator

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=8)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language="ur")

    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

    query = str(query).lower()
    return query

def translation_urdu_to_eng(Text):
    line = str(Text)
    translator = Translator()
    data = translator.translate(line, src="ur", dest="en")
    print(f"You: {data.text}.")
    return data.text

def MicExecution():
    query = Listen()
    if query:
        data = translation_urdu_to_eng(query)
        return data
    else:
        print("Could not understand the audio.")

MicExecution()
