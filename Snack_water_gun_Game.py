#Module import
import random

#Function definition
def gameWin(comp, you):
    if comp == you:
        return None

    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

#Randomly taking computer's choice
print("Computer's turn:\nSnack(s), Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
if(randNo == 1):
    compTurn = 's'
elif(randNo == 2):
    compTurn = 'w'
elif(randNo == 3):
    compTurn = 'g'

#Taking Your's Choice
You = input("Your's turn:\nSnack(s), Water(w) or Gun(g)?")

#Calling function and Passing values to the gameWin function
result = gameWin(compTurn, You)

#Printing choices
print(f"Computer's choice: {compTurn}\n Your choice: {You}")

#Result
if result == None:
    print("Game is Tie")
elif result:
    print("You Win!")
else:
    print("Computer Win!")