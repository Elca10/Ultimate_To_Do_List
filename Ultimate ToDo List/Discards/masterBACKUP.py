# import libraries
from datetime import datetime
import time
import numpy as np
import tkinter as tk
import pickle
import pandas as pd
#from tkinterGood import *


###global data, allLists, allItems
##data = []
##allLists = []
##allItems = []
##allCats = []

def initialization():
    global allLists, allItems, allCats
    print('**WARNING** Proceeding will delete all existing data. Are you sure you want to continue?')
    i = int(input('If yes, enter any number. If no, enter anything but a number. ').strip())
    allLists = []
    allItems = []
    allCats = []
    
    with open('allListsPickle.obj', 'wb') as f:
        pickle.dump(allLists, f)
    with open('allItemsPickle.obj', 'wb') as f:
        pickle.dump(allItems, f)
    with open('allCatsPickle.obj', 'wb') as f:
        pickle.dump(allCats, f)


class List():
    def __init__(self, name):
        self.name = name
        tasks = []
        self.tasks = tasks
        sortBy = None
        self.sortBy = sortBy
        self.visible = False
        # add position (on tkinter window) attribute


    def addTask(self, task):
        self.tasks.append(task)
        if self.sortBy != None:
            self.sortList()
        self.updateWindow()         


    def sortByCategory(self):
        '''Sorts the list by categories in alphabetical order. '''
        categories = []
        for task in self.tasks:
            categories.append((task.category.name, task))
        categories = sorted(categories) 
        sortedTasks = [cat[-1] for cat in categories]
        self.tasks = sortedTasks

    def sortByPriority(self):
        '''Sorts the list in order of ascending priority (1 -> 5). '''
        print("SORTED BY PRIORITY")
        priorities = sorted([(task.priority, task) for task in self.tasks])
        sortedTasks = [pri[-1] for pri in priorities]
        self.tasks = sortedTasks
        
    def sortByDue(self):
        '''Sorts the list by due date - MAKE IT MOST PAST TO MOST FUTURE. '''
        dates = sorted([(task.due, task) for task in self.tasks])
        sortedTasks = [dat[-1] for dat in dates]
        self.tasks = sortedTasks

    def sortByName(self):
        '''Sorts the list alphabetically by task. '''
        names = sorted([(t.task, t) for t in self.tasks])
        sortedTasks = [nam[-1] for nam in names]
        self.tasks = sortedTasks

    def sortByCreated(self):
        '''Sorts the list by when the list item was created. MAKE SURE THIS IS RIGHT. '''
        dates = sorted([(task.created, task) for task in self.tasks])
        sortedTasks = [dat[-1] for dat in dates]
        self.tasks = sortedTasks



class Category():
    def __init__(self, name):
        self.name = name

    # self.items using decorator
    #    for item in allItems:

    # IF TIME HAVE A COLOR LIKE TRELLO LABEL        


class Item():
    def __init__(self, task:str):
        self.task = task
        self.created = datetime.now()
        self._list = None
        self.category = None
        self.priority = None
        self.due = None
        self.complete = False
        self.visible = True
        # add attribute using decorator for time completed and complete

##    def setList(self): # print a numbered list that corresponds with list nums
##        global allLists, allItems, allCats
##        print('\nWhat list would you like to add the card to?')
##        for i in range(len(allLists)):
##            print(f'({i+1}) {allLists[i].name}')
##        try:
##            self._list = allLists[int(input('Enter the corresponding number to the list of your choice: '))-1]
##        except:
##            self._list = allLists[int(input('Please enter a valid number: '))-1]

    def setCategory(self):
        global allLists, allItems, allCats
        if len(allCats) == 0:
            cat = Category(input('You first need to create a category. What would you like to call it? '))
            allCats.append(cat)
        print('\nWhat category would you like to put the item under?')
        for i in range(len(allCats)):
            print(f'({i+1}) {allCats[i].name}')
        try:
            self.category = allCats[int(input('Enter the corresponding number to the list of your choice: '))-1]
        except:
            self.category = allCats[int(input('Please enter a valid number: '))-1]
    
    def setPriority(self):
        self.priority = int(input('How high of a priority is your item? ').strip())

    def setDue(self):
        date = input('When is this item due? (M/D/YY) ')
        self.due = date # MAKE THIS A DATETIME OBJECT
        
    def setComplete(self):
        self.complete = True
        self.visible = False

    def showCard(self):
        self.visible = True
        pass



def createList(event=None):
    global question, uI
    print("INSIDE OF CLIST FUNCTION")
    global allLists, allItems, allCats
    print("USER INPUT (uI): ", uI, type(uI))
    uL = uI.get() # get the contents of the entry widget
    print("uL: ", uL)
    uI.delete(0, 'end') # delete the text inside of the entry box
    aList = List(str(uL))
    print(len(allLists))
    allLists.append(aList)
    print(len(allLists))
    question.destroy()
    uI.destroy()

def createListVisual(m):
    global question, uI
    print("INSIDE OF CREATELISTVISUAL FUNCTION")
    question = tk.Label(master=m, text="Enter list name: ", font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)

    
    uI.bind('<Return>', createList, add='+')
    print("FINISHED BINDING")
    
    question.pack(side=tk.TOP)
    uI.pack(side=tk.TOP)

    print("FINISHED PACKING INSIDE OF createListVisual FUNCTION")
    #return uI



def createItem(event=None):
    global question, uI
    global allLists, allItems, allCats
    uL = uI.get()
    uI.delete(0, 'end')
    anItem = Item(str(uL))
    allItems.append(anItem)
    question.destroy()
    uI.destroy()


def setList(event=None):
    global question2, uI2, listTexts
    global allLists, allItems, allCats
    uL = uI2.get()
    uI2.delete(0, 'end')
    try:
        itemList = allLists[int(uL)-1]
        itemList.tasks.append(allItems[-1]) # add the item to the list's tasks
        allItems[-1]._list = itemList

        for l in listTexts:
            l.destroy()
        question2.destroy()
        uI2.destroy()
    except:
        pass

def createItemVisual(m):
    # COMBINE WITH CREATE LIST VISUAL AND MAYBE ADD CREATE CATEOGRY
    # just have a variable for the question and the binded function
    global question, uI
    global question2, uI2, listTexts
    print("INSIDE OF createItemVisual")
    question = tk.Label(master=m, text="Enter item/task: ", font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)
    
    question2 = tk.Label(master=m, text="What list would you like to add the item to? ", font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI2 = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)

    uI.bind('<Return>', createItem, add='+')
    uI2.bind('<Return>', setList, add='+')
    
    question.pack(side=tk.TOP)
    uI.pack(side=tk.LEFT)

    
    print('down here in createItemVisual!')
    # prints the a numbered list of lists (names)
    listTexts = []
    for i in range(len(allLists)):
        l = allLists[i].name
        t = f'({i+1}) {l}'
        LText = tk.Label(master=m, text=t, font=("Arial", 15), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        listTexts.append(LText)
        LText.pack()

    
    question2.pack(side=tk.TOP)
    uI2.pack(side=tk.LEFT)
    print('finished packing in createItemVisual')



    
def sortListVisual2(event=None):
    global listToSort
    global q3, uI3, listTexts1
    global allLists
    uL3 = uI3.get()
    uI3.delete(0, 'end')
    print("BEFORE TRY IN sortListVisua2l")
    try:
        listToSort = allLists[int(uL3)-1]
        print("LIST TO SORT: ", listToSort)
        for l in listTexts1:
            l.destroy()
        q3.destroy()
        uI3.destroy()
    except:
        pass
    print("AFTER EXCEPT IN  sortListVisual2")
    

def sortListAction(event=None):
    

def sortListVisual(m):
    print("INSIDE sortListVisual")
    global allLists, allItems, allCats
    global q3, uI3, listTexts1
    global listToSort
    print("INSIDE SORTLISTVISUAL AFTER GLOBALS")
    q3 = tk.Label(master=m, text='What list would you like to sort?',font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI3 = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)

    # prints the a numbered list of lists (names)
    listTexts1 = []
    for i in range(len(allLists)):
        l = allLists[i].name
        t = f'({i+1}) {l}'
        LText = tk.Label(master=m, text=t, font=("Arial", 15), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        listTexts1.append(LText)
        LText.pack()

    uI3.bind('<Return>', sortListVisual2, add='+')

    q3.pack(side=tk.TOP)
    uI3.pack(side=tk.LEFT)

    print("BEGINNING PART 2 of sortListVisual")

    global q3b, uI3b, sortTexts    
#    print("LIST TO SORT: ", listToSort.name)
    q3b = tk.Label(master=m, text=f'How would you like to sort the list?',font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    print("DONE CREATE q3b")
    uI3b = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)
    
    print("DONE CREATING UI3B")
    # prints the a numbered list of lists (names)
    sortOptions = ['Category', 'Priority', 'Date Due', 'Name', 'Date Created']
#    sortByOptions = ['sortByCategory', 'sortByPriority', 'sortByDue', 'sortByName', 'sortByCreated']
#    sortFunctions = {0:sortByCategory, 1:sortByPriority, 2:sortByDue, 3:sortByName, 4:sortByCreated}
    print("ABOUT TO PRINT SORT OPTIONS in sortListVisual")
    i  = 0
    sortTexts = []
    for s in sortOptions:
        i += 1
        t = f'({i}) {s}'
        print("T IS:", t)
        sText = tk.Label(master=m, text=t, font=("Arial", 15), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        print("sText is made")
        sortTexts.append(sText)
        print("sText is appended")
        sText.pack(side=tk.TOP)
        print("sText is packed")
    print("ABOUT TO BIND uI3B IN sortlistVisual")
    uI3b.bind('<Return>', sortListAction, add='+')
    print("ABOUT OT PACK")
    q3b.pack(side=tk.TOP)
    uI3b.pack(side=tk.LEFT)
    print("FINISHED PACKING. AT THE END OF sortListVisual")




def completeItem(event=None):
    global q4, UI4, itemTexts
    global allLists, allItems, allCats
    uL = UI4.get()
    UI4.delete(0, 'end')
    try:
        item = allItems[int(uL)-1]
        item.setComplete() # marks as complete and makes visible = False
        print('ITEM INFORMATION: ', item.task, item.complete, item.visible)
        for i in itemTexts:
            i.destroy()
        q4.destroy()
        UI4.destroy()
    except:
        pass
        
    

def completeItemVisual(m):
    print("INSIDE OF COMPLETE ITEM VISUAL")
    global q4, UI4
    global allItems
    global itemTexts
    print("completeItemVisual AFTER GLOBAL")
    q4 = tk.Label(master=m, text="What item would you like to mark as complete?  ", font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    UI4 = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)
    print("completeItemVisual AFTER CREATING Q AND UI")
    UI4.bind('<Return>', completeItem, add='+')
    print("completeItemVisual AFTER BIND")
    
    itemTexts = []
    for i in range(len(allItems)):
        if i%2 == 0:
            it1 = allItems[i].task
            t1 =  f"{f'({i+1}) {it1}':<30}"
            it2 = allItems[i+1].task
            t2 = f"{f'({i+2}) {it2}':<30}"
            iText1 = tk.Label(master=m, text=t1+t2, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
            itemTexts.append(iText1)
            iText1.pack(side=tk.TOP)

    print("completeItemVisual AFTER CREATING ITEM LIST")
    
    q4.pack(side=tk.TOP)
    UI4.pack(side=tk.TOP)



def itemInfo():
    global allLists, allItems, allCats
    print('\nWhat item would you like to edit or add to?')
    for i in range(len(allItems)):
        print(f'({i+1}) {allItems[i].task}')
    try:
        editItem = allItems[int(input('Enter the corresponding number to the item of your choice: '))-1]
    except:
        editItem = allItems[int(input('Please enter a valid number: '))-1]

    print(f"\nWhat would you like to change/add to '{editItem.task}'")
    actions = ['List', 'Category', 'Priority','Due Date', 'Complete']
    functions = {0:editItem.setList, 1:editItem.setCategory, 2:editItem.setPriority,
                 3:editItem.setDue, 4:editItem.setComplete}

    for i in range(len(actions)):
        print(f'({i+1}) {actions[i]}')
    try:
        edit = int(input('Enter the corresponding number to the action of your choice: ').strip())-1
    except:
        edit = int(input('Please enter a valid number: ').strip())-1
    functions[edit]()





def moveItem1(event=None):
    global itemToMove
    global q6, ui6, itemTexts
    global allItems
    uL6 = ui6.get()
    ui6.delete(0, 'end')
    try:
        itemToMove = allItems[int(uL6)-1]
        for i in itemTexts:
            i.destroy()
        q6.destroy()
        ui6.destroy()
    except:
        pass


def moveItemVisual(m):
    global allLists, allItems, allCats
    global q6, ui6, itemTexts
    global itemToMove
    q6 = tk.Label(master=m, text='What item would you like to move?', font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    ui6 = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)

    itemTexts = []
    for i in range(len(allItems)):
            if i%2 ==0:
                it1 = allItems[i].task
                t1 = f"{f'({i+1}) {it1}':<30}"
                it2 = allItems[i+1].task
                t2 = f"{f'({i+2}) {it2}':<30}"
                #f'({i+2}) {it2}'
                print(len(t1+t2))
                iText1 = tk.Label(master=m, text=t1+t2, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
                itemTexts.append(iText1)
                iText1.pack(side=tk.TOP)
    ui6.bind('<Return>', moveItem1, add = '+')

    q6.pack(side=tk.TOP)
    ui6.pack(side=tk.LEFT)

    global q6b, ui6b, listTexts
    q6b = tk.Label(master=m, text=f'What list do you want to move the item to?',font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    ui6b = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)

    listTexts = []
    for i in range(len(allLists)):
            if i%2 ==0:
                it1 = allLists[i].task
                t1 = f"{f'({i+1}) {it1}':<30}"
                it2 = allLists[i+1].task
                t2 = f"{f'({i+2}) {it2}':<30}"
                l = tk.Label(master=m, text=t1+t2, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
                listTexts.append(l)
                l.pack(side=tk.TOP)
    ui6b.bind('<Return>', moveItem2, add = '+')
    q6b.pack(side=tk.TOP)
    ui6b.pack(side=tk.LEFT)




def delItem(event=None):
    global allLists, allItems, allCats
    global q7, uI7, itemTexts
    uL = uI7.get()
    uI7.delete(0, 'end')
    print("INSIDE OF DELITEM FUNCTION")
    try:
        
        dItem = allItems[int(uL)-1]
        print('DITEM:', dItem)
        allItems.remove(dItem)
        del dItem
        print("ABOUT TO DESTROY INFO FOR 7")
        for i in itemTexts:
            i.destroy()
        q7.destroy()
        uI7.destroy()
    except:
        pass
    

#f'{"Hi": <16} StackOverflow!'

def delItemVisual(m):
    global q7, uI7, itemTexts
    itemTexts = []
    for i in range(len(allItems)):
        if i%2 ==0:
            it1 = allItems[i].task
            t1 = f"{f'({i+1}) {it1}':<30}"
            it2 = allItems[i+1].task
            t2 = f"{f'({i+2}) {it2}':<30}"
            #f'({i+2}) {it2}'
            print(len(t1+t2))
            iText1 = tk.Label(master=m, text=t1+t2, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
            itemTexts.append(iText1)
            iText1.pack(side=tk.TOP)

            


    q7 = tk.Label(master=m, text='What item would you like to delete?', font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI7 = tk.Entry(master=m, fg='black',bg='white',width=15,bd=3)
    uI7.bind('<Return>', delItem, add='+')

    q7.pack(side=tk.TOP)
    uI7.pack(side=tk.LEFT)



def delList(event=None):
    global q8, uI8, listTexts
    global allLists, allItems, allCats
    uL = uI8.get()
    uI8.delete(0, 'end')
    try:
        delL = allLists[int(uL)-1]
        for item in delL.tasks:
            #allItems.pop(item)
            allItems.remove(item)
            del item
        #allLists.pop(delL)

        allLists.remove(delL)
        del delL
        
        for l in listTexts:
            l.destroy()
        q8.destroy()
        uI8.destroy()
    except:
        pass



def delListVisual(m):
    global q8, uI8, listTexts
    # prints the a numbered list of lists (names)
    listTexts = []
    for i in range(len(allLists)):
        l = allLists[i].name
        t = f'({i+1}) {l}'
        LText = tk.Label(master=m, text=t, font=("Arial", 15), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        listTexts.append(LText)
        LText.pack()

    q8 = tk.Label(master=m, text='What list would you like to delete?', font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI8 = tk.Entry(master=m, fg='black',bg='white',width=15,bd=3)
    uI8.bind('<Return>', delList, add='+')

    q8.pack(side=tk.TOP)
    uI8.pack(side=tk.LEFT)



def createCategory(event=None):
    global question, uI
    global allLists, allItems, allCats
    uL = uI.get() # get the contents of the entry widget
    uI.delete(0, 'end') # delete the text inside of the entry box
    aCat = Category(str(uL))
    allCats.append(aCat)
    question.destroy()
    uI.destroy()

def createCategoryVisual(m):
    global question, uI
    print("INSIDE OF createCategoryVisual FUNCTION")
    question = tk.Label(master=m, text="Enter category name: ", font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)

    
    uI.bind('<Return>', createCategory, add='+')

    
    question.pack(side=tk.TOP)
    uI.pack(side=tk.TOP)




def userInput(choice,m):
    print('INSIDE userInput ON master')
    global allLists, allItems, allCats
    # DONE: 1, 2, 3, 4, 7, 8, 9
    # TO DO: 5, 6
    print("AFTER GLOBAL userInput")
    functions = {1:createListVisual, 2:createItemVisual, 3:sortListVisual, 4:completeItemVisual, 5:itemInfo,
                 6:moveItemVisual, 7:delItemVisual, 8:delListVisual, 9:createCategoryVisual}
    print("AFTER DICTIONARY userInput")
    functions[choice](m)
    print("DONE WITH userInput")



def save(leftW, toDelete):
    global allLists, allItems, allCats
   # allListsDF = pd.DataFrame(allLists)
    #allListsDF.to_pickle('allListsPickle.pkl')
    toDelete.destroy()
    with open('allListsPickle.obj', 'wb') as f:
        pickle.dump(allLists, f)
    with open('allItemsPickle.obj', 'wb') as f:
        pickle.dump(allItems, f)
    with open('allCatsPickle.obj', 'wb') as f:
        pickle.dump(allCats, f)

#    global saved
    print("INSIDE OF save")
    t = f'Last saved at {datetime.now().strftime("%H:%M:%S")}'
    saved = tk.Label(master=leftW, text=t, font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    saved.pack(side=tk.TOP)
    print("DONE PACKING IN save")
    return saved
            




def updateDisplay():
    # maybe put this function in the tkinter function
    pass


def intro():
    global allLists, allItems, allCats
    list1 = List(input("\nLet's start by making a list. What would you like to call it? "))
    allLists.append(list1)
    task1 = Item(input("Next let's make a list item, or task. For example: write code. Enter yours here: "))
    allItems.append(task1)
    task1.setList()

def load(): # LOAD UP EXISTING INFO
    global allLists, allItems, allCats
    # (outside of function so that the lists are in the global scope)
    with open('allListsPickle.obj', 'rb') as f:
        allLists = pickle.load(f)
    with open('allItemsPickle.obj', 'rb') as f:
        allItems = pickle.load(f)
        # list of objects
    with open('allCatsPickle.obj', 'rb') as f:
        allCats = pickle.load(f)
    return allLists, allItems, allCats


def main():
    global allLists, allItems, allCats
    allLists, allItems, allCats = load()
    intro()
    while True:
        userInputOLD()
        print('\nLists:')
        for l in allLists:
            print(l.name, len(l.tasks))
        print('\nItems:')
        for t in allItems:
            print(t.task)

        #data.append(allLists)
        #data.append(allItems)
        #data.append(allCats)
        save()

if __name__ == '__main__':
    main()


# IF TIME MAKE A TUTORIAL INTRO, OR JUST BASIC "START BY MAKING A LIST" then next window


#### TO DO ###
# --- High priority ---
# - add docstrings and comments
# - make the lists show up on the left
# - Finish some of the user input actions visual stuff
# - rename question and uI vars
# - add entry boxes and questions to frames

# --- Low priority ---
# - figure out how to deal with lists that are longer than the screen (arbitrary list lengths)
#      maybe 'show more' button? or multiple windows? like a button that will switch it all
#      or maybe have it just move to the right side of the left side (columns)
#      and then ask user which list they would like to display? - have each on it's own window
# - finish all user input actions visual stuff





######################
## USING DECORATORS ##
######################


##import math
##class Circle:
##    def __init__(self, radius):
##        self.radius = radius
##    
##    def circumference(self):
##        return 2*math.pi*self.radius
##    
##    @property
##    def area(self):
##        return math.pi*self.radius**2
##    
##    @area.setter
##    def area(self, area):
##        self.radius = math.sqrt(area/math.pi)
##    
##    def __str__(self):
##        return f"Circle with radius {self.radius} and area {self.area:0.3f}."

##c = Circle(2)
##print(c.area)
##c.area = 10
##print(c)
