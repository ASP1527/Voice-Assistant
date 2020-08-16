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


x = corona.get_deaths()
print(x)
