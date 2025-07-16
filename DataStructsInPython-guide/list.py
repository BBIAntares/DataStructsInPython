
def printList(listArg):
    for it in listArg:
        print(it)


x = 0
listOfNumbers = []


while len(listOfNumbers) < 10:
    x+=1
    listOfNumbers.append(x)

printList(listOfNumbers)  


while len(listOfNumbers) != 0:
    listOfNumbers.pop();

printList(listOfNumbers) 