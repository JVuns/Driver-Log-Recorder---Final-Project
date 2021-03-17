num_inp = int(input("Input N: "))
num_list = []
while num_inp != 0:
    num_list.append(input(""))
    num_inp -= 1
print(num_list[::-1])