# def fibonacci(x):
#     if x==1:
#         return 0
#     elif x==2:
#         return 1
#     else:
#         return(fibonacci(x-1)+fibonacci(x-2))
    
# num = int(input("number"))
# print(fibonacci(num))

def fibonacci(count): 
    my_list = [0, 1] 
    any(map(lambda _: my_list.append(sum(my_list[-2:])), range(1, count,)))
  
    return my_list[:count] 
  
print(fibonacci(int(input("the number of series :")))) 