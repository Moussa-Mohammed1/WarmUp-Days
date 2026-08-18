# raw strings use the word 'r' before the single quoting opening, to show full string without any special caracter interpretation, for example:
print(r'C:\this\name')

# string literals can gather multiple lines in one string, by using triple-quotes: """...""" or '''...'''
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


# strings can be indexed, and we can access a caracter by its position

word = 'Moussa-Mohammed1'
print(word[7]) # caracter in position 0
print(word[-1]) # last caracter
print(word[-2]) # second-last caracter 
print(len(word)) # 16
# print(word[66]) # IndexError: string index out of range

# its possible to slice a string also by writing string[start:end] (start is included, end is excluded)
# word[:i] + word[i:] always equals to word
print(word[:4] + word[4:])
# 'Moussa-Mohammed1'
print(word[0:1] + word[7:8])  # concactination using + symbol
# 'MM'
print(word[7:-1])
# 'Mohammed'
print(word[:6])
# 'Moussa'
# out of range index while slicing, are handled silenty
print(word[:66])
'Moussa-Mohammed1'
print(word[66:])
''


# ===== LISTS =====

# a list is a collection of elements, we write them between [ ] and separate them with commas
# a list can hold different types of elements at the same time

my_list = [1, 2, 3]
mixed = ['apple', 42, 3.14, True]
print(my_list)
print(mixed)

# like strings, lists are indexed from 0
print(my_list[0])   # first element
print(mixed[-1])    # last element
print(len(my_list)) # number of elements

# we can also slice a list, the same way we did with strings
print(my_list[:2])  # first two elements

# BUT: unlike strings, lists are mutable
# it means we can CHANGE an element after the list is created
my_list[0] = 10
print(my_list)  # [10, 2, 3]

# add an element at the end with .append(element)
my_list.append(4)
print(my_list)  # [10, 2, 3, 4]

# add an element at a specific position with .insert(position, element)
my_list.insert(1, 99)
print(my_list)  # [10, 99, 2, 3, 4]

# remove an element by its value with .remove(element)
my_list.remove(99)
print(my_list)  # [10, 2, 3, 4]

# remove AND return the last element with .pop()
last = my_list.pop()
print(last)     # 4
print(my_list)  # [10, 2, 3]

# check if an element exists with the 'in' keyword
print(2 in my_list)   # True
print(42 in my_list)  # False

# python have Lists, which we can group a difference variables from difference types

squares = [1, 4, 9, 16, 25]
print(squares)


