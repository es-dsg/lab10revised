'''
DEVELOPER: <your name>
COLLABORATORS: <anyone you worked with>
DATE: <date last worked on>
'''

"""A one line summary of the program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the program.
"""

##########################################
# IMPORTS:
#   <list modules needed for program and their purpose>
##########################################
import random

##########################################
# FUNCTIONS:
##########################################
def randomList():
    list2=random.sample(range(1,50),5)
    list2.append(random.randint(1,19))
    return (f"Your lottery ticket is: {list2[0]:02d} {list2[1]:02d} {list2[2]:02d} {list2[3]:02d} {list2[4]:02d} (mega {list2[5]})")

def customTicket():
    list1 = [0,0,0,0,0]
    list2=[]
    for element in list1:
        element= int(input("Enter your lottery number between 1 and 49: "))
        if element in list2:
            element=input("Invalid input. Enter your lottery number between 1 and 49: ")
        
        list2.append(int(element))
    
    list2.append(random.randint(1,20))
    return(f"Your lottery ticket is: {list2[0]:02d} {list2[1]:02d} {list2[2]:02d} {list2[3]:02d} {list2[4]:02d} (mega {list2[5]:02d})")
        


##########################################
# MAIN PROGRAM:
##########################################
def main():
    pass

main()
print("Welcome to Python Lotto!")
print("You have the option to choose your own lottery numbers or have them randomly selected for you.")
choose = input("Please enter C for custom or R for random:\n")
if choose.upper() == "C":
    print(customTicket())
elif choose.upper() =="R":
    print(randomList())

