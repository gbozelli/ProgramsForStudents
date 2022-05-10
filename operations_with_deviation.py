
def multiplication_of(a,b,c,d):
    value = a * c
    error = ((a * b) + (c * d))
    print(value, "+-", error)

def sum_of(a,b,c,d):
    value = a + c 
    error = b + d
    print(value, "+-", error)
    
def division_of(a,b,c,d):
    value = a/c
    error = ((a*c)+(b*d))/(c*c)
    print(value, "+-", error)

def multiplication_by_k(a,k,b):
    value = k*a
    error = k*b
    print(value, "+-", error)

def difference_of(a,b,c,d):
    value = a - c
    error = b - d
    print(value, "+-", error)

print("Type the correspondent number if you:")
print("1 - Want to  evaluate a sum")
print("2 - Want to  evaluate a difference")
print("3 - Want to  evaluate a multiplication")
print("4 - Want to  evaluate a division")
print("5 - Want to  evaluate a multiplication by a constant")
number = int(input(""))
a = int(input("Type the first value: "))
b = int(input("Type the first error: "))
c = int(input("Type the second value: "))
d = int(input("Type the second error: "))
if number == 1:
    sum_of(a,b,c,d)
if number == 2:
    difference_of(a,b,c,d)
if number == 1:
    multiplication_of(a,b,c,d)
if number == 1:
    division_of(a,b,c,d)
if number == 1:
    multiplication_by_k(a,b,c,d)
