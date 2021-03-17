length_inp = input("Input string length: ")
str_inp = input("Input string: ")
if str_inp[::-1] == str_inp:
    print(f"{str_inp} is a palindrome")
else:
    print(f"{str_inp} is not a palindrome")