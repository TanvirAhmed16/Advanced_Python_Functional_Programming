'''
# reduce() in Python - The reduce(fun,seq) function is used to apply a particular function passed in its argument
  to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.
# Working :
--> At first step, first two elements of sequence are picked and the result is obtained.
--> Next step is to apply the same function to the previously attained result and the number just succeeding the
    second element and the result is again stored.
--> This process continues till no more elements are left in the container.
--> The final returned result is returned and printed on console.
'''

from functools import reduce

my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item
print(reduce(accumulator, my_list, 0))