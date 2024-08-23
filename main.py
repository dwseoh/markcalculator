import json


data = []
categories = {
    
}

#backup
def backup():
    with open("data.json", "r") as a, open("backup.json", "w") as b:
        b.write(a.read())

backup()

def importJson():
    global data,categories

    f = open('data.json')
    dataImported = json.load(f)
    for dataset in dataImported['categories']:
        categories[dataset['name']] = dataset['percent']

    for dataset in dataImported['data']:
        data.append(dataset['raw'])

    print(dataImported)
    dataImported = {"name":"John"}
    print(dataImported)

    f.close()

def updateJson():
    categories_list = [{"name": key, "percent": value} for key, value in categories.items()]
    data_list = [{"raw": item} for item in data]
    custom_dict = {
        "categories": categories_list,
        "data": data_list
    }

    file_path = 'data.json'
    with open(file_path, 'w') as json_file:
        json.dump(custom_dict, json_file, indent=4)

    


importJson()

'''data = [[100,2,0],[95,2,1]]
categories = {
    "Knowledge": 20,
    "Communication":10,
    "Application":20,
    "Thinking":20,
    "Final30":30
}
'''

def resetData():
    global categories,data
    userInput = input("\nAre you sure you want to delete your data?\nType YES (case sensitive) to confirm. Any other input will stop this request.\nInput: ")
    if userInput == 'YES':
        categories = {}
        data = []
        print("Request successful.\n")
        updateJson()
        categorySetup()
    else:
        print("Request stopped.\n")



def calculateMark():
    global categories,data
    if len(data) == 0:
        return [],'-1'

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



def printMarkReport(raw,mark):
    
    if raw != []:
        print(f"\nMARK REPORT\nFinal Mark: {mark:.2f}%\nCategory Breakdown:")
        for data in raw: 
            if data[1] != 0:
                print(f" - {data[4]:<15} ( {data[3]:<3}% )  -  {data[2]:<3.2f} %")
            else:
                print(f" - {data[4]:<15} ( {data[3]:<3}% )  -  N/A (no entry)")
    else:
        print("\nNO ENTRIES\n")

def addEntry():
    global categories,data
    print("\nADD ENTRY\n")
    mark = 999
    while not (0<= mark <=100):
        try:
            mark = float(input('What is the mark you are entering? (Number 1-100 - decimal allowed)\nInput: '))
            if not (0<=mark<=100):
                print("Wrong input. Please try again\n")

        except Exception as e:
            print("Wrong input. Please try again\n")
    
    print("Available Categories:")
    c = 1
    for k,v in categories.items():
        print(f'{c}. {k:<15} ( {v:<3}% )')
        c+= 1

    category = -1
    while not (1<= category <=len(categories)):
        try:
            category = int(input("Which category would you like to choose? Enter the number next to the category name you desire\nInput: "))
            if not (1<= category <=len(categories)):
                print("Wrong input. Please try again\n")

        except Exception as e:
            print("Wrong input. Please try again\n")
    weight = -1.0
    while not (weight>0):
        try:
            weight = float(input("What is the weight factor of this mark? \nInput: "))
            if weight<0:
                print("Wrong input. Please try again\n")

        except Exception as e:
            print("Wrong input. Please try again\n")

    data.append([mark,weight,category-1])
    print("Data added!")
    

def printCategories():
    global categories,data
    print("\nCATEGORIES:")
    c = 1
    for k,v in categories.items():
        print(f'{c}. {k:<15} ( {v:<3}% )')
        c+= 1

def removeEntry():
    global categories,data
    print("\nREMOVE ENTRY\n")
    print("Available Entries:\n")
    c = 1
    t = ['Mark','Weight','Category']
    print(" "*6+f"{t[0]:^10} {t[1]:^10} {t[2]:^20}")
    categoryNames = []
    for k,v in categories.items():
        categoryNames.append(k)
    
    for dataset in data:
        print(f'{c:<5} {dataset[0]:^10.2f} {dataset[1]:^10.2f} {categoryNames[dataset[2]]:^20}')
        c+= 1
    
    removeIndex = -1
    while removeIndex == -1:
        try:
            removeIndex = int(input("\nWhich entry do you want to remove? Please enter the row number\nInput: "))
            if 1<=removeIndex<=len(data):
                print(f"Successful, removed entry #{removeIndex} : ",data[removeIndex-1])
                data.pop(removeIndex-1)
            else:
                print("Wrong input. Please try again\n")
        except Exception as e:
            print("Wrong input. Please try again\n")



def categorySetup():
    global categories,data
    print('CATEGORY SETUP\nExample: "Knowledge": 20, "Communication":10, "Application":20, "Thinking":20,"Final30":30\n')
    sum = 0
    while sum != 100:
        if sum>100:
            print("The category sum has exceeded 100. Resetting categories")
            categories = {}
            sum = 0
        t1 = input(f"What is the category name? (current category sum: {sum})\n")
        try:
            t2 = int(input("\nWhat is the percentage of the category? *must be an integer from 1 to 100\n"))
            if 1<=t2<=100:
                categories[t1] = t2
                sum += t2
                print("Category added!\n")
            else:
                print("Wrong input. Please try again\n")
        except Exception as e:
            print("Wrong input. Please try again\n")

    print("Setup successful!")



if not categories:
    categorySetup()

userInput = ""

#add an option to edit categories later

while userInput != "Exit":
    updateJson()
    userInput = input("What do you want to do?\n\n1 - Add an entry\n2 - Remove an entry\n3 - Reset all data\n4 - Mark report\n5 - View categories\nInput: ")
    
    if userInput == '1':
        addEntry()
    elif userInput == '2':
        removeEntry()
    elif userInput == '3':
        resetData()
    elif userInput == '4':
        a,b=calculateMark()
        printMarkReport(a,b)
        
    elif userInput == '5':
        printCategories()
    
    else:
        print("Wrong input. Please try again\n")
    

