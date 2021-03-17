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
            count +=1
# For printing the matrix 
print(f"There are {count} positive integers in matrix")
for i in range(input1): 
    for j in range(input2): 
        print(matrix[i][j], end = " ") 
    print()