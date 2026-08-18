for i in [1, 2, 4, 9, 3]:
    print(i , "\n")

for i in range(7): # range function can be used with two or three arguments, range(start included, end excluded)
    print(i, "\n")

c = ["Full", "-", "Stack", "Developer"]
print(len(c))
for i in range(len(c)):
    print("i = ", i, ", c[i] = ", c[i])
print("ENDFOR i in range(len(c))\n")
for i in c:
    print(i)
print("ENDFOR i in c\n")

x =  1
while x < 10:
    print("x = ", x)
    x += 2 
print("ENDWHILE\n")
i = 0 
while i < len(c):
    print(c[i])
    i += 1
print("ENDWHILE i < len(c)")

j = 0
while True:
    print(c[j])
    if c[j] == "-":
        break
    j += 1
print("ENDWHILE True")


# ===== FUNCTIONS =====

# A function is a block of code that we can CALL (run) many times.
# This is the "anatomy" of a function - one part on each line:

def add(a, b):
    return a + b

# 1. def       -> the keyword: it creates (defines) the function
# 2. add       -> the NAME of the function (you choose it)
# 3. (a, b)    -> the PARAMETERS: the inputs the function receives
# 4. :         -> the header ends with a colon
# 5. body      -> the indented code that runs when we call it
# 6. return    -> gives BACK a result, so we can store it

# Call a function: write its name followed by ( ) with the inputs
result = add(3, 5)
print(result)       # 8
print(add(10, 20))  # 30

# a function without parameters (no inputs)
def greet():
    print("Hello!")

greet()
greet()  # we can call it as many times as we want

# a function with one parameter: the input is used inside the body
def greet_user(name):
    print("Hello", name)

greet_user("Youco")
greet_user("Moussa")

# a function that returns a value, so we can use the result
def multiply(a, b):
    return a * b

total = multiply(4, 5)
print(total)              # 20
print(multiply(2, 3))     # 6

