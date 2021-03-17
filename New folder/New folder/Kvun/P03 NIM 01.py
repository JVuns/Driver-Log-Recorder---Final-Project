my_list = []
my_input = int(input("angka: "))
i = 0 #iteration initializer

while i < my_input: # if iteration is still less than my_input
    if i%2 == 0: # if it is even
        sub_input = input("Enter a ["+ str(i+1) +"]: ")
        my_list.append(int(int(sub_input)))
        i += 1
    elif i%2 == 1: # if it is odd (you can use else and remove the parameter if you want but elif is a safer choice)
        sub_input = input("Enter a ["+ str(i+1) +"]: ")
        my_list.append(int(int(sub_input)*-1))
        i += 1
print(sum(my_list))