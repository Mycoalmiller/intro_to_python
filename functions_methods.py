# 1. 

def set_foo(): 
    foo = 'bar'

set_foo()
print(foo)

# no variable of foo in the scope

# 2. 

foo = 'bar'

def set_foo(): 
    foo = 'qux'

set_foo()
print(foo)

# prints bar, isnt called to print in set_foo()

# 3. 

number1 = input('whats the first number?')
number1 = int(float(number1))
number2 = input('whats the second number?')
number2 = int(float(number2))
print((number1),  '*',  (number2), '=', (number1 * number2))

# 4. 

def multiply_numbers(num1, num2, num3): 
    result = num1 * num2 * num3 
    return result 

product = multiply_numbers(2,3,4)

# function name = multiply_numbers, product
# function arguments = (2,3,4)
# function definition = def multiply_numbers(num1, num2, num3): 
    # result = num1 * num2 * num3 
    # return result 
# function body = 
    # result = num1 * num2 * num3 
   #  return result 
# function parameters = num1, num2, num3 
# function invocation = multiply_numbers(2,3,4)
# function return value = 24
# all identifiers = multiply_numbers, num1, num2, num3, result, product

# 5. 

def scream(words): 
    return words + '!!!'

scream('yipeee')

# will add yipeee and !!! together, but doesnt print it

# 6. 

def scream(words): 
    words = words + '!!'
    return 
    print(words)

scream('yipee')

# wont print it, return stops the function

# 7. 
def foo(bar,qux): 
    print(bar)
    print(qux)

foo('hello')

# an error, only 1 function argument is defined

# 8. 

def foo(bar, qux):
    print(bar)
    print(qux)

foo(34,34,34)

# error, 3 function arguments, when 2 unction parameters are defined

# 9. 

def foo(first, second=3, third=2): 
    print(first)
    print(second)
    print(third)

foo (23, 34, 34)

# prints 23, 34, 34 - doesnt print 3 as second=3 because its a parameter, and the variable was redefined

# 10. 

def foo(first, second=3, third=2): 
    print(first)
    print(second)
    print(third)

foo(42, 42)

# prints 42, 42, 2

# 11. 

def foo(first, second=3, third=2): 
    print(first)
    print(second)
    print(third)

foo(42)

# Prints 42, 3, 2

# 12. 

def foo(first, second=3, third=2): 
    print(first)
    print(second)
    print(third)

foo()

# no arguments to do anything with

# 13. 

def foo(first, second=3, third): 
    print(first)
    print(second)
    print(third)

foo(42)

# 14. 

# multiply 
# left 
# right 
# get_num 
# prompt
# first_number 
# second_number 
# product 
# print 
# float 
# input

# 15. 

# global = multiply, get_num, left, right, prompt,
# local = left, right, prompt, 
# built in = float, print, input

# 16. 

function name = 
multiply line 1 
get_num line 4
first_number line 7
second_number line 8 
product line 9 

parameters = 
left, right line 1
prompt line 4

# 17. 
function name - say 
method names - upper and lower # used with a variable, ie: a method to organize it 
build in - print, input, max

# 18.

def remainders_3(numbers): 
    return(number % 3 for number in numbers)

# number in numbers compares the values 

def hello():
    print('Hello')
    return True 

hello()
print(hello(hello))

print(print())

# prints none - because there arent any values 

print(max(-10, 3, 8))

# 8 

print(min(-10, 3, 8))

# -10

my_list = (1,2,3,4)
print(min(my_list))
print(max(my_list))

# 1 & 4

print(ord('s'))

#115

print(chr(97))

# a 

numbers = [2, 5, 8, 10, 13]
print([number % 2 == 0 for number in numbers])

# asks if its even - if so its a boolean statement

s = 'hello world'
t = 'hello world'
print(id(s) == id(t))

# used to make programs run faster

help()

help(ord)
help('topics')
help('BOOLEAN')

# gives help prompts

def func_name(): 
    func_body

# outline of making a function

def say(): 
    print('hello world')

print('first')
say()
print('second')

# print in the function body is whats executed

def say(): 
    """ 
    hello hello 
    """
    print('hi')

print('-' * 60)
print(say.__doc__)
print('-' * 60)
help(say)

# say.__doc__ calls the function, and states the doc info with 
# the """

greeting = 'hello'

def well_howdy(who):
    print(f'{greeting}, {who}')

well_howdy('michael')
print(greeting)

# variables in the def body cant be called outside of it

def scope_test():
    if True: 
        foo = 'hello'
    else: 
        bar = 'there'
    
    print(foo)
    print(bar)

scope_test()

# creates an error message, because bar was never defined
# since else block never ran 

def say(text):
    print('==> ' + text)

say('hello')
say('hi')
say('how do you do')
say('quite all right')

def add (left, right): 
    sum = left + right
    return sum 

sum = add (3,6)
# it returns 9 but doesnt print it

def is_digit(char):
    if char >= '0' and char <= '9': 
        return True
    
    return False

def say(text='hello'): 
    print(text + '!')

say('hi')
say()

# if there are no paramaters entered, the default is 
# the original parameters 

def say(hello, hello='world'): 
    pass

def say(msg1, msg2, msg3): 
    print(msg1)
    print(msg2)
    print(msg3)
    
say('a','b','c')

# can call different things in a functions paramaters

my_str = "def-mno"
print(my_str.upper())

# makes it uppercase 

def add_new_number (my_list): 
    my_list.append (9)

numbers = [1,2,3,4,5]
add_new_number(numbers)
print(numbers)

# numbers list is outside the function body

def add_new_number (my_list): 
    return my_list + [9]

numbers = [1,2,3,4,5]
new_numbers = add_new_number(numbers)
print(new_numbers)
print(numbers)

# new_numbers takes my_list and runs add_new_number, adding 
# 9 to the end