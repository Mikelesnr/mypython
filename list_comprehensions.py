# kist, set ,dict

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

my_list2 = [char for char in 'hello']

print(my_list2)

#my_list3 = [num for num in range(0, 100)]

#print([num*2 for num in range(0, 100)])

print(list(filter(lambda item: item %
      2 == 0, list([num for num in range(0, 100)]))))

print([num for num in range(0, 100) if num % 2 == 0])
