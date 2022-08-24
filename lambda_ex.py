# square
my_list = [2, 3, 4]

print(list(map(lambda item: item**2, my_list)))

# List sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda item: item[1])
print(a)
