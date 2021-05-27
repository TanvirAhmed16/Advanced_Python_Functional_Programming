'''
# Comprehensions in Python - Comprehensions in Python provide us with a short and concise way to construct new
  sequences (such as lists, set, dictionary etc.) using sequences which have been already defined. Python supports
  the following 4 types of comprehensions:

    # List Comprehensions
    # Dictionary Comprehensions
    # Set Comprehensions
    # Generator Comprehensions

# List Comprehensions:
    List Comprehensions provide an elegant way to create new lists. The following is the basic structure of a list
    comprehension:

output_list = [output_exp for var in input_list if (var satisfies this condition)]

Note that list comprehension may or may not contain an if condition. List comprehensions can contain multiple
for (nested list comprehensions).
'''

'''
Example #1: Suppose we want to create an output list which contains only the even numbers which are present in 
the input list. Let’s see how to do this using for loops and list comprehension and decide which method suits better.
'''

# Constructing output list WITHOUT Using List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_list = []

for num in input_list:
    if num % 2 == 0:
        if num not in output_list:  # Checking duplicate item. An extra condition.
            output_list.append(num)

print(f'The output list using for loop is : {output_list}')

# Constructing output list Using List comprehensions
print(f'The output list using list comprehension is : ', [num for num in input_list if num % 2 == 0], '\n')

# Creating new list very easily...
print([num for num in range(0, 50) if num % 2 == 0])
my_list = [num*3 for num in range(0, 20)]
print(my_list)
