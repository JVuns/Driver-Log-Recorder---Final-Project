input2 = int(input("Input N : "))
count = 0
while count < input2:
    input1 = str(input(f"Password {count+1}: "))
    kitten = ""
    for i in input1:
        if i not in ["_","-","*"]:
            kitten += i
    count += 1
    print("kitten {}: {}".format(count, kitten))
    