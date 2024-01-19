#Jiawen & Leslie's Shopping List
#1/10/2024

#Initalize 
print("Welcome to the Shopping List!")
item1=str(input("What is the first item you would like to shop for? "))
item2=str(input("What is the second item you would like to shop for? "))
item3=str(input("What is the last item you would like to shop for? "))
ShoppingList=[item1,item2,item3]
#Functions 

def showList():
    print(ShoppingList)
def complete():
    ShoppingList.remove(input("Which item have you gotten? "))
    showList()
def eraseList():
    ShoppingList.remove(input("Which item would you like to remove from your grocery list? "))
    showList()
def Grocery():
    for i in range (99):
        print("What action would you like to do?")
        print("1: View List \n2: Mark item as complete \n3: Add item \n4: Remove item \n5: Replace item \n6: Remove all \n7: Alphabetically organize \n8: See total number of items \n9: Quit")
        option=input("Option: ")
        if option == "1":
            showList()
        elif option == "2":
            complete()
        elif option == "3":
            newfood=input("What item would you like to add? ")
            ShoppingList.insert(0, newfood)
            showList()  
        elif option == "4":
            eraseList()
        elif option == "5":
            ShoppingList.remove(input("What item would you like to replace? "))
            newf1=input("What would you like to replace it with? ")
            ShoppingList.insert(2, newf1)
            showList()
        elif option =="6":
            ShoppingList.clear
            showList()
        elif option =="7":
            ShoppingList.sort()
            showList()
        elif option =="8":
            print("There are "+len(ShoppingList)+" items in your list.")
        elif option =="9":
            print("Thank you for visiting, see you next time.")
            quit()    
#Main 
Grocery()
