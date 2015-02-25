__author__ = 'Brian'

"""This file is an experimental typing adventure game
I made to test if PyCharm educational edition will
work for what we are trying to do."""

print("You are at the supermarket choosing your lunch for tomorrow. You stumble upon the lunchable section and decide you want one.")
print(" ")

def lunch_chooser():
    print("The three choices the supermarket has are:")
    print(" ")
    print("1. The ham, cheese, and cracker stackers")
    print("2. The cheese pizza")
    print("3. The nachos")
    print(" ")
    print("Which one do you choose?")

    answer = str(input("Type 1, 2, or 3 and press enter: "))

    print(" ")
    if answer == '1':
        print("Classic stackers!")
    elif answer == '2':
        print("You must like cold pizza!")
    elif answer == '3':
        print("I've had worse nachos...")
    else:
        print("You didn't type 1, 2, or 3. ".upper() + "Try again.")
        print(" ")
        lunch_chooser()

lunch_chooser()