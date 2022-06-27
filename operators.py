#simple o[erations on variables types

seven = 7
three = 3
ten = seven + three
print(ten)

#concatenate strings

firstWord = "Hello"
secondWord = " Grey"
concat = firstWord + secondWord
print(concat)

#simple function to add multiple inputs
def add(*args):
     sum = 0
     for num in args :
         sum += num

     return sum

print(add(90, 80, 70,60, 50, 40))
