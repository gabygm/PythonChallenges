
numbers = [3, 6, 7, 8, 6, 4, 6]
is_even = [x if x % 2 == 0 else 0 for x in numbers]


list1 = [1, 2, 3, 4, 5, ]
list2 = [2, 4, 5, 6, 7, ]

intersection = [x for x in list1 for y in list2 if x == y]
print(intersection)


list_3 = [1, 2, 3, 4, 5, 6]
x = [[a**2, a**3] for a in list_3]
print(x)

