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
        for i in range(0, 11):
            if i == 0:
                day = today[0].get_text()
                label = tk.Label(frame, text=day)
                label.pack()
            elif i % 2 != 0:
                day = dates[i].get_text()
                label = tk.Label(frame, text=day)
                label.pack()
            else:
                day = day
            temp = info[i].get_text()
            label = tk.Label(frame, text=temp)
            label.pack()
    else:
        for i in range(0, 11):
            if i == 0 or i == 1:
                day = today[0].get_text()
                label = tk.Label(frame, text=day)
                label.pack()
            elif i % 2 == 0:
                day = dates[i].get_text()
                label = tk.Label(frame, text=day)
                label.pack()
            else:
                day = day
            temp = info[i].get_text()
            label = tk.Label(frame, text=temp)
            label.pack()


weatherB = tk.Button(root, text="Click", padx=10, pady=5, fg="white",
                     bg="#C0C0C0", font=('helvetica', 9), command=get_weather_week)
weatherB.pack()


tk.mainloop()
