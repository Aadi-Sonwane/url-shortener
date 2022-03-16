
from tkinter import *
import pyshorteners
# Function for short URL and set value in textbox
def convert():
    s = pyshorteners.Shortener().tinyurl.short(url.get())
    shorturl.set(s)
root = Tk()
root.title(" URL Shortner")
root.geometry("400x350")
root.resizable(False, False)
root.config(background="#35fc99")
# Declare variables
url = StringVar()
shorturl = StringVar()
# Design labels
Label(root, text="URL Shortner", bg="#35fc99", fg="#ff9e3d", font="verdana 22 ").place(x=100, y=10)
Label(root, text="-----------------------------------------------------", bg="#74ec3a", fg="#008080"
            , font="verdana 12 ").place(x=15, y=50)
# Accepting URL as a Input
Label(root, text="Enter URL Here ", bg="#2C3E50", fg="#38DFAB", font="verdana 10 bold"
            , padx=2, pady=2).place(x=9, y=100)
Entry(root, textvariable=url, font="verdana 12", width=30).place(x=10, y=120)
# Creating button to give a call for convert function
Button(root, text="Convert...", bg="#B2D8D8", fg="#550E61", font="verdana 12 "
        , command=convert, relief=GROOVE).place(x=9, y=180)
# Displaying shortened URL
Label(root, text="Shortened URL - Copy & Paste in browser", bg="#2C3E50", fg="#38DFAB"
            , font="verdana 10 bold", padx=2, pady=2).place(x=7, y=250)
Entry(root, textvariable=shorturl, width=35, font="verdana 12").place(x=7, y=270)
# StatusBar - Only for design purpose
statusvar = StringVar()
statusvar.set("©https://aadi-sonwane.github.io/")
Label(root, textvariable=statusvar, relief=GROOVE,  bg="#61fc1d"
            , fg="#2C3E50", width=60).place(x=-1, y=328)
root.mainloop()
