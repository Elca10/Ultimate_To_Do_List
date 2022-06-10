def createList():
    global allLists, allItems, allCats
    aList = List(input("Enter list name: "))
    allLists.append(aList)


def createItem():
    global allLists, allItems, allCats
    anItem = Item(input("Enter item/task: "))
    allItems.append(anItem)
    anItem.setList()




def userInputOLD():
    global allLists, allItems, allCats
    # ACTIONS:
    # (1) Create a list
    # (2) Create an item
    # (3) Sort a list
    # (4) Mark item as complete
    # (5) Add information to an item
    # (6) Move item to a different list
    # (7) Delete item
    # (8) Delete list (and items in list)
    # (9) Create a category


    print()
    actions = ['(1) Create a list', '(2) Create an item', '(3) Sort a list', '(4) Mark item as complete',
               '(5) Add information to an item (Edit it)', '(6) Move item to a different list', '(7) Delete item',
               '(8) Delete list (and items in list)','(9) Create a category']
    functions = {1:createList, 2:createItem, 3:sortList, 4:completeItem, 5:itemInfo,
                 6:moveItem, 7:delItem, 8:delList, 9:createCategory}
    
    for s in actions:
        print(s)
    try:
        choice = int(input('Enter the corresponding number to the action you would like to take: '))

    except:
        choice = int(input('Please enter a valid number: '))
    
    functions[choice]()    
    # updateDisplay()





### INSIDE OF ITEM CLASS ###
    
    def setList(self): # print a numbered list that corresponds with list nums
        global allLists, allItems, allCats
        print('\nWhat list would you like to add the card to?')
        for i in range(len(allLists)):
            print(f'({i+1}) {allLists[i].name}')
        try:
            self._list = allLists[int(input('Enter the corresponding number to the list of your choice: '))-1]
        except:
            self._list = allLists[int(input('Please enter a valid number: '))-1]



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
        
    def showCard(self):
        self.visible = True

##########################




def action(userAction, event=None):
    print("INSIDE OF ACTION FUNCTION IN MASTER")
    userActionChoice = userAction.get() # get the contents of the entry widget
    userAction.delete(0, 'end')
    try:
        userActionChoice = int(userActionChoice)
        if userActionChoice <= 9 and userActionChoice >= 0:
            print('hello im here')
            exec(userInput(userActionChoice))
            print('now here')
            print(userActionChoice)
            
            return userActionChoice # RETURNS ONLY VALID NUMBERS
    except:
        pass
    
def action1(event=None):
    userActionChoice = userAction.get() # get the contents of the entry widget
    userAction.delete(0, 'end')
    try:
        userActionChoice = int(userActionChoice)
        if userActionChoice <= 9 and userActionChoice >= 0:
            print('hello im here')
            uI = userInput(userActionChoice,rightW)
            print('now here')
            print(userActionChoice)
            #if userActionChoice==1:
            #    createListVisual(rightW)
            #    print("INSIDE OF IF STATEMENT")
            
            print("done")

            #return userActionChoice # RETURNS ONLY VALID NUMBERS
    except:
        pass


def createCategory():
    global allLists, allItems, allCats
    aCat = aCat(input("Enter category name: "))
    allCats.append(aCat)


def save():
    global allLists, allItems, allCats
   # allListsDF = pd.DataFrame(allLists)
    #allListsDF.to_pickle('allListsPickle.pkl')

    with open('allListsPickle.obj', 'wb') as f:
        pickle.dump(allLists, f)
    with open('allItemsPickle.obj', 'wb') as f:
        pickle.dump(allItems, f)
    with open('allCatsPickle.obj', 'wb') as f:
        pickle.dump(allCats, f)

    print(f'Last saved at {datetime.now().strftime("%H:%M:%S")}')    
    # print('Saving at 11:41 AM') or 'Last saved at 11:40 AM'



def delList():
    global allLists, allItems, allCats
    print("---FIX THIS---- Needs to also delete from the pickle file (maybe in save file just resave it?)")
    print("--- I THINK I DID THIS BELOW---")
    print('*Warning* This will also delete all items in the list')
    print('\nWhat list would you like to delete?')
    print(len(allLists))
    for i in range(len(allLists)):
        print(f'({i+1}) {allLists[i].name}')
    try:
        delList = allLists[int(input('Enter the corresponding number to the list of your choice: '))-1]
    except:
        delList = allLists[int(input('Please enter a valid number: '))-1]
    for item in delList.tasks:
        del item
    del delList
    print(len(allLists))
    global savedMsgs
    savedMsgs.append(save(leftW, savedMsgs[-1]))



def delItem():
    global allLists, allItems, allCats
    print('\nWhat item would you like to delete?')
    for i in range(len(allItems)):
        print(f'({i+1}) {allItems[i].task}')
    try:
        editItem = allItems[int(input('Enter the corresponding number to the item of your choice: '))-1]
    except:
        editItem = allItems[int(input('Please enter a valid number: '))-1]

    del editItem




def sortList2(self): 
    '''do sorting stuff'''
    print(f"\nHow would you like to sort '{self.name}'?")
    sortOptions = ['Category', 'Priority', 'Date Due', 'Name', 'Date Created']
    sortByOptions = ['sortByCategory', 'sortByPriority', 'sortByDue', 'sortByName', 'sortByCreated']
    sortFunctions = {0:self.sortByCategory, 1:self.sortByPriority, 2:self.sortByDue, 3:self.sortByName, 4:self.sortByCreated}
    i  = 0
    for s in sortOptions:
        i += 1
        print(f'({i}) {s}')
    try:
        choice = int(input('Enter the corresponding number to the sorting method of your choice: '))-1
        sortBy = sortByOptions[choice]
    except:
        choice = int(input('Please enter a valid number: '))-1
        sortBy = sortByOptions[choice]
    
    self.sortBy = sortBy
    sortFunctions[choice]()



def sortList():
    global allLists, allItems, allCats
    print('\nWhat list would you like to sort?')
    for i in range(len(allLists)):
        print(f'({i+1}) {allLists[i].name}')
    try:
        listToSort = allLists[int(input('Enter the corresponding number to the list of your choice: '))-1]
    except:
        listToSort = allLists[int(input('Please enter a valid number: '))-1]
    listToSort.sortList()


def completeItem():
    global allLists, allItems, allCats
    print('\nWhat item would you like to mark as complete?')
    for i in range(len(allItems)):
        print(f'({i+1}) {allItems[i].task}')
    try:
        finsihed = allItems[int(input('Enter the corresponding number to the item of your choice: '))-1]
    except:
        finished = allItems[int(input('Please enter a valid number: '))-1]
    finished.setComplete() # also sets visible to false


def moveItem():
    global allLists, allItems, allCats
    print('\nWhat item would you like to move?')
    for i in range(len(allItems)):
        print(f'({i+1}) {allItems[i].task}')
    try:
        editItem = allItems[int(input('Enter the corresponding number to the item of your choice: '))-1]
    except:
        editItem = allItems[int(input('Please enter a valid number: '))-1]

    print(f"\nWhat list would you like to move '{editItem.task}' to?")
    for i in range(len(allLists)):
        print(f'({i+1}) {allLists[i].name}')
    try:
        newList = allLists[int(input('Enter the corresponding number to the list of your choice: '))-1]
    except:
        newList = allLists[int(input('Please enter a valid number: '))-1]
    editItem._list = newList


def intro():
    global allLists, allItems, allCats
    list1 = List(input("\nLet's start by making a list. What would you like to call it? "))
    allLists.append(list1)
    task1 = Item(input("Next let's make a list item, or task. For example: write code. Enter yours here: "))
    allItems.append(task1)
    task1.setList()


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











def itemInfo():
    global allLists, allItems, allCats
    print('\nWhat item would you like to edit or add to?')
    for i in range(len(allItems)):
        print(f'({i+1}) {allItems[i].task}')
    try:
        editItem = allItems[int(input('Enter the corresponding number to the item of your choice: '))-1]
    except:
        editItem = allItems[int(input('Please enter a valid number: '))-1]

    actions = ['List', 'Category', 'Priority','Due Date', 'Complete']
    functions = {0:editItem.setList, 1:editItem.setCategory, 2:editItem.setPriority,
                 3:editItem.setDue, 4:editItem.setComplete}

    for i in range(len(actions)):
    try:
        edit = int(input('Enter the corresponding number to the action of your choice: ').strip())-1
    except:
        edit = int(input('Please enter a valid number: ').strip())-1
    functions[edit]()












