length_inp = int(input("Input N: "))
string_inp = str(input("Input String: "))
my_list = []
for alphanumeric in string_inp: #will iterate through each alphanumeric of string_inp
    if alphanumeric in my_list: #checking if there is any duplicate. If alphanumeric is already exist the function will pass
        pass
    elif not alphanumeric in my_list and int(len(my_list)) < length_inp: #if there is no duplicate and the
        my_list.append(alphanumeric)                                     #list is still less than length_inp,
print(my_list)                                                           #append it to my_list