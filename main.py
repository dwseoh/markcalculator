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


def calculateMark():
    category_marks = []
    for k,v in categories.items():
        category_marks.append([0.0,0.0,0.0,v,k])
    
    for dataset in data:
       category_marks[dataset[2]][0] += (dataset[0]*dataset[1])
       category_marks[dataset[2]][1] += dataset[1]
       category_marks[dataset[2]][2] = category_marks[dataset[2]][0] / category_marks[dataset[2]][1]

    totalMark = 0
    i = 0
    for dataset in category_marks:
        if dataset[1] != 0:
            totalMark += (dataset[3] * dataset[2] / 100)
            i += (dataset[3]/100)
        else:
            pass
    totalMark /= i

    return category_marks,totalMark

    


def addEntry():
    print("\nADDING ENTRY:")

def printMarkReport(raw,mark):
    print(f"\nMARK REPORT\nFinal Mark: {mark:.2f}%\nCategory Breakdown:")
    for data in raw: 
        if data[1] != 0:
            print(f" - {data[4]:<15} ( {data[3]:<3}% )  -  {data[2]:<3.2f} %")
        else:
            print(f" - {data[4]:<15} ( {data[3]:<3}% )  -  N/A (no entry)")


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

#add an option to edit categories later

while userInput != "Exit":
    userInput = input("What do you want to do?\n\n1 - Add an entry\n2 - Remove an entry\n3 - Reset all data\n4 - Mark report\n5 - View Categories\nInput: ")
    
    if userInput == '1':
        addEntry()
    elif userInput == '2':
        pass
    elif userInput == '3':
        pass
    elif userInput == '4':
        a,b=calculateMark()
        print(a,b)
        printMarkReport(a,b)
        
    elif userInput == '5':
        printCategories()
    

