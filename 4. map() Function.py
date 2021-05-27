'''
# Python map() function - map() function returns a map object(which is an iterator) of the results after applying
  the given function to each item of a given iterable (list, tuple etc.)
# Syntax :
    map(fun, iter)
# Parameters :
    fun : It is a function to which map passes each element of given iterable.
    iter : It is a iterable which is to be mapped.
# NOTE : You can pass one or more iterable to the map() function.
# Returns :
    Returns a list of the results after applying the given function to each item of a given iterable
    (list, tuple etc.)
# NOTE : The returned value from map() (map object) then can be passed to functions like list()
        (to create a list), set() (to create a set) .
'''


def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, [1, 2, 3])))
'''
# Here we can see, we don't need to use () to call our defined function as map() itself call that.
# map() doesn't modify any data, it generates , i mean let's see our below example. 
'''
my_list = [3, 6, 9]
print(list(map(multiply_by2, my_list)))
print(my_list, '\n')
'''
# Here we can see our my_list remains the same. Let's see another example.
'''


def make_double(n):
    return n + n


my_data = [1, 3, 5]
result = map(make_double, my_data)
print(list(result))
