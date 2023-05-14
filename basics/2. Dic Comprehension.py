
dict_numbers = {'A': 6, 'B': 2, 'C': 34, 'D': 9}
x = dict_numbers.keys()
square_dict = {k: v**2 for (k, v) in dict_numbers.items() if 'A' in k}
print(square_dict)



