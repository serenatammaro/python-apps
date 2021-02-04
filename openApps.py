
#!/bin/python
# errno13
import tkinter as tk
from tkinter import filedialog, Text
import subprocess
import os
from tkmacosx import Button
from subprocess import call


root = tk.Tk()
apps = []

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("Windows: executables", "*.exe"),("all files", "*.*"), ("OsX: applications", "*.app")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        subprocess.call([app])
        


canvas = tk.Canvas(root, height=600, width=700, bg="#263D42")
canvas.pack() 

frame = tk.Frame(bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = Button(root, text="Open File", padx=10, 
                    pady=5, fg="green", bg="black", command=addApp)
openFile.pack()


runApps = tk.Button(root, text="Run Apps", padx=10, 
                    pady=5, fg="green", bg="black", command=runApps)
runApps.pack()

root.mainloop()



