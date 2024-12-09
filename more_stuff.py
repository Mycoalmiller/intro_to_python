# 1. 

# CHRIS 

# 2. 

import math 

print(math.sqrt(37))

import math as m

print(m.sqrt(37))

from math import sqrt 

print(sqrt(37))

import math 

def sqrt(a): 
    print(math.sqrt(a))

sqrt(37)

# 3. 

def sum_of_squares (num1,num2): 
    def square(number): 
        return number * number
        

    return square(num1) + square(num2)

print(sum_of_squares(3,4))
print(sum_of_squares(5,12))

# 4. 

counter = 0 

def increment_counter(): 
    global counter 
    counter += 1 

print(increment_counter())

# 5. 

def all_actions(): 
    def increment_counter(): 
        nonlocal counter
        counter += 1 

    counter = 0
    print(counter)

    increment_counter() 
    print(counter)

    counter = 100
    increment_counter() 
    print(counter)
all_actions()





def add(a,b): 
    return a + b 

def subtract(a,b): 
    return a - b 

sum = add(20,45)
print(sum)

difference = subtract(80,10)
print(difference)

# the function with a return is almost a method

def add(a,b): 
    return a + b 

def subtract(a,b): 
    return a - b

def times(num1,num2): 
    return num1 * num2

print(times(add(2,2), subtract(6,2)))

total = add(2,2)
difference = subtract(6,2)
result = times(total,difference)
print(result)

tv_show = 'hello world today'
tv_show = tv_show.upper().split()
print(tv_show)

tv_show = 'hello world today'
tv_show = tv_show.replace('w', '')
print(tv_show)

import math 

# imports the whole module

from math import pi, sqrt 

# imports just the pi and sqrt functions 

import math as m 

# m is now the name when referencing math 

import math 
print(math.sqrt(36))
print(math.sqrt(2))
print(math.pi)

from datetime import datetime as dt 

date = dt.strptime("june 16, 1995", "%B %d, %Y")
weekday_name = date.strftime('%A')
print(weekday_name)

def top(): 
    bottom()

def bottom(): 
    print('you reached the bottom')

top()

def foo(): 
    def bar(): 
        print('Bar')

    bar()
foo()

greeting = 'hello'

def well_howdy(who): 
    global greeting 
    print(f'{greeting}, {who}')

well_howdy('michaeal')
print(greeting)

# greeting variables are independent of each other 

def set_pi(): 
    global pi 
    pi = 3.1415

set_pi() 
print(pi)

# the set_pi was ran, made the global variable pi 
# pi printed as the value defined 

def outer(): 
    def inner1(): 
        def inner2 ():
            nonlocal foo 
            foo = 3 
            print(f'inner2 -> {foo} with id {id(foo)}')

        nonlocal foo 
        foo = 2
        inner2() 
        print(f'inner -> {foo} with id {id(foo)}')
    foo = 1 
    inner1() 
    print(f'outer -> {foo} with id {id(foo)}')   

outer() 
# print(f'global -> {foo} with id {id(foo)}')

# global value defined and called 
# on when nested globally

# nonlocal excuses 