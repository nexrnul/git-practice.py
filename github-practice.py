toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def addItem(userAns):
    toDoList.append(itemA)
    return toDoList

def deleteItem(userEdit):
    toDoList.remove(itemD)
    return toDoList

while True:
    userAns = input("Do you want to edit to your list or quit? E/Q") 
    if userAns == 'Q':
            print(toDoList)
            break
    elif userAns == 'E':
            userEdit = input("Would you like to add or delete from list? A/D")
            if userEdit == 'A':
                itemA = input("What would you like to add?")
                addItem(itemA)
                print(toDoList)
                
            elif userEdit == 'D':
                    itemD = input("Which would you like to delete?")
                    if itemD in toDoList:
                        deleteItem(itemD)                      
                        print("Item successfuly deleted")
                        #else: print(ITEM NOT FOUND)
                        
                        
                        
    



        
