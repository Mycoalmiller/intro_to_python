"hello world" # str literal
3.1415926     # float literal
True          # bool literl 
{'a': 1, 'b': 2} # dict literal
[1,2,3]      # list literal
(4,5,6)       # tuple literal
{7,8,9}      # set literal

range(10) # range of numbers: 0-9
range(1,11) # range of numbers: 1-10
set()     # empty set
frozenset([1,2]) # frozen set of values: 1 and 2

# Numberic Values

2 #integer
-2 #integer 
123_456 #integer

1.0 # float_
3.14 # float
-3.14 # float
-123_456.789

import sys 

print(sys.float_info.dig)
# max number of digits that can be presented accurately 

print(sys.float_info.max)
# largest possible float value 

print(sys.float_info.min)
# smallest non zero positive float value 

print(3.14 * (10**20)) 
# 3.14 with 20 zeros 

print(3.14 * (10**-20))
# 3.14 with 20 negative zeros, ie: a very small decimal

print(3.14e+20 / 2.72e-15) #1.14e+35

print(3 * (10**20))
# same as
print(int(3e+20))

# Variables and Assignment

pi = 3.14
meaning_of_the_universe = 42

# the left is the variable, the right is the value

a = 4 
# assignment or initialization 

a = 2 
# reassignment

# Boolean Values
 
toggle_on = True 
session_active = False

# Text Sequence 

'hello'

greeting = 'hello'
for letter in greeting: 
    print (letter)

# prints each letter of hello to a row

'hello' # single quote
"hello" # double quotes

''' hello "world" 
today is friday ''' # triple single quotes

""" hello "world" 
today is friday """ # triple double quotes


print( """ my nickname is "troy". what's yours?""")
print( 'my nickname is "troy". what\'s yours?')
print("my nickname is \"troy\". what's yours? ")

print("C:\\users\\michael") # each \\ produces a literal \

my_str = 'abc'
my_str [0]

# prints out the letter a 

my_str [-1]

# last character, which is c

my_str [-2] 

# second to last character, which is b

# raw strings and f strings 

print( "C:\\users\\michael") # each \\ produces a literal \ 
print( r"C:\users\michael") # raw string literal , with the r the \\ arent needed

f'5 plus 5 equals {5 + 5}.'

# '5 plus 5 equals 10.' 
# good way to merge expressions with strings 

f'blah {expression} blah.'

# basic syntax of it

{}

# what a literal string looks like "literally"

print(f'{123456789:_}') # 123_456_789
print(f'{123456789:,}') # 123,456,789

# sequences 

my_list = [1, 'hello', [2,3]]

# list literal

tup = ('hello', [3,4], True)

# tuple literal
# lists can be changed, tuples cant

tup = (1,)

# must have the , or else its viewed as an expression 

tuple(range(5))

# (0,1,2,3,4)

list(range(1,10,2))

# [1,3,5,7,9]

my_range = range(5,10)
my_range [3]

# 8 

# mappings

my_dict = {
    'page 1': 'introduction',
    'page 2': 'same thing as page 1',
}

my_dict['page 2'] = 'introduction part 2'

print (my_dict)

print (my_dict['page 2'])

print (my_dict['page 1'])

# {'page 1': 'introduction', 'page 2': 'same thing as page 1'}
# introduction part 2
# introduction

dic = {}
dic['c'] = 1
dic['e'] = 2 
print (dic) 
# {'c': 1, 'e': 2}
del dic['c']
dic['c'] = 1 
print(dic)
# {'e': 2, 'c': 1} changes the order of the set range

my_dict = {
    'hello': 'world'
    'people involved': 
    ['michael',]
}

# can have nested list literals within a set dictionary

# sets 

d1 = {}
print(type(d1))
# <class 'dict'>
# empty dict 

s1 = set()
print(s1)
# set()
# empty set 

s2= {2,3,5,7,11,13}
print(s2)
{2,3,5,7,11,13}
# creates a set from a literal , with out the use of range 

s3 = set('hello')
print(s3)
{'h', 'o', 'l', 'e'}
# create a set from a string
# the order has nothing to do with the string

set_literal = {
    'example 1', 
    'example 2',
}
# set literal with a multi lines 

s5 = frozenset([1,2,3])
print(s5)

s6 = frozenset((1,2,3))
print(s6)

s7 = frozenset({1,2,3})
print(s7)

s8 = frozenset(range(1,4))
print(s8)

# frozenset({1,2,3}) - they all print the same thing

# exercises

# 1. identify the data type or class for each of the following values:

'True'           # string, str
False =          # boolean, bool
(1, 2, 3)        # tuple literal, tuple
1.5              # float, float
[1, 2, 3]        # list literal, list 
2                # integer, int
range(5)         # range, range
{1, 2, 3}        # set literal, set
None             # nonetype, nonetype
{'foo': 'bar'}   # dictionary, dict

# 2. Create a tuple called names that contains several pet names. For instance:

names = ('john', 'toa', 'renley')


# 3. Create a dictionary named pets that contains a list of pet names and the type of animal. For instance:

pets = {
    'asta' : 'dog', 
    'butterscotch' : 'cat', 
    'pudding' : 'cat', 
    'neptune' : 'fish', 
    'darwin' : 'lizard'
}