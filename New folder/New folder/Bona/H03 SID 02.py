num_inp = int(input("Input number of elements in A: "))
list_a = []
counter = 1
while num_inp != 0:
    list_a.append(input(f"Input element A number {counter}: "))
    num_inp -= 1
    counter += 1
num_inp = int(input("Input number of elements in B: "))
list_b = []
counter = 1
while num_inp != 0:
    list_b.append(input(f"Input element B number {counter}: "))
    num_inp -= 1
    counter += 1
dict_fa = {}
dict_fb = {}
for element in list_a:
    if element in dict_fa:
        dict_fa[element] += 1
    else:
        dict_fa[element] = 1
for element in list_b:
    if element in dict_fb:
        dict_fb[element] += 1
    else:
        dict_fb[element] = 1
if dict_fa == dict_fb:
    print("B is anagram of A")
else:
    print("B is not anagram of A")