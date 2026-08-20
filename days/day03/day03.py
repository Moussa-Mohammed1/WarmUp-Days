# ===== DATA STRUCTURES =====
# a data structure is a way to GROUP data together.
# Python has: lists [ ], tuples ( ), dicts { }, sets { }

# ----- TUPLE -----
# a tuple is like a list, but it CANNOT be changed (immutable)
# we write it with ( ) instead of [ ]

point = (3, 4)
print(point)       # (3, 4)
print(point[0])    # 3
print(len(point))  # 2

# we can unpack a tuple into variables
x, y = point
print(x, y)        # 3 4

# point[0] = 10  # -> TypeError: 'tuple' object does not support item assignment


# ----- DICT -----
# a dict stores KEY -> VALUE pairs
# we write it with { } and separate key and value with :

person = {
    "name": "Youco",
    "age": 25,
    "skills": ["Python", "HTML"]
}

print(person["name"])   # Youco
print(person["age"])    # 25

# add or change a pair
person["city"] = "Oran"
print(person)   # {..., 'city': 'Oran'}

# check if a key exists with 'in'
print("name" in person)   # True

# loop over the keys
for key in person:
    print(key, "->", person[key])


# ----- SET -----
# a set is a collection of UNIQUE elements, with NO order
# we write it with { }, but no key -> value

fruits = {"apple", "banana", "apple", "orange"}
print(fruits)  # {'banana', 'apple', 'orange'} -> "apple" appears only ONCE

# check if an element is inside
print("apple" in fruits)   # True

# add an element
fruits.add("kiwi")
print(fruits)

# remove an element
fruits.remove("banana")
print(fruits)