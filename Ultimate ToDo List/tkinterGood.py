# import libraries and master file
from datetime import datetime
import time
import numpy as np
import tkinter as tk
import pickle
import pandas as pd
# the star allows all functions to be referenced as if they were local in this file
from master import * 

global allLists, allItems, allCats

def makeWindow():
    # Makes the window, adds a title
    global window, width, height
    window = tk.Tk()
    window.title("Ultimate To Do List")

    # makes it fullscreen
    width= window.winfo_screenwidth()               
    height= window.winfo_screenheight()               
    window.geometry("%dx%d" % (width, height))


def backgroundSetup():
    ''' Sets up the permanent background of the window, including the instructions/actions. '''
    global window, width, height
    global background
    global leftB, leftW, leftTitle
    global rightB, rightW, rightTitle
    
    # SETTING UP THE BACKGROUND
    background = tk.Frame(master=window, bg="white", bd=10, height = 2000, width= 4000)

    # LEFT SIDE FRAME
    leftB = tk.Frame(master=background, bg='black', bd=10, height=height, width=width/2)
    leftW = tk.Frame(master=leftB, bg='white', height = height-10, width = width/2 - 10)

    leftB.pack(padx=5, pady=5, side=tk.LEFT)
    leftW.pack()
    leftW.pack_propagate(False)

    # RIGHT SIDE FRAME
    rightB = tk.Frame(master=background, bg='black', bd=10, height=height, width=width/2)
    rightW = tk.Frame(master=rightB, bg='white', height = height-10, width = width/2 -10)

    rightB.pack(padx=5, pady=5, side=tk.LEFT)
    rightW.pack()
    rightW.pack_propagate(False)


    # LEFT SIDE (LISTS TITLE)
    leftTitle = tk.Label(master=leftW, text='LISTS',fg = 'black', font=("Arial", 15), bg='white')
    leftTitle.pack()

    # RIGHT SIDE (USER INPUT ACTION OPTIONS)
    rightTitle = tk.Label(master=rightW, text='What would you like to do?',fg = 'black', font=("Arial", 15), anchor=tk.W, bg = 'white',width=100,padx=10,pady=5)
    rightTitle.pack()

    actions = ['(1) Create a list', '(2) Create an item', '(3) Sort a list', '(4) Mark item as complete', '(5) Move item to a different list',
               '(6) Delete item', '(7) Delete list (and items in list)', '(8) Create a category', '(9) Add an item to a category']

    actionTexts = []
    for a in actions:
        aText = tk.Label(master=rightW, text=a, font=("Arial", 15), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        actionTexts.append(aText)
        aText.pack()


def actionVisual():
    ''' Displays question and user input box for choosing an action to make. '''
    global inputFrame1, actionQuestion, userAction
    global rightW

    # Adds the q and entry box to a frame so they are on the same line
    inputFrame1 = tk.Frame(master=rightW, bg='white', height = 10, width = 500)
    inputFrame1.pack(side=tk.TOP)
    q = 'Enter the corresponding number of the action you would like to take: '
    actionQuestion = tk.Label(master=inputFrame1, text=q,font=("Arial", 15), fg="black",
                              bg='white', width = 54, anchor=tk.W, padx=10)
    actionQuestion.pack(side=tk.LEFT,pady=10)
    userAction = tk.Entry(master=inputFrame1, fg="black",bg='white', width=6,font=("Arial", 15), bd=3)


    # bind enter key (called return in tkinter) to the entry widget and
    # connect it to the action2 function
    userAction.bind('<Return>', action2)

    userAction.pack(side=tk.LEFT)
    inputFrame1.pack()


def action2(event=None):
    ''' Sets off the chain of functions for making an action, and saves data. '''
    global inputFrame1, actionQuestion, userAction, uI
    global rightW, leftW
    global savedMsgs
    userActionChoice = userAction.get() # get the contents of the entry widget
    userAction.delete(0, 'end') # empties entry box

    # only excepts valid input (numbers 1-9)
    try:
        savedMsgs.append(save(leftW, savedMsgs[-1]))
        userActionChoice = int(userActionChoice)
        if userActionChoice <= 9 and userActionChoice >= 0:
            # calls the userInput function (see master.py)
            userInput(userActionChoice,rightW,leftW)
    # otherwise does nothing more
    except:
        pass


def finalPack():
    '''Packs all main frames (finals step for displaying visuals) '''
    global background, window
    background.pack()
    background.propagate(0) # user can resize the window
    window.mainloop()


def tkinterMain():
    ''' controls the flow of the program by calling primary functions in the correct order'''
    # no while loop is needed for the program to continue running, as later functions
    #   will always be waiting for input
    
    global allLists, allItems, allCats
    #initialization()   # when this is uncommented, all user data will be erased
    load()
    makeWindow()
    backgroundSetup()

    # initial saved message
    global savedMsgs
    t = f'Last saved at {datetime.now().strftime("%H:%M:%S")}'
    saved1 = tk.Label(master=leftW, text=t, font=("Arial", 15), fg="black", bg="white",
                      anchor=tk.W, padx=10, width=45)
    savedMsgs = [saved1]
    
    actionVisual()
    leftSide(leftW)
    finalPack()

# calls the ultimate main function (so the code will start when this file is run)
tkinterMain()
