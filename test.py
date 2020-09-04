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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Say yes if you would like to choose a location.")
ifLocation = input()

ifLocation = ifLocation.lower()

if ifLocation == "yes" or ifLocation == "yeah" or ifLocation == "ok":
    print("Choose a location.")
    location = input()
else:
    location = ""

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
'''
driver.get("https://twitter.com/Windows")

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
'''
driver.get("https://www.google.co.uk/maps/")
name = driver.find_element_by_id("searchboxinput")
if location != "":
    name.send_keys(location)
    name.send_keys(Keys.RETURN)
