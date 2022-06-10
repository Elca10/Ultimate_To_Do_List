import tkinter as tk

window = tk.Tk()
window.title("Ultimate To Do List")

# makes it fullscreen
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("%dx%d" % (width, height))


'''
BASIC WIDGETS:
tk.Label
tk.Button
tk.Entry
tk.Text
tk.Frame

Later: look into themed widgets in the tkinter.tkk module
'''

# SETTING UP THE BACKGROUND
background = tk.Frame(master=window, bg="white", bd=10, height = 2000, width= 4000)

leftB = tk.Frame(master=background, bg='black', bd=10, height=height, width=width/2)
leftW = tk.Frame(master=leftB, bg='white', height = height-10, width = width/2 - 10)

leftB.pack(padx=5, pady=5, side=tk.LEFT)
leftW.pack()
leftW.pack_propagate(False)

rightB = tk.Frame(master=background, bg='black', bd=10, height=height, width=width/2)
rightW = tk.Frame(master=rightB, bg='white', height = height-10, width = width/2 -10)

rightB.pack(padx=5, pady=5, side=tk.LEFT)
rightW.pack()
rightW.pack_propagate(False)


# LEFT SIDE (LISTS)
leftTitle = tk.Label(master=leftW, text='LISTS',fg = 'black', font=("Arial", 15), bg='white').grid(row=0,column=0)


# RIGHT SIDE (USER INPUT)
rightTitle = tk.Label(master=rightW, text='What would you like to do?',fg = 'black', font=("Arial", 15), anchor=tk.W, bg = 'white',width=100,padx=10,pady=5).grid(row=1, column=0)
actions = ['(1) Create a list', '(2) Create an item', '(3) Sort a list', '(4) Mark item as complete', '(5) Add information to an item',
           '(6) Move item to a different list', '(7) Delete item', '(8) Delete list (and items in list)', '(9) Create a category']

##
##actionTexts = []
##for a in actions:
##    aText = tk.Label(master=rightW, text=a, font=("Arial", 15), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
##    actionTexts.append(aText)
##    aText.pack()
###actions = '(1) Create a list\n(2) Create an item\n(3) Sort a list\n(4) Mark item as complete\n(5) Add information to an item\n(6) Move item to a different list\n(7) Delete item\n(8) Delete list (and items in list)\n(9) Create a category'
###rightInfo = tk.Label(master=rightW, text=actions, font=("Arial", 15), fg="black", width = 100, anchor=tk.W)
###rightInfo.pack()
### wraplength=35
##
##inputFrame1 = tk.Frame(master=rightW, bg='yellow', height = 500, width = 500)
##
##actionQuestion = tk.Label(master=inputFrame1, text='Enter the corresponding number of the action you would like to take: ',font=("Arial", 15), fg="black", width = 100, anchor=tk.W, padx=10)
##actionQuestion.pack(side=tk.RIGHT)
##
##userAction = tk.Entry(master=inputFrame1, fg="black",bg='white', width=6,font=("Arial", 15))
##userAction.pack(side=tk.RIGHT)
##inputFrame1.pack()
##
##
###button = tk.Button(master=rightW, text="Start here", width=10, height=2, bg="red",fg = 'white',cursor='dot')
###button.pack()
##
###name = tk.Entry(master=rightW, fg="white", bg="black", width = 20)
###name.pack()
##
##background.pack()
##background.propagate(0) # user can resize the window
##
##
##window.mainloop()
##
##
