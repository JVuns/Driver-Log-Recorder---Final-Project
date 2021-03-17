input1 = int(input("Input N: ")) 
input2 = int(input("input M: ")) 
count = 0
matrix = []  

for i in range(input1):        
    a =[] 
    for j in range(input2):  
         a.append(int(input(f"Input value A[{i+1}][{j+1}]"))) 
    matrix.append(a) 
for i in range(input1):
    for j in range(input2):
        if matrix[i][j] > 0:
            count += 1
if matrix[0][1] == 0 and matrix[0][2] == 0 and matrix[1][2]:
    print("Lower triangle matrix")
elif matrix[1][0] == 0 and matrix[2][0] == 0 and matrix[2][1]:
    print("Upper triangle matrix")
elif matrix[0][1] == 0 and matrix[0][2] == 0 and matrix[1][2] and matrix[1][0] == 0 and matrix[2][0] == 0 and matrix[2][1]:
    print("Diagonal matrix")
else:
    print("Not a special matrix")
print(matrix)