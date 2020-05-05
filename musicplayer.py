from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from pygame import mixer



currentloc=os.system("pwd")

root=Tk()

mixer.init()
root.geometry('480x360')
root.title('Solppam Muziq Kelkkam')

myimg= ImageTk.PhotoImage(Image.open('play.png'))


def onclick():
    root.filename = filedialog.askopenfilename(initialdir =currentloc, title = "Browse the musiz", filetypes=(("mp3","*.mp3"),("all files","*.*")))
    print(root.filename)

    
    mixer.music.load(root.filename)
    
    mixer.music.play()
 

button= Button(root, image= myimg, command= onclick).pack()








root.mainloop()