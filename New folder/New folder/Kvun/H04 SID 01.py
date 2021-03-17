input1 = int(input("Input A: "))
input2 = int(input("Input B: "))

def function(x):
    return(f"f({num}) = {num**2-2*num+5}")
for num in range(input1,input2+1):
    print(function(num))