'''
# Set Comprehensions - Set comprehensions are pretty similar to list comprehensions. The only difference between
  them is that set comprehensions use curly brackets { }. Let’s look at the following example to understand set
  comprehensions.
-> Note that set will discard all the duplicate values. Let’s see how we can do this using for loops and set
    comprehension.
'''

'''
Example #1 : Suppose we want to create an output set which contains only the even numbers that are present in the 
input list. 
'''
# Constructing output set Using for loop...
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_set = set()

for num in input_list:
    if num % 2 == 0:
        output_set.add(num)

print(f'The output list using for loop is : {output_set}')

# Constructing output set Using set comprehensions...
output_set = {num for num in input_list if num % 2 == 0}
print(output_set)
print(f'The output set using set comprehension is : ', {num for num in input_list if num % 2 == 0}, '\n')

# Creating new Set very easily...
print(f'My new set is: ', sorted({num * 5 for num in range(0, 10)}))
print(f'My new set-2 is: ', sorted({num * num for num in range(0, 5)}), '\n')


'''
# Dictionary Comprehensions - Extending the idea of list comprehensions, we can also create a dictionary using 
dictionary comprehensions. The basic structure of a dictionary comprehension looks like below.
 
--> output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}
'''

'''
Example #1: Suppose we want to create an output dictionary which contains only the odd numbers that are present in 
the input list as keys and their cubes as values. Let’s see how to do this using for loops and dictionary comprehension.
'''
# Constructing output dictionary Using for loop...
input_list = [1, 2, 3, 4, 5, 6, 7]
output_dict = {}

for num in input_list:
    if num % 2 != 0:
        output_dict[num] = num**3

print(f'My dictionary using for loop is:', output_dict, '\n')

# Constructing output dictionary Using dictionary comprehensions...
my_dict = {num: num*2 for num in input_list if num % 2 != 0}
print(my_dict, '\n')

my_dict1 = {key: num*2 for key in input_list if key % 2 != 0}
print(my_dict, '\n')


simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
my_dict1 = {key: value*3 for key, value in simple_dict.items() if key == 'a' or value % 2 == 0}
print(my_dict1)
