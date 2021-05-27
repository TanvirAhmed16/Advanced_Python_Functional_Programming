# Square
my_list = [5, 4, 3]
print(list(map(lambda item: item * item, my_list)))

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1), (5, 8)]


def sort_tuple(tup):
    tup.sort(key=lambda x: x[1])
    return tup


a.sort()  # This will sort the list according to the first item.
print(a)
print(sort_tuple(a))