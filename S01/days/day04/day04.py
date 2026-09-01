# ===== DAY 04 - INPUT / OUTPUT =====
# this day is about:
#   1) formatting the OUTPUT (f-strings, format(), ...)
#   2) READING and WRITING files


# ===== 1) FORMATTING OUTPUT =====

# --- f-strings ---
# put an f (or F) before the quotes, then write expressions inside { }

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
# Results of the 2016 Referendum

# --- str.format() ---
# {} are replaced by the arguments we pass

yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
# ' 42572654 YES votes  49.67%'

# --- str() vs repr() ---
# str()  -> for humans to read
# repr() -> for the interpreter (with quotes and special characters)

s = 'Hello, world.'
print(str(s))
# Hello, world.
print(repr(s))
# 'Hello, world.'
print(str(1/7))
# 0.14285714285714285

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The value of x is 32.5, and y is 40000...
hello = 'hello, world\n'
print(repr(hello))
# 'hello, world\n'
print(repr((x, y, ('spam', 'eggs'))))
# "(32.5, 40000, ('spam', 'eggs'))"

# --- string.Template ---
# replace $placeholders with values (easy but less control)

from string import Template
t = Template('Hey $name, welcome to $place!')
print(t.substitute(name='Youco', place='Oran'))
# Hey Youco, welcome to Oran!


# ===== 1.1 f-strings in detail =====

import math

# a format spec after ':' -> here 3 decimals for pi
print(f'The value of pi is approximately {math.pi:.3f}.')
# The value of pi is approximately 3.142.

# an integer after ':' = minimum field width (nice for tables)
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678

# conversions: !s -> str(), !r -> repr()
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')
# My hovercraft is full of 'eels'.

# the = specifier shows "expression=value" (good for debugging)
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
# Debugging bugs='roaches' count=13 area='living room'


# ===== 1.2 str.format() in detail =====

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"

# numbers inside {} = position of the argument
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
# spam and eggs
# eggs and spam

# named arguments
print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))
# This spam is absolutely horrible.

# positional + named together
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
# The story of Bill, Manfred, and Georg.

# access dict keys with [key]
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# or with **table (unpack the dict as named arguments)
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# aligned table: squares and cubes
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
#  1   1    1
#  2   4    8
# ... etc


# ===== 1.3 manual formatting =====

# same table, but formatted by hand with rjust()
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
#  1   1    1
#  2   4    8
# ... etc

# rjust() / ljust() / center() pad a string with spaces
# zfill() pads with zeros (it understands + and -)
print('12'.zfill(5))
# 00012
print('-3.14'.zfill(7))
# -003.14
print('3.14159265359'.zfill(5))
# 3.14159265359
print('|' + 'hello'.ljust(10) + '|')
# |hello     |
print('|' + 'hello'.center(11, '-') + '|')
# |---hello---|

# --- old % formatting ---
print('The value of pi is approximately %5.3f.' % math.pi)
# The value of pi is approximately 3.142.


# ===== 2) READING AND WRITING FILES =====

# open(filename, mode, encoding)
# mode: 'r' read, 'w' write (overwrites!), 'a' append, 'r+' read+write

# create the file for later examples
f = open('workfile', 'w', encoding='utf-8')
f.write('This is the entire file.\n')
f.write('This is the first line of the file.\n')
f.write('Second line of the file\n')
f.close()
print('workfile created')
# workfile created

# with ... as ... : closes the file automatically
with open('workfile', encoding='utf-8') as f:
    read_data = f.read()

print(f.closed)  # True -> auto-closed by with
# True
print(read_data)
# This is the entire file.
# This is the first line of the file.
# Second line of the file

# f.read() reads the whole file; at the end it returns ''
f = open('workfile', encoding='utf-8')
print(repr(f.read()))
# 'This is the entire file.\nThis is the first line of the file.\nSecond line of the file\n'
print(repr(f.read()))
# ''
f.close()

# f.readline() reads one line (the \n stays at the end)
f = open('workfile', encoding='utf-8')
print(repr(f.readline()))
# 'This is the entire file.\n'
print(repr(f.readline()))
# 'This is the first line of the file.\n'
print(repr(f.readline()))
# 'Second line of the file\n'
f.close()

# loop over the file, line by line
f = open('workfile', encoding='utf-8')
for line in f:
    print(line, end='')
f.close()
# This is the entire file.
# This is the first line of the file.
# Second line of the file

# f.write() returns the number of characters written
f = open('workfile', 'w', encoding='utf-8')
print(f.write('This is a test\n'))  # 15
# 15
value = ('the answer', 42)
s = str(value)  # convert the tuple to a string first
print(f.write(s))  # 18
# 18
f.close()

# f.tell() = current position, f.seek(offset, origin) = move
# first reset the file with empty binary content
f = open('workfile', 'wb')
f.write(b'0123456789abcdef')
f.close()

f = open('workfile', 'rb+')
f.seek(5)       # go to byte 6 (origin 0 = start, default)
print(f.read(1))  # b'5'
# b'5'
f.seek(-3, 2)   # origin 2 = end -> 3 bytes before the end
print(f.read(1))  # b'd'
# b'd'
f.close()


# ===== 2.1 JSON: save structured data =====

import json

# dumps(): convert a Python object to a JSON string
x = [1, 'simple', 'list']
print(json.dumps(x))
# [1, "simple", "list"]

# dump(): write it into a file
with open('workfile.json', 'w', encoding='utf-8') as f:
    json.dump(x, f)

# load(): read it back from the file
with open('workfile.json', encoding='utf-8') as f:
    y = json.load(f)
print(y)
# [1, 'simple', 'list']

# dicts work too
data = {'name': 'Youco', 'scores': [12, 15, 9]}
print(json.dumps(data))
# {"name": "Youco", "scores": [12, 15, 9]}


# ===== DAY 04 (suite) - FILE I/O IN PRACTICE =====
# most biological data is stored as TEXT in files.
# let's read and write those files, like the book shows.


# --- create the example file animaux.txt ---
with open("animaux.txt", "w") as f:
    f.write("girafe\ntigre\nsinge\nsouris\n")


# --- .readlines(): a LIST of all the lines (each with its \n) ---

filin = open("animaux.txt", "r")      # open the file
print(filin.readlines())              # read ALL lines -> a list
# ['girafe\n', 'tigre\n', 'singe\n', 'souris\n']
filin.close()                         # close it (a closed book)
# filin.readlines()  # -> ValueError: I/O operation on closed file.


# --- complete example: read, loop, print ---

filin = open("animaux.txt", "r")
lignes = filin.readlines()
for ligne in lignes:
    print(ligne)      # print adds a newline + the file has \n -> blank lines
filin.close()
# girafe
# (blank)
# tigre
# (blank)
# singe
# (blank)
# souris
# (blank)


# --- same example with "with": auto close ---

with open("animaux.txt", "r") as filin:
    lignes = filin.readlines()
    for ligne in lignes:
        print(ligne)
# same output as above


# --- .read(): the WHOLE content as ONE string ---

with open("animaux.txt", "r") as filin:
    print(repr(filin.read()))
# 'girafe\ntigre\nsinge\nsouris\n'


# --- .readline(): ONE line each call, used with while ---

with open("animaux.txt", "r") as filin:
    ligne = filin.readline()
    while ligne != "":       # "" = end of file
        print(ligne)
        ligne = filin.readline()
# girafe
# ...
# souris


# --- direct iteration: the preferred way ---

with open("animaux.txt", "r") as filin:
    for ligne in filin:
        print(ligne)
# girafe
# ...
# souris


# ===== 7.2 WRITING INTO A FILE =====

animaux2 = ["poisson", "abeille", "chat"]
with open("animaux2.txt", "w") as filout:
    for animal in animaux2:
        filout.write(animal)   # no newline -> everything on ONE line!

with open("animaux2.txt", "r") as f:
    print(repr(f.read()))
# 'poissonabeillechat'

# better: add the line break with an f-string
animaux2 = ["poisson", "abeille", "chat"]
with open("animaux2.txt", "w") as filout:
    for animal in animaux2:
        filout.write(f"{animal}\n")

with open("animaux2.txt", "r") as f:
    print(f.read())
# poisson
# abeille
# chat


# ===== 7.3 TWO FILES IN ONE "with" =====

with open("animaux.txt", "r") as fichier1, open("animaux3.txt", "w") as fichier2:
    for ligne in fichier1:
        fichier2.write("* " + ligne)

with open("animaux3.txt", "r") as f:
    print(f.read())
# * girafe
# * tigre
# * singe
# * souris


# ===== 7.5 TYPES: file content is ALWAYS strings =====
# numbers in a file come back as strings -> convert with float() / int()
# if you need to use them in math operations.

with open("notes.txt", "w") as f:
    f.write("13.5\n17.0\n9.5\n12.0\n10.0\n")

notes = []
with open("notes.txt", "r") as f:
    for ligne in f:
        notes.append(float(ligne.strip()))  # strip() removes the \n

print(notes)
# [13.5, 17.0, 9.5, 12.0, 10.0]
print(sum(notes))   # file lines were strings, now they are numbers
# 62.0


# ===== 7.7.1 EXERCISE 1: average of the grades =====

notes = []
with open("notes.txt", "r") as f:
    for ligne in f:
        notes.append(float(ligne.strip()))

moyenne = sum(notes) / len(notes)
print(f"moyenne = {moyenne:.2f}")
# moyenne = 12.40


# ===== 7.7.2 EXERCISE 2: admis (pass) or recalé (fail) =====

with open("notes2.txt", "w") as f_out:
    for note in notes:
        if note >= 10.0:
            f_out.write(f"{note:.1f} admis\n")
        else:
            f_out.write(f"{note:.1f} recalé\n")

# show the new file
with open("notes2.txt", "r") as f:
    for ligne in f:
        print(ligne, end="")
# 13.5 admis
# 17.0 admis
# 9.5 recalé
# 12.0 admis
# 10.0 admis


# ===== 7.7.3 EXERCISE +++: two-dimensional spiral =====

import math

# x = r * cos(theta), y = r * sin(theta)
# theta goes from 0 to 4*pi (two full turns), r grows from 0.5 by 0.1
with open("spirale.dat", "w") as f:
    r = 0.5
    theta = 0.0
    while theta <= 4 * math.pi:
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        f.write(f"{x:10.5f} {y:10.5f}\n")
        r += 0.1
        theta += 0.1

# show the first 6 lines of spirale.dat
with open("spirale.dat", "r") as f:
    for i, ligne in enumerate(f):
        if i < 6:
            print(ligne, end="")
#    0.50000    0.00000
#    0.59700    0.05990
#    0.68605    0.13907
#    0.76427    0.23642
#    0.82895    0.35048
#    0.87758    0.47943

with open("spirale.dat", "r") as f:
    print(len(f.readlines()))  # number of points
# 126