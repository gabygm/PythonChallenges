
dict_numbers = {'A': 6, 'B': 2, 'C': 34, 'D': 9}
x = dict_numbers.keys()
square_dict = {k: v**2 for (k, v) in dict_numbers.items() if 'A' in k}
print(square_dict)

temp_fahrenheit = {"temp_1": 10, "temp_2": 9, "temp_3": 50, "temp_4": 45}
temp_celsius = {k: ((v-32)*5)/9 for k, v in temp_fahrenheit.items()}
print(temp_celsius)




