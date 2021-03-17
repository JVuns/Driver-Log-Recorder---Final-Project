def multiply_list(start, stop):
    product = 1
    for element in range(start, stop):
        product = product * element
    return product
x = multiply_list(1, 4)
print(x)