# List of modules that I have imported
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
from tkinter import *
import os
import config
from PyDictionary import PyDictionary
from translate import Translator
import corona
import pyjokes
import calculator


configured = False
global alarmCheck
alarmCheck = False

def play50():
    playsound.playsound("50cent.mp3")
    os.remove('alarm.txt')


if os.path.isfile('config.py'):
    configured = True
if configured == False:
    root = tk.Tk()
    items = []
    root.title('Configuring')
    canvas = tk.Canvas(root, height=700, width=800, bg="#008080")
    canvas.pack()
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def addToFile():
        item = e.get()
        item = str(item)
        items.append(item)
        for widget in frame.winfo_children():
            widget.destroy()
        for i in range(0, len(items)):
            label = tk.Label(frame, text=items[i], bg="#C0C0C0")
            label.pack()
        if len(items) > 2:
            root.destroy()
    label = tk.Label(
        text="Enter 3 Email Addresses that you would like to send emails to using this voice assistant:")
    label.pack()
    e = tk.Entry(root, width=50)
    e.pack()
    add = tk.Button(root, text="Click", padx=10, pady=5, fg="white",
                    bg="#C0C0C0", font=('helvetica', 9), command=addToFile)
    add.pack()
    root.mainloop()
    with open('config.py', 'w') as f:
        f.write("email_address = ")
        f.write('"')
        f.write(items[0])
        f.write('"')
        f.write("\n")
        f.write("email_address2 = ")
        f.write('"')
        f.write(items[1])
        f.write('"')
        f.write("\n")
        f.write("email_address3 = ")
        f.write('"')
        f.write(items[2])
        f.write('"')


'''
    gui
'''


root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=800, bg="#008080")
canvas.pack()
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


global calls
calls = ["Hello, how can I help?", "What can I do for you?", "What's the time? Its time for me to help",
         "How may I help you?", "Who do you call? Me", "000110101 oops I mean what do you need help with?"]


# Function that allows the assistant to speak
def speak(text):
    destroyed = False
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    if os.path.isfile('transcript.txt'):
        f = open('transcript.txt', 'r')
        readFile = f.read()
        transcript = readFile.split('\n')
        f.close()
    else:
        with open('transcript.txt', 'w') as f:
            print("file made")

    if len(transcript) > 25:
        for widget in frame.winfo_children():
            widget.destroy()
            destroyed = True
        items_temp = []
        for i in range(1, 26):
            items_temp.append(transcript[i])
        transcript = items_temp
    transcript.append(text)
    f = open('transcript.txt', 'w')
    for i in range(len(transcript)):
        f.write(transcript[i])
        f.write('\n')
    f.close()
    if destroyed == True:
        for i in range(len(transcript)):
            tText = transcript[i]
            label = tk.Label(frame, text=tText)
            label.pack()
    else:
        label = tk.Label(frame, text=text)
        label.pack()
    Tk.update(root)


# Function that allows audio from the microphone to be recognised
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        try:
            said = r.recognize_google(audio)
            print(said)
            return said
        except:
            print("unrecognised")


# Function that removes the voice file from which the assistant speaks from so that it can speak again
def remove_file():
    os.remove('voice.mp3')


'''
Functions of what it can do
'''


def get_weather_today():
    page = requests.get('https://www.bbc.co.uk/weather/2643743')
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    info = soup.find_all(class_='wr-value--temperature--c')
    # print(info)
    high_today = info[0].get_text()
    low_today = info[1].get_text()
    print(high_today)
    print(low_today)
    tie = time()
    timeData = ctime(tie)
    splitData = timeData.split(" ")
    times = splitData[3]
    times = times.split(":")
    hour = times[0]
    hour = int(hour)
    if hour > 17 or hour < 5:
        speak("Right now, it is " + high_today)
        remove_file()
    else:
        speak("Today, right now, it is " +
              high_today + ". Today there is a low of " + low_today)
        remove_file()


def get_news():
    page = requests.get('https://www.bbc.co.uk/news')
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    mainHeadline = soup.find(
        class_='gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text')

    headline1 = mainHeadline.get_text()

    secondaryHeadlines = soup.find_all(
        class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')

    headline2 = secondaryHeadlines[0].get_text()

    headline3 = secondaryHeadlines[1].get_text()

    speak("Here are the top 3 headlines for today on BBC News")
    remove_file()
    speak(headline1)
    remove_file()
    speak(headline2)
    remove_file()
    speak(headline3)
    remove_file()


def get_time():
    tie = time()
    timeData = ctime(tie)
    splitData = timeData.split(" ")
    times = splitData[3]
    times = times.split(":")
    hour = times[0]
    minutes = times[1]
    speak("It's " + hour + " " + minutes)
    remove_file()


def alarm():
    tie = time()
    timeData = ctime(tie)
    splitData = timeData.split(" ")
    times = splitData[3]
    times = times.split(":")
    hour = times[0]
    minutes = times[1]
    hour = int(hour)
    minutes = int(minutes)
    amount = int(input("length: "))
    alarmMinutes = minutes + amount
    print(alarmMinutes)
    if alarmMinutes >= 60:
        print("big number")
        if alarmMinutes == 60:
            hour = hour + 1
        elif alarmMinutes > 60:
            temp = alarmMinutes - 60
            hour = hour + 1 
            alarmMinutes = temp

    f = open('alarm.txt', 'w')
    hour = str(hour)
    f.write(hour)
    f.write("\n")
    alarmMinutes = str(alarmMinutes)
    f.write(alarmMinutes)
    f.close()



'''
end of functions
'''


# Running an infinite loop in which the assistant is called when the keyword is said


def calling_assistant():
    global running_main_loop
    running_main_loop = False
    randomCall = random.randint(0, len(calls)-1)
    randomC = calls[randomCall]
    while not running_main_loop:
        if os.path.isfile('alarm.txt'):
            print ("running this check")
            f = open('alarm.txt', 'r')
            readfile = f.read()
            f.close()
            hour1 = readfile[0]
            hour1 = int(hour1)
            minute1 = readfile[1]
            minute1 = int(minute1)
            alarmTime = hour1, minute1
            tie = time()
            timeData = ctime(tie)
            splitData = timeData.split(" ")
            times = splitData[3]
            times = times.split(":")
            hour = times[0]
            minutes = times[1]
            hour = int(hour)
            minutes = int(minutes)
            totalTime = hour, minutes
            print ("running this check")
            if minute1 == minutes:
                print ("compared")
                play50()
        print("running")
        #text = get_audio()
        text = input("text")
        if "hello" in text or "Hello" in text:
            speak(randomC)
            remove_file()
            running_main_loop = True
            main_loop()

def main_loop():
    running_main_loop = True
    while running_main_loop:
        if os.path.isfile('alarm.txt'):
            print ("running this check")
            f = open('alarm.txt', 'r')
            readfile = f.read()
            readfile = readfile.split("\n")
            f.close()
            hour1 = readfile[0]
            hour1 = int(hour1)
            minute1 = readfile[1]
            minute1 = int(minute1)
            alarmTime = hour1, minute1
            tie = time()
            timeData = ctime(tie)
            splitData = timeData.split(" ")
            times = splitData[3]
            times = times.split(":")
            hour = times[0]
            minutes = times[1]
            hour = int(hour)
            minutes = int(minutes)
            totalTime = hour, minutes
            print ("running this check")
            print(minute1)
            print(minutes)
            if minute1 == minutes:
                print ("compared")
                play50()

        #text = get_audio()
        text = input("text")

        if "weather" in text:
            get_weather_today()
        elif "news" in text:
            get_news()
        elif "time" in text:
            get_time()
        elif "alarm" in text:
            alarm()
        else:
            speak("I am not sure how to do that at the moment")
            remove_file()

        running_main_loop = False

    calling_assistant()

# button to run the assistant


initialise = tk.Button(root, text="Run", padx=10, pady=5, fg="white",
                       bg="#C0C0C0", font=('helvetica', 9), command=calling_assistant)
initialise.pack()

# running the gui

root.mainloop()

# cleanup

f = open('transcript.txt', 'w')
f.write("")
f.close()

if os.path.isfile('voice.mp3'):
    os.remove('voice.mp3')
if os.path.isfile('alarm.txt'):
    os.remove('alarm.txt')
