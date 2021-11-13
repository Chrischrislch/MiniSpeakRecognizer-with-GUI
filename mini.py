from tkinter import *
from tkinter import ttk
import tkinter as tk
import speech_recognition as sr
import time

obj = tk.Tk()
obj.title("Recognizer")
obj.geometry('300x250')
obj.resizable(0,0)

def rec():
    r = sr.Recognizer()
    #msg.configure(text="Say something")
    while True:
        with sr.Microphone() as source: 
            r.adjust_for_ambient_noise(source)
            #Output.insert(END,"Recording for 10 seconds\n")
            audio = r.listen(source,timeout=5)
            #Output.insert(END,"Done recording\n")
        try:
            txt = r.recognize_google(audio, language="en-US")
            msg.configure(text=txt)
            Output.insert(END,"Decoded message:\n")
            Output.insert(END,txt)
        except Exception as e:
            Output.insert(END,"Try Again!\n")
            break

msg = tk.Label()
l = Label(text = "Click Start to record for 5s")
Display = Button(obj, height = 2,
                 width = 20, 
                 text ="Start",
                 command = lambda:rec())
Output = Text(obj, height = 10, 
              width = 25, 
              bg = "light cyan")
b2 = Button(obj, height = 2,
            width = 20,
            text = "Exit",
            command = obj.destroy) 
l.pack()
Display.pack()
Output.pack()
b2.pack()
obj.mainloop()