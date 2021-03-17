def rec(n):      
    if n>0:
        print(n)
        return(rec(n-1))
    else:
        print("done")
