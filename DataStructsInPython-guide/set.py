# ��� ��������� 
setA = {"apple", "banana", "cherry"}
setB = {"watermelon", "banana"}

# ������������ �������� (��� ��������)
setUnion = setA.union(setB)
print(setUnion)

# �����������
setIntersection = setA.intersection(setB)
print(setIntersection)

# a - ����������� a � b
diffSetA = setA.difference(setB)
print(diffSetA)

# b - ����������� a � b
diffSetB = setB.difference(setA)
print(diffSetB)