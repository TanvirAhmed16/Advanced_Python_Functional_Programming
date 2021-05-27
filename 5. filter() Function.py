'''
# filter() in python - The filter() method filters the given sequence with the help of a function that tests each
  element in the sequence to be true or not.
# syntax:
    filter(function, sequence)
# Parameters:
    function: function that tests if each element of a sequence true or not.
# sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.
# Returns:
    returns an iterator that is already filtered.
'''

my_list = [1, 2, 3, 4, 5, 6]


def only_even(item):
    return item % 2 == 0


print(list(filter(only_even,my_list)))


alphabets = ['d', 's', 'a', 'r', 'q', 'i', 'h', 'e']


def find_vowel(item):
    if item in ('a', 'e', 'i', 'o', 'u'):
        return item


print(list(filter(find_vowel, alphabets)))



