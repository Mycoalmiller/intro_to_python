# Summary 

# 1. 

my_name = 'michael ' + 'miller'
print(my_name)


# 2. 

my_list = "4936"
print('One place is ' + my_list[3])
print('Tens place is ' + my_list[2])
print('Hundres place is ' + my_list[1])
print('Thousands place is ' + my_list[0])

# 3. 

# The following code combines the 2 strings into '510'. 
# because they are strings and not integers. 

# 4. 

print(5 + 10)

# 5. 

# Yes, because foo[3] asks for the fourth letter in the word 
# when there are only 3 letters in the word 

# 6. 

# False. its not equal because of the difference in caps 

# 7. 

# an error. it's not a integer, its a float value 

# 8. 

# it only compares the first number in the string. 
# Therefore, the boolean value would be true. 

# Arithmetic Operations

print (38 + 41.5) 
# 79.5 - integers and float can be combined

print (38 - 41.9) 
# -3.5 - can have a negative number

print (16 // 3) # 5
print (16 // -3 ) # -6 

# rounds down, -5.33 was rounded down to -6 

print (3**4)  #4096 

# 3 to the 4th power

print (15 % 3) # 0
print (17 % 3) # 2

# prints the remaining numbers 

# floating point imprecision

print(0.1 + 0.2 == 0.3) # false

import math 
math.isclose(0.1 + 0.2, 0.3)

from Decimal import Decimal
Decimal('0.1') + Decimal('0.2') == Decimal('0.3')
# must use this when you want to do precise math
 
# equality comparison 

print (42 == 43) # false
print ('foo' == 'Foo') # false 
# comparison does work with strings and not 

print (42 != 43) # true 
# works as a 'does not equal' operator 

print ('3' < '24') # false
print ('24' < '3') # true 

# only the first number in the string are compared 

print('A' , 'a')  # true

# based on the order in the ascll chart 

print([1,3,3] < [1,4,3]) 

# true - compares the sum number of each lists

# String Concatenation

'foo' + 'bar'
'foobar'

# combines the string 

'1' + '2'

# 12 - combines the numbers because theyre strings, doesnt do the math

print( 'abc' * 3) 

# abcabcabc

# Coercion

print(int('5'))   

# 5 - prints it out as an integer

print(float('3.1415')) 

# 3.1415 - converts string to float 

print(str(5)) 

# '5' - turns it into a string

foo = 42
print(type(foo))

# <class 'int'> 

print(type('abc').__name__) 

# str

print(type('abc') is str)

# True 

print(type([]) is list)

# True 
# is a boolean value comparison

print(isinstance ('abc', str))

# True

print(isinstance([], set)) 

# False 
# asks if the value is a type of class type, returns boolean value

# String Representations

my_str = 'abc'
print(my_str) # abc
print(str(my_str)) # abc
print(repr(my_str)) # 'abc' 

# Collection and String Lengths 

print(len(range(5,15))) 

# 10

print(len({'foo' : 42, 'bar' : 7}))

# 2 - because its a dictionary 

# Indexing and key Access

my_str = 'abc'
print(my_str[0])

# a 

my_list = [1,2,3,4]
my_list[2] = 6 
print(my_list)

# change the value in a list 

# Expressions and Statements

# expression evaluation 

1 + 2 + 3 + 4 + 5 

# 15

# output and return values 

