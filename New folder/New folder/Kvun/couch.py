a = [4,1,-3,-5,7,0,-6,2,-3,-2]
sum = 0
for i in range(0,8):
    if (i%2!=0):
        sum = sum + a[i]
print("sum= ", sum)