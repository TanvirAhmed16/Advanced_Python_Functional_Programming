'''
# Python Lambda Functions - A lambda function is a small anonymous function. In Python, an anonymous function means
  that a function is without a name. As we already know that the def keyword is used to define a normal function in
  Python. Similarly, the lambda keyword is used to define an anonymous function in Python. Basically we use this
  function in those places where we don't need to use a function more than once.

# It has the following syntax:
    Syntax: lambda arguments: expression
# This function can have any number of arguments but only one expression, which is evaluated and returned.
# One is free to use lambda functions wherever function objects are required.
# You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
--> Let's see some examples related to our previous function examples. Let's do the same with Lambda Function.
'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# map()
def multiplied_by_2(item):
    return item * 5


print(list(map(multiplied_by_2, my_list)))
# Let's do the same using Lambda Function.
print(list(map(lambda item: item * 5, my_list)), '\n')


# filter()
def only_even(item):
    return item % 2 == 0


print(list(filter(only_even, my_list)))
# Let's do the same using Lambda Function.
print(list(filter(lambda item: item % 2 != 0, my_list)), '\n')


# reduce()
def accumulator(acc, item):
    print(acc, item)
    return acc + item


from functools import reduce
print(reduce(accumulator, my_list, 5), '\n')
# Let's do the same using Lambda Function.
print(reduce(lambda acc, item: acc + item, my_list, 5))