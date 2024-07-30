# -*- encoding: utf-8 -*-

install_gentoo_str = 'Install "Gentoo" now' # 'string "double quote" string'
print(install_gentoo_str)

multiple_strings_concat = "Multiple " "strings" " concat"
print(multiple_strings_concat)

# variable[] -> sequence type
# * strings
# * byte sequences
# * bute arrays
# * lists
# * tuples
# * range objects

str = "Python"
print(str[0])       # -> P
print(str[-1])      # -> n
# print(str[10])    # out of range
print(str[:3])      # -> Pyt
# sequence_type_variable[inclusive:exclusive]

print(str[2:3])     # -> t
print(str[-3:])     # -> hon
# str[1] = 'Y'      # string is immutable. create new string.
new_string_with_cap_y = str[0:1] + 'Y' + str[2:]; # idk there should be better ways to do this, but I start learning python some hours ago. future me, TODO this
print(new_string_with_cap_y)

# str " Python"     # only works with string literal, does not work with expressions and variables.
print (str + " Python")     # use '+' operator
print(str[:2] + str[2:])    # same as str.

# list
numbers = [1, 2, 3, 4, 5]
print(numbers)                  # -> [1, 2, 3, 4, 5]
print(numbers[2])               # -> 3
print(numbers[1:3])             # -> [2, 3]
print(numbers[-2])              # -> 4
print([1, 2, 3] + [4, 5, 6])    # -> [1, 2, 3, 4, 5, 6]

numbers.append(6)
print(numbers)                  # -> [1, 2, 3, 4, 5, 6]

numbers[2:4] = [7, 7] #, 7]     # 오버하게 넣으면 그냥 뒤에 하나 더 넣음
print(numbers)                  # -> [1, 2, 7, 7, 5, 6]
numbers[2:4] = []               # remove
print(numbers)                  # -> [1, 2, 5, 6]
numbers[:] = []
print(numbers)                  # -> []

rgb = ["red", "green", "blue"]
print(rgb)                      # -> ["red", "green", "blue"]

rgba = rgb                      # -> shallow copy
print(id(rgba) == id(rgb))      # -> True, points same reference

rgba.append("Alpa")
print(rgb)                      # -> ["red", "green", "blue", "Alpa"]

correct_alpha = rgba[:]         # -> copies element
correct_alpha[-1] = "alpha"

print(id(correct_alpha) == id(rgba))    # -> False
print(rgba)                             # -> ["red", "green", "blue", "Alpa"]
print(correct_alpha)                    # -> ["red", "green", "blue", "alpha"]

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)                                # -> [['a', 'b', 'c'], [1, 2, 3]]
print(x[0][2])                          # -> c

a, b = 0, 1                             # a = 0, b = 1
while a < 10:
    print(a, end=',')                   # replaces \n to end='<string>'
    a, b = b, a + b
print("") # newline
