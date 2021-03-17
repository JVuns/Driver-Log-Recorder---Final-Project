input1 = int(input("Input N: "))
input2 = int(input("Input M: "))
matrix = []
input3 = str(input("Input string: "))

count = 0
for y in range(input1):
    for i in range(input2):
        a = []
        a.append(input3[count::(input2)])
    matrix.append(a)
    count += 1
a = ""
for x in matrix:
    for c in x:
        a += c
print(a)