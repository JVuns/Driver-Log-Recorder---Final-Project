input1 = int(input("input l: "))
input2 = int(input("input r: "))
my_list = []
for num in range(input1,input2):
    currentnum = (abs((num*2 + 3)-(num*4-5)))
    my_list.append([currentnum,num])
my_list.sort()
print(f"The integer x found is {my_list[0][1]}")
    