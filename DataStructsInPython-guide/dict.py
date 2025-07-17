# пустой словарь + элем для push'a значений
dictionaryCharKInt = {}
x = 0

# push элементов в словарь (ключ : значение) Можно 2й input для значения написать
while len(dictionaryCharKInt) < 5:
    intIt+=1
    dictionaryCharKInt[input()] = x

print(len(dictionaryCharKInt)) # принтим количество элементов в словаре 
