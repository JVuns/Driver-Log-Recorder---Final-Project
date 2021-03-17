input1 = str(input("Input the initial integer: "))
count = 0
while len(input1) != 1:
    result = 1
    for i in input1:
        count += 1
        result *= int(i)
    input1 = str(result)
    print (f"After {count} process: {result}")



    