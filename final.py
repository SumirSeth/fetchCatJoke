from tkinter import *
from tkinter import ttk
import requests, json


root = Tk() 
 
root.title("Cat Facts")
root.config(background="#0A1D37")


def click():
    url = "https://catfact.ninja/fact?max_length=500"

    response = requests.request("GET", url=url)
    data = json.loads(response.text)

    fact = data["fact"]
    label.config(text=fact, font=("Monospace", 24), background="#0d274a", foreground="#FFEEDB")
    label.pack()
 
submit = Button(root, text="Get Cat Fact", font=("Helvetica 11 bold", 20), command=click, background="#f09465", activebackground="#f7c4b5", foreground="#303030").pack(padx=20, pady=20) 
label = Message(root)
 
 
 
root.mainloop()   