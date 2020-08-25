import os
import playsound
import speech_recognition as sr
from gtts import gTTS
from bs4 import BeautifulSoup
import requests
from time import time, ctime
import random
import wikipedia as wiki
import smtplib
import tkinter as tk
from tkinter import filedialog, Text
import os
from PyDictionary import PyDictionary
from translate import Translator
import corona
import pyjokes


def randomFacts():
    page = requests.get('http://randomfactgenerator.net/')
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    info = soup.find_all(id='z')
    fact = info[0].get_text()
    fact = fact.replace('Tweet', '')
    print(fact)


randomFacts()
