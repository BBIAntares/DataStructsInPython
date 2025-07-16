# эт функция, которая принтит список 
def printList(listArg):
    for it in listArg:
        print(it)

# пустой список + элем для push'a 
x = 0
listOfNumbers = []

# push элементов в список 
while len(listOfNumbers) < 10:
    x+=1
    listOfNumbers.append(x)

printList(listOfNumbers)  

# фулл pop элементов
while len(listOfNumbers) != 0:
    listOfNumbers.pop();

printList(listOfNumbers) # принтит пустой список

# для pop'a и push'a можно написать функции, но python меня душит 
