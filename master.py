# import libraries
from datetime import datetime
import time
import numpy as np
import tkinter as tk
import pickle
import pandas as pd


def initialization():
    '''Resets all user data by writing empty lists to the files storing the data.'''
    global allLists, allItems, allCats

    # will create an error that stops the code
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

    def sortByCategory(self):
        '''Sorts the list by categories in alphabetical order. '''
        categories = []
        for task in self.tasks:
            categories.append((task.category.name, task))
        categories = sorted(categories) 
        sortedTasks = [cat[-1] for cat in categories]
        self.tasks = sortedTasks

    def sortByPriority(self):
        '''Sorts the list in order of ascending priority.'''
        print("SORTED BY PRIORITY")
        priorities = sorted([(task.priority, task) for task in self.tasks])
        sortedTasks = [pri[-1] for pri in priorities]
        self.tasks = sortedTasks
        
    def sortByDue(self):
        '''Sorts the list by due date.'''
        dates = sorted([(task.due, task) for task in self.tasks])
        sortedTasks = [dat[-1] for dat in dates]
        self.tasks = sortedTasks

    def sortByName(self):
        '''Sorts the list by name. '''
        names = sorted([(t.task, t) for t in self.tasks])
        sortedTasks = [nam[-1] for nam in names]
        self.tasks = sortedTasks

    def sortByCreated(self):
        '''Sorts the list by when the list item was created.'''
        dates = sorted([(task.created, task) for task in self.tasks])
        sortedTasks = [dat[-1] for dat in dates]
        self.tasks = sortedTasks

    def addTask(self, task):
        '''Adds a task to the list.'''
        self.tasks.append(task)
        # resorts the list
        if self.sortBy != None:
            self.sortList()


class Category():
    def __init__(self, name):
        self.name = name


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

    def setComplete(self):
        ''' When an item is complete, it will not appear on the visual lists. '''
        self.complete = True
        self.visible = False

def createList(event=None):
    ''' Creates a list based on input into createListVisual '''
    global question, uI
    global allLists, allItems, allCats
    
    uL = uI.get() # get the contents of the entry widget
    uI.delete(0, 'end') # delete the text inside of the entry box

    # makes a list object and adds to the list of all Lists
    aList = List(str(uL))
    allLists.append(aList)

    # deletes the question and entry box
    question.destroy()
    uI.destroy()

def createListVisual(m):
    ''' Question and entry box for (1) '''
    global question, uI
    question = tk.Label(master=m, text="Enter list name: ", font=("Arial", 15), fg="black",
                        bg="white", anchor=tk.W, padx=10, width=45)
    uI = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)
    # calls 'createList' when return is pressed in the entry box
    uI.bind('<Return>', createList, add='+')

    # displays the question and entry box
    question.pack(side=tk.TOP)
    uI.pack(side=tk.TOP)


def createItem(event=None):
    ''' Creates an item. '''
    global question, uI
    global allLists, allItems, allCats
    
    # retrieves input
    uL = uI.get()
    uI.delete(0, 'end')
    
    # creates and saves item
    anItem = Item(str(uL))
    allItems.append(anItem)
    
    # deletes question and entry box
    question.destroy()
    uI.destroy()


def setList(event=None):
    ''' Sets the list for the newly created item. '''
    global question2, uI2, listTexts
    global allLists, allItems, allCats

    # retrieves input
    uL = uI2.get()
    uI2.delete(0, 'end')
    # try/except block will only use valid input
    try:
        # obtains the list the user wants
        itemList = allLists[int(uL)-1]
        # adds the item to the list's tasks
        itemList.tasks.append(allItems[-1])
        # sets the item's list
        allItems[-1]._list = itemList

        # deletes the text and entry box on the right
        for l in listTexts:
            l.destroy()
        question2.destroy()
        uI2.destroy()
    except:
        pass

def createItemVisual(m):
    ''' Creates the visuals for action (2) '''
    global question, uI
    global question2, uI2, listTexts
    # creates question and entry box for item name
    question = tk.Label(master=m, text="Enter item/task: ", font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)

    # creates a second question and entry box pair for item list
    question2 = tk.Label(master=m, text="What list would you like to add the item to? ", font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI2 = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)

    # when return key is pressed in an entry box, the corresponding function is called
    uI.bind('<Return>', createItem, add='+')
    uI2.bind('<Return>', setList, add='+')

    # displays first q/entry pair
    question.pack(side=tk.TOP)
    uI.pack(side=tk.TOP)

    # creates and displays the a numbered list of list names
    listTexts = []
    for i in range(len(allLists)):
        l = allLists[i].name
        t = f'({i+1}) {l}'
        LText = tk.Label(master=m, text=t, font=("Arial", 15), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        # saves each tkinter label in a list for later deletion
        listTexts.append(LText)
        LText.pack()

    # displays second q/entry pair
    question2.pack(side=tk.TOP)
    uI2.pack(side=tk.TOP)

    
def sortListVisual2(event=None):
    ''' Obtains the list the user would like to sort '''
    global listToSort
    global q3, uI3, listTexts1
    global allLists
    uL3 = uI3.get()
    uI3.delete(0, 'end')
    try:
        listToSort = allLists[int(uL3)-1]
        for l in listTexts1:
            l.destroy()
        q3.destroy()
        uI3.destroy()
    except:
        pass
    

def sortListAction(event=None):
    ''' Sorts the list based on user input. '''
    global listToSort
    global q3b, uI3b, sortTexts
    global allLists
    sortMethod = uI3b.get()
    uI3b.delete(0, 'end')
    # will only except valid input
    try:
        sortOptions = ['Category', 'Priority', 'Date Due', 'Name', 'Date Created']
        sortByOptions = ['sortByCategory', 'sortByPriority', 'sortByDue', 'sortByName', 'sortByCreated']
        sortFunctions = {0:listToSort.sortByCategory, 1:listToSort.sortByPriority, 2:listToSort.sortByDue, 3:listToSort.sortByName, 4:listToSort.sortByCreated}
        listToSort.sortBy = sortOptions[int(sortMethod)-1]
        sortFunctions[int(sortMethod)-1]() # calls the corresponding sort function
        for s in sortTexts:
            s.destroy()
        q3b.destroy()
        uI3b.destroy()
    except:
        pass

def sortListVisual(m):
    ''' Creates the visuals and user input boxes for action (3). '''
    global allLists, allItems, allCats

    # PART 1 of SORTING A LIST (choosing list)
    global q3, uI3, listTexts1
    global listToSort
    
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
    uI3.pack(side=tk.TOP)

    # PART 2 OF SORTING A LIST (choosing sort method)
    global q3b, uI3b, sortTexts    

    q3b = tk.Label(master=m, text=f'How would you like to sort the list?',font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI3b = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)
    
    # prints the a numbered list of lists (names)
    sortOptions = ['Category', 'Priority', 'Date Due', 'Name', 'Date Created']
    i  = 0
    sortTexts = []
    for s in sortOptions:
        i += 1
        t = f'({i}) {s}'
        sText = tk.Label(master=m, text=t, font=("Arial", 15), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        sortTexts.append(sText)
        sText.pack(side=tk.TOP)
        
    uI3b.bind('<Return>', sortListAction, add='+')
    
    q3b.pack(side=tk.TOP)
    uI3b.pack(side=tk.TOP)


def completeItem(event=None):
    ''' Marks an item as complete. '''
    global q4, UI4, itemTexts
    global allLists, allItems, allCats
    uL = UI4.get()
    UI4.delete(0, 'end')
    # again, only excepts valid answer
    try:
        item = allItems[int(uL)-1]
        item.setComplete() # marks as complete and makes visible = False
        for i in itemTexts:
            i.destroy()
        q4.destroy()
        UI4.destroy()
    except:
        pass
        
    

def completeItemVisual(m):
    ''' Visuals and user input for action (4) '''
    global q4, UI4
    global allItems
    global itemTexts
    
    q4 = tk.Label(master=m, text="What item would you like to mark as complete?  ", font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    UI4 = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)
    
    UI4.bind('<Return>', completeItem, add='+')

    # displays a list of all items
    itemTexts = []
    # loops through allItems and prints in pairs of items
    for i in range(len(allItems)-1):
        if i%2 == 0:
            it1 = allItems[i].task
            t1 =  f"{f'({i+1}) {it1}':<30}"
            it2 = allItems[i+1].task
            t2 = f"{f'({i+2}) {it2}':<30}"
            iText1 = tk.Label(master=m, text=t1+t2, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
            itemTexts.append(iText1)
            iText1.pack(side=tk.TOP)
    # if there's an odd number of items, prints the last item
    if len(allItems)%2 != 0:
        it = allItems[-1].task
        t = f"{f'({0+1}) {it1}':<30}"
        iText1 = tk.Label(master=m, text=t, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        itemTexts.append(iText1)
        iText1.pack(side=tk.TOP)
    
    q4.pack(side=tk.TOP)
    UI4.pack(side=tk.TOP)


def moveItem2(event=None):
    ''' Moves item to list of user's choice. '''
    global itemToMove
    global q6b, ui6b, listTexts
    global allLists, allItems
    listDest = ui6b.get()
    ui6b.delete(0, 'end')
    try:
        oldList = itemToMove._list
        newList = allLists[int(listDest)-1]
        # removes item from the old list's tasks
        oldList.tasks.remove(itemToMove)
        itemToMove._list = newList
        # and adds the item to the new list's tasks
        newList.tasks.append(itemToMove)

        if newList.sortBy != None:
            sortOptions = ['Category', 'Priority', 'Date Due', 'Name', 'Date Created']
            sortByOptions = ['sortByCategory', 'sortByPriority', 'sortByDue', 'sortByName', 'sortByCreated']
            sortFunctions = {0:newList.sortByCategory, 1:newList.sortByPriority, 2:newList.sortByDue, 3:newList.sortByName, 4:newList.sortByCreated}
            i = sortOptions.index(newList.sortBy)
            print("ABOUT TO SORT", newList.sortBy, i)
            sortFunctions[i]() # calls the corresponding sort function

        
        for s in listTexts:
            s.destroy()
        q6b.destroy()
        ui6b.destroy()
    except:
        pass


def moveItem1(event=None):
    ''' Obtains item to move based on user input '''
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
    ''' Displays the visuals and user input for action (5) '''
    global allLists, allItems, allCats

    # PART 1 (Selecting item)
    global q6, ui6, itemTexts
    global itemToMove
    q6 = tk.Label(master=m, text='What item would you like to move?', font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    ui6 = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)

    itemTexts = []
    # loops through all items and displays them
    for i in range(len(allItems)-1):
        if i%2 ==0:
            it1 = allItems[i].task
            t1 = f"{f'({i+1}) {it1}':<30}"
            it2 = allItems[i+1].task
            t2 = f"{f'({i+2}) {it2}':<30}"
            iText1 = tk.Label(master=m, text=t1+t2, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
            itemTexts.append(iText1)
            iText1.pack(side=tk.TOP)
    # if odd # of items, displays remaining one
    if len(allItems)%2 != 0:
        it = allItems[-1].task
        t = f"{f'({len(allItems)}) {it1}':<30}"
        iText1 = tk.Label(master=m, text=t, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        itemTexts.append(iText1)
        iText1.pack(side=tk.TOP)

    ui6.bind('<Return>', moveItem1, add = '+')

    q6.pack(side=tk.TOP)
    ui6.pack(side=tk.TOP)

    # PART 2 (Selecting new list for item)
    global q6b, ui6b, listTexts
    q6b = tk.Label(master=m, text=f'What list do you want to move the item to?',font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    ui6b = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)
    listTexts = []

    for i in range(len(allLists)-1):
        if i%2 ==0:
            it1 = allLists[i].name
            t1 = f"{f'({i+1}) {it1}':<30}"
            it2 = allLists[i+1].name
            t2 = f"{f'({i+2}) {it2}':<30}"
            l = tk.Label(master=m, text=t1+t2, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
            listTexts.append(l)
            l.pack(side=tk.TOP)
    if len(allItems)%2 != 0:
        it = allLists[-1].task
        t = f"{f'({len(allLists)}) {it1}':<30}"
        iText1 = tk.Label(master=m, text=t, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        listTexts.append(iText1)
        iText1.pack(side=tk.TOP)
        
    ui6b.bind('<Return>', moveItem2, add = '+')
    
    q6b.pack(side=tk.TOP)
    ui6b.pack(side=tk.TOP)



def delItem(event=None):
    global allLists, allItems, allCats
    global q7, uI7, itemTexts
    uL = uI7.get()
    uI7.delete(0, 'end')
    try:
        dItem = allItems[int(uL)-1]
        # deletes item from list
        dItem._list.tasks.remove(dItem)
        # deletes item from list of allItems
        allItems.remove(dItem)
        del dItem
        for i in itemTexts:
            i.destroy()
        q7.destroy()
        uI7.destroy()
    except:
        pass
    
def delItemVisual(m):
    ''' Displays the visuals and user input boxes for action (6) '''
    global q7, uI7, itemTexts
    
    itemTexts = []
    for i in range(len(allItems)-1):
        if i%2 ==0:
            it1 = allItems[i].task
            t1 = f"{f'({i+1}) {it1}':<30}"
            it2 = allItems[i+1].task
            t2 = f"{f'({i+2}) {it2}':<30}"
            #f'({i+2}) {it2}'
            iText1 = tk.Label(master=m, text=t1+t2, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
            itemTexts.append(iText1)
            iText1.pack(side=tk.TOP)
    if len(allItems)%2 != 0:
        it = allItems[-1].task
        t = f"{f'({len(allItems)}) {it1}':<30}"
        iText1 = tk.Label(master=m, text=t, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        itemTexts.append(iText1)
        iText1.pack(side=tk.TOP)

    q7 = tk.Label(master=m, text='What item would you like to delete?', font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI7 = tk.Entry(master=m, fg='black',bg='white',width=15,bd=3)
    uI7.bind('<Return>', delItem, add='+')
    q7.pack(side=tk.TOP)
    uI7.pack(side=tk.TOP)


def delList(event=None):
    ''' Deletes a list and the items in it. '''
    global q8, uI8, listTexts8
    global allLists, allItems, allCats

    uL = uI8.get()
    uI8.delete(0, 'end')

    try:
        # deletes all the items in the list
        delL = allLists[int(uL)-1]
        for item in delL.tasks:
            allItems.remove(item)
            del item
        # then deletes the list
        allLists.remove(delL)
        del delL
        
        for l in listTexts8:
            l.destroy()
        q8.destroy()
        uI8.destroy()
    except:
        pass


def delListVisual(m):
    ''' Displays visuals and user input boxes for action (7). '''
    global q8, uI8, listTexts8
    # prints the a numbered list of lists (names)
    listTexts8 = []
    for i in range(len(allLists)):
        l = allLists[i].name
        t = f'({i+1}) {l}'
        LText = tk.Label(master=m, text=t, font=("Arial", 15), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        listTexts8.append(LText)
        LText.pack()

    q8 = tk.Label(master=m, text='What list would you like to delete?', font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI8 = tk.Entry(master=m, fg='black',bg='white',width=15,bd=3)
    uI8.bind('<Return>', delList, add='+')

    q8.pack(side=tk.TOP)
    uI8.pack(side=tk.TOP)


def createCategory(event=None):
    ''' Creates a category based on user input. '''
    global question, uI
    global allLists, allItems, allCats
    uL = uI.get() # get the contents of the entry widget
    uI.delete(0, 'end') # delete the text inside of the entry box
    aCat = Category(str(uL))
    allCats.append(aCat)
    question.destroy()
    uI.destroy()

def createCategoryVisual(m):
    ''' Displays visuals and entry box for action (8). '''
    global question, uI
    question = tk.Label(master=m, text="Enter category name: ", font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    uI = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)

    uI.bind('<Return>', createCategory, add='+')
    
    question.pack(side=tk.TOP)
    uI.pack(side=tk.TOP)


def itemCat2(event=None):
    ''' Sets item's category. '''
    global itemToCat
    global q9b, ui9b, catTexts
    global allLists, allItems, allCats
    catDest = ui9b.get()
    ui9b.delete(0, 'end')
    try:
        itemToCat.category = allCats[int(catDest)-1]
        for s in catTexts:
            s.destroy()
        q9b.destroy()
        ui9b.destroy()
    except:
        pass


def itemCat1(event=None):
    ''' Gets item based on user input. '''
    global itemToCat
    global q9, ui9, itemTexts
    global allItems
    uL9 = ui9.get()
    ui9.delete(0, 'end')
    try:
        itemToCat = allItems[int(uL9)-1]
        for i in itemTexts:
            i.destroy()
        q9.destroy()
        ui9.destroy()
    except:
        pass


def itemCategoryVisual(m):
    ''' Displays visuals and entry box for action (9). '''
    global allLists, allItems, allCats

    # PART 1 (Item to set category for)
    global q9, ui9, itemTexts
    global itemToCat
    
    q9 = tk.Label(master=m, text='What item would you like to set a category for?', font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    ui9 = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)

    itemTexts = []
    for i in range(len(allItems)-1):
        if i%2 ==0:
            it1 = allItems[i].task
            t1 = f"{f'({i+1}) {it1}':<30}"
            it2 = allItems[i+1].task
            t2 = f"{f'({i+2}) {it2}':<30}"
            #f'({i+2}) {it2}'
            iText1 = tk.Label(master=m, text=t1+t2, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
            itemTexts.append(iText1)
            iText1.pack(side=tk.TOP)
    if len(allItems)%2 != 0:
        it = allItems[-1].task
        t = f"{f'({len(allItems)}) {it1}':<30}"
        iText1 = tk.Label(master=m, text=t, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        itemTexts.append(iText1)
        iText1.pack(side=tk.TOP)
        
    ui9.bind('<Return>', itemCat1, add = '+')

    q9.pack(side=tk.TOP)
    ui9.pack(side=tk.TOP)

    # PART 2 (Item's new category)
    global q9b, ui9b, catTexts
    q9b = tk.Label(master=m, text=f'What category do you want to put the item under?',font=("Arial", 15), fg="black", bg="white", anchor=tk.W, padx=10, width=45)
    ui9b = tk.Entry(master=m, fg='black', bg='white', width=15, bd=3)
    
    catTexts = []
    for i in range(len(allCats)-1):
        if i%2 ==0:
            it1 = allCats[i].name
            t1 = f"{f'({i+1}) {it1}':<30}"
            it2 = allCats[i+1].name
            t2 = f"{f'({i+2}) {it2}':<30}"
            l = tk.Label(master=m, text=t1+t2, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
            catTexts.append(l)
            l.pack(side=tk.TOP)
    if len(allCats)%2 != 0:
        it = allCats[-1].task
        t = f"{f'({len(allCats)}) {it1}':<30}"
        iText1 = tk.Label(master=m, text=t, font=("Courier", 13), fg="black", width = 100, anchor=tk.W, padx=25,bg='white')
        catTexts.append(iText1)
        iText1.pack(side=tk.TOP)
            
    ui9b.bind('<Return>', itemCat2, add = '+')
    
    q9b.pack(side=tk.TOP)
    ui9b.pack(side=tk.TOP)


def userInput(choice,m,leftW):
    ''' Calls the corresponding function based off of what action the user would like to make. '''
    # this is one of the main functions that controls the flow of the code
    global allLists, allItems, allCats
    # a dictionary of the action numbers and their corresponding functions
    functions = {1:createListVisual, 2:createItemVisual, 3:sortListVisual, 4:completeItemVisual, 5:moveItemVisual,
                 6:delItemVisual, 7:delListVisual, 8:createCategoryVisual, 9:itemCategoryVisual}
    # calls the function (m is the 'rightW' variable, making it so all text displays on the right side
    functions[choice](m)
    # updates the left side (the visual lists)
    leftSide(leftW)



def save(leftW, toDelete):
    ''' Saves all current data and lets user know when data was last saved. '''
    global allLists, allItems, allCats
    # deletes the last 'last saved' message
    toDelete.destroy()
    # saves all existing data
    with open('allListsPickle.obj', 'wb') as f:
        pickle.dump(allLists, f)
    with open('allItemsPickle.obj', 'wb') as f:
        pickle.dump(allItems, f)
    with open('allCatsPickle.obj', 'wb') as f:
        pickle.dump(allCats, f)

    # Displays 'last saved at X' message
    t = f'Last saved at {datetime.now().strftime("%H:%M:%S")}'
    saved = tk.Label(master=leftW, text=t, font=("Arial", 15), fg="black", bg="white",
                     anchor=tk.CENTER, padx=10, width=45)
    saved.pack(side=tk.TOP)

    # returns the saved msg so that it can be deleted when this function is called again
    # (a cycle of 'saved' --> 'toDelete' + new 'saved' ...)
    return saved


def leftSide(m):
    ''' Maintains an up-to-date visual display of the lists on the left side of the window. '''
    global allLists, allItems, allCats
    global listFrameBorders, listFrames
    global listNames, listSubtitle
    global itemNames, itemCats

    # destroys existing visuals, if any
    try:
        for a in listFrameBorders:
            a.destroy()
        for b in listFrames:
            a.destroy()
        for c in listNames:
            c.destroy()
        for d in itemNames:
            d.destroy()
    # otherwise, creates new lists (if this function has not been run before)
    except:
        listFrameBorders = []
        listFrames = []
        listNames = []
        itemNames = []
        itemCats = []

    # Loops through all lists 
    for i in range(len(allLists)):
        # Creates the gray border and list name (the sizes of each is dependent on the # of lists)
        listFrameBorder = tk.Frame(master=m, bg='lightgray', height = 725, width = ((700/len(allLists))-15))
        listFrame = tk.Frame(master=listFrameBorder, bg='white', height = 700, width=((700/len(allLists))-25))
        listName = tk.Label(master=listFrame, bg='lightgray', text=allLists[i].name, font=("Arial", 15), wraplength=((700/len(allLists))-30))

        listName.pack(side=tk.TOP, padx=5, expand=True, fill=tk.X, pady=5)
        listFrame.pack(side=tk.TOP, padx=10, expand=True)
        listFrameBorder.pack(side=tk.LEFT, padx=10, pady=5,expand=True, fill=tk.Y)
        
        listFrameBorders.append(listFrameBorder)
        listFrames.append(listFrame)
        listNames.append(listName)
        # IF TIME ADD Subtitle: List sorted by ...

        # Creates the visuals for all the items in the list
        for item in allLists[i].tasks:
            # but only if they're set to visible (not marked as complete)
            if item.visible == True:
                itemName = tk.Label(master=listFrame, bg='white', text='● '+item.task, font=("Courier", 12), wraplength=((700/len(allLists))-30))
                itemNames.append(itemName)
                itemName.pack(side=tk.TOP)
                # if the item has a category, it displays it underneath the item
                if item.category != None:
                    itemCat = tk.Label(master=listFrame, bg='white', text=f'({item.category.name})', font=('Courier', 8), wraplength=((700/len(allLists))-30))
                    itemCats.append(itemCat)
                    itemCat.pack(side=tk.TOP)


def load():
    ''' loads up all existing data/info (using what was saved to the files) '''
    global allLists, allItems, allCats
    with open('allListsPickle.obj', 'rb') as f:
        allLists = pickle.load(f)
    with open('allItemsPickle.obj', 'rb') as f:
        allItems = pickle.load(f)
        # list of objects
    with open('allCatsPickle.obj', 'rb') as f:
        allCats = pickle.load(f)
    return allLists, allItems, allCats
