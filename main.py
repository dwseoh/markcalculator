import math

'''
data = []
categories = {
    
}
'''

data = [[100,2,0],[95,2,1]]
categories = {
    "Knowledge": 20,
    "Communication":10,
    "Application":20,
    "Thinking":20,
    "Final30":30
}


def printCategories():
    print("\nCATEGORIES:")
    c = 1
    for k,v in categories.items():
        print(f'{c}. {k:<15} ( {v:<3}% )')
        c+= 1


if not categories:
    print('CATEGORY SETUP\nExample: "Knowledge": 20, "Communication":10, "Application":20, "Thinking":20,"Final30":30\n')
    sum = 0
    while sum != 100:
        if sum>100:
            print("The category sum has exceeded 100. Resetting categories")
            categories = {}
            sum = 0
        t1 = input(f"What is the category name? (current category sum: {sum})\n")
        t2 = int(input("\nWhat is the weight of the category? *must be an integer from 1 to 100\n"))
        if 1<=t2<=100:
            categories[t1] = t2
            sum += t2
            print("Category added!\n")
        else:
            print("Wrong input. Please try again\n")

    print("Setup successful!")

userInput = ""

while userInput != "Exit":
    userInput = input("What do you want to do?\n\n1 - Add an entry\n2 - Remove an entry\n3 - Reset all data\n4 - Mark report\n5 - View Categories\nInput: ")
    
    if userInput == '1':
        pass
    elif userInput == '2':
        pass
    elif userInput == '3':
        pass
    elif userInput == '4':
        pass
    elif userInput == '5':
        printCategories()
    

