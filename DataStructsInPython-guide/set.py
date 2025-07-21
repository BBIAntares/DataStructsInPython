# два множества 
setA = {"apple", "banana", "cherry"}
setB = {"watermelon", "banana"}

# объединиение множеств (без повторок)
setUnion = setA.union(setB)
print(setUnion)

# пересечение
setIntersection = setA.intersection(setB)
print(setIntersection)

# a - пересечение a и b
diffSetA = setA.difference(setB)
print(diffSetA)

# b - пересечение a и b
diffSetB = setB.difference(setA)
print(diffSetB)