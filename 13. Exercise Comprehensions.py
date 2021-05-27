'''
# We need to find the duplicate items of a list using list/set/dictionary comprehensions.
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# One of the optimal solution is
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
'''

# My solution
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

duplicates1 = [some_list.count(x) for x in some_list if some_list.count(x) > 1 if x not in duplicates and duplicates.append(x)]
print(duplicates)

# Their solution
duplicate_items = list(set([char for char in some_list if some_list.count(char) > 1]))
print(duplicate_items)