

import math
mean1=0
mean1=0

def deviation(values):
    sumofmultiply = 0
    for i in values:
        multiply = abs(i - mean1)
        sumofmultiply = sumofmultiply + multiply
    global dev
    dev = (sumofmultiply/len(values))

def sum_of_list(values):
    sum = 0
    for i in values:
        sum = sum + i
    return sum

def mean(values):
    global mean1
    sum_of_list(values)
    mean1 = sum_of_list(values)/(len(values))
    

def summeandeviation():
    mean(values)
    deviation(values)
    print (mean1, "+-", dev)


n = 1
values = []
while n != 0:
    n = float(input("Type the values, if you want to finish, type 0: "))
    if n != 0:
        values.append(n)

summeandeviation()



