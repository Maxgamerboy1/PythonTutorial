print("HelloWorld")

# Defining a function


def add_nums(a: int, b: int) -> int:
    return a+b


print(add_nums(5, 5))

aNumber = 1
aString = 'Hello'

# How awesome is Python
# f"hello {name}" --string interpolation
# None is similar to null

if aNumber == 1 and aString:
    print("aNumber is 1 and aString is not None")

# Ternary statement
a = 50
b = 10
print("bigger" if a > b else "smaller")

# Lists
names = ["Andy", "Billy", "Charlie", "Dan"]
print(names[1])  # 0-index based
print(names[-1])  # Get last
names.append("Ellie")  # Add to the end
print(names[-1])  # Get last
print("Yes" if "B" in names else "Nope")  # ternary to check if there is 'B' in names
del names[2]  # delete
print(len(names))  # gets length of names
print(names[2:])  # ignore all elements before index 2, give the rest

# Loops
for name in names:
    print(f"The name is: {name}")
#        start, stop, increment
for i in range(2, 10, 2):
    print(i)

for nname in names:
    if len(nname) == 7:
        break
    elif len(nname) == 5:
        continue
    else:
        print(nname)

x = 0
while x < 10:
    print(x)
    x += 1

# Dictionaries
book = {
    "Title": "Harry Potter",
    "Author": "J.K.Rowling",
    "BookAge": 2
}
print(book["Title"])

print()

print("Done")
