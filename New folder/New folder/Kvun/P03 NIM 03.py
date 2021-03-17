redundantinp = input("Input N: ")
realinp = str(input("Input the string: "))
def subseq(list, ph, anslist):
    if ph == len(arr):  
        if len(anslist) != 0:  
            if anslist == ["t","u","a","n"]: #filter all possibilities if they have the exact tuan arrangement
                KISS.append("count") #the improvised list counter
    else:  
        subseq(arr, ph + 1, anslist)                   #recursion 
        subseq(arr, ph + 1, anslist+[arr[ph]])         #recursion
    return
arr = []
KISS = []
for alphanum in realinp:
    arr.append(alphanum) #making the ["t","u","a","u","a","n","n"]
subseq(arr, 0, []) #running the subseq
print(len(KISS)) #the improvised list counter

