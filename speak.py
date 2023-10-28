import pyttsx3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "Database\chrome.exe"

def Speak(Text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170) 
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 

    print(f"You: {Text}.")
    engine.say(Text)
    engine.runAndWait()






