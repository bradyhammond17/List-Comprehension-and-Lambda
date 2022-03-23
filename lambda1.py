from audioop import add
from cgi import test
import numbers


remainder = lambda num: num % 2
print(remainder(5))


product = lambda x,y: x*y
print(product(2,3))


def testfunc(num):
    print(num)
    return lambda x: x * num

#can create two functions from this one function
#multiplies any number by 10
result10 = testfunc(10)

#multiplies any number by 100
result100 = testfunc(100)

print(result10)
print(result100)

#takes argument in parentheses and multiplies by 10/100
print(result10(9))
print(result100(9))

result10 = lambda x: x * 10
result100 = lambda x: x * 100

print(result10(9))
print(result100(9))

def myfunc2(n):
    return lambda a: a*n

mydoubler = myfunc2(2)
mytripler = myfunc2(3)

print(mydoubler(11))
print(mytripler(11))

#filters list, needs a function and a list as arguments
numbered_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]
filtered_list = list(filter(lambda num: (num > 7), numbered_list))
print(filtered_list)


def addition(n):
    return n + n 
numbers = [1,2,3,4]
result = map(addition, numbers)
print(list(result))

#maps each element in a list and applies a function to each element in that list
result = list(map(lambda n: n + n, numbers))
print(result)

import os

clear = lambda: os.system("cls")
clear()