'''
# Pure Functions - A function is called pure function if it always returns the same result for same argument
  values and it has no side effects like modifying an argument (or global variable) or outputting something.
  The only result of calling a pure function is the return value. Examples of pure functions are strlen(), pow(),
  sqrt() etc. Examples of impure functions are printf(), rand(), time(), etc.
# If a function is known as pure to compiler then Loop optimization and subexpression elimination can be applied
  to it. In GCC, we can mark functions as pure using the “pure” attribute.
'''


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))
'''
Here no matter how many times we run this program, this will give us the same output which won't affect the
outside world.
But if we declare our new list as global then this will no longer be a pure function as it can be modified.
'''

new_list = []


def multiplied_by3(li):
    for item in li:
        new_list.append(item * 3)
    return new_list


print(multiplied_by3([1, 2, 3]))

new_list = ''
print(multiplied_by3([1, 2, 3]))
