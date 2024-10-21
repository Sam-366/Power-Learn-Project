# Create an empty list

my_list = []

print(my_list)

# Append values to list

my_list = []

my_list.append('10')
my_list.append('20')
my_list.append('30')
my_list.append('40')

print(my_list)

# Extend list

my_list = ['10', '20', '30', '40']
my_list.extend([50, 60, 70])
print(my_list)

# Remove last element

my_list = ['10', '20', '30', '40', 50, 60, 70]
my_list.pop()
print(my_list)

# Sort in ascending order

my_list = ['10', '30', '20', '40', 50, 60, 70]
my_list.sort()
print(my_list)

# Find and print index of 30

my_list = ['10', '30', '20', '40', 50, 60, 70]
index_of_30 = my_list.index(30)
print(index_of_30)
