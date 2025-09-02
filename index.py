# conditional statements
x = 12
y = 20

if x < y:
    print("y is greater than x")
else:
    print("x is greater than y")

# Loop (for)

l1 = ["dsfs","dfgdfg","dfgdfg"]
for x in l1:
    print(x)

# Loop (while)

i = 5
while i<20:
    print(i)
    i = i+1

# range

tableRange = range(2,6,3)
range2 = range(1,11)

for y in tableRange:
    for x in range2:
        result = x*y
        print(y, "*", x ,"=", result)

# function

def first_Function(num):
    print("inside function",num)
first_Function(5)

# tuple 
thistuple = ("apple", "banana", "cherry")
print(thistuple)