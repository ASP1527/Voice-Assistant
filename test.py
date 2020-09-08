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

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=800, bg="#008080")
canvas.pack()
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


def get_weather_week():
    temps = []
    days = []
    page = requests.get('https://www.bbc.co.uk/weather/2643743')
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    info = soup.find_all(class_='wr-value--temperature--c')
    dates = soup.find_all(class_='wr-date__long')
    today = soup.find_all(class_='wr-date')
    # print(info)
    tie = time()
    timeData = ctime(tie)
    splitData = timeData.split(" ")
    times = splitData[3]
    times = times.split(":")
    hour = times[0]
    hour = int(hour)
    if hour > 17 or hour < 5:
        days = ["Today"]
        for i in range(0, 10):
            temp = info[i].get_text()
            temps.append(temp)
        for i in range(1, 5):
            day = dates[i].get_text()
            days.append(day)
        print(days[0])
        print(temps[0])
        print(temps[1])
        print(days[1])
        print(temps[2])
        print(temps[3])
        print(days[2])
        print(temps[4])
        print(temps[5])
        print(days[3])
        print(temps[6])
        print(temps[7])
        print(days[4])
        print(temps[8])
        print(temps[9])
    else:
        days = ["Tonight"]
        for i in range(0, 9):
            temp = info[i].get_text()
            temps.append(temp)
        for i in range(1, 5):
            day = dates[i].get_text()
            days.append(day)
        print(days[0])
        print(temps[0])
        print(days[1])
        print(temps[1])
        print(temps[2])
        print(days[2])
        print(temps[3])
        print(temps[4])
        print(days[3])
        print(temps[5])
        print(temps[6])
        print(days[4])
        print(temps[7])
        print(temps[8])


get_weather_week()
