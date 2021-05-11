import random
import tkinter
import os
from tkinter import *
import tkinter.font as font
from tkinter import messagebox 
import numpy as np
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
import os, random
# loading Python Imaging Library
from PIL import ImageTk, Image
# To get the dialog box to open when required 
from tkinter import filedialog
from tensorflow.keras.preprocessing import image
from tensorflow import keras
result = -1
global x

def fun_predict():
    global Result_l
    img_width, img_height = 150, 150
    img = image.load_img(x, target_size = (img_width, img_height))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis = 0)

    result = model.predict(img)
    if result == 1 :
        result = "Result : Pneumonia"
    elif result == 0 :
        result = "Result : Normal"
    else:
        result = "Result : Unpredicted"
    myFont = font.Font(size=10)
    win.update()
    Result_l['text'] = result
    Result_l['font']=myFont
    Result_l.place(x=560,y=400)
    win.mainloop()

def open_img():
    global x, Result_l
    # Select the Imagename  from a folder 
    x = openfilename()
    Result_l['text'] = " "
    # opens the image
    img = Image.open(x)
      
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.ANTIALIAS)
  
    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)
   
    # create a label
    panel = Label(win, image = img)
      
    # set the image as img 
    panel.image = img
    panel.place(x=460,y=100)

def openfilename():
  
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title ='"pen')
    return filename

win = Tk()
win.geometry("1200x1200")
win.configure(bg='black')
win.title("ML")
myFont = font.Font(size=20)
Result_l = Label(win, text=" ")

model = keras.models.load_model("my_model1")

btn = Button(win, text ='open image', command = lambda:open_img())
btn['font']=myFont
btn.place(x=450,y=440)

pre_b = Button(win, text ='predict', command = lambda:fun_predict())
pre_b['font']=myFont
pre_b.place(x=650,y=440)

win.mainloop()