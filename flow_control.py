# 1. 

False or (True and False) # false 
True or (1+2) # true 
(1+2) or True # 3 
True and (1+2) # 3 
False and (1+2) # false 
(1+2) and True # true 
( 32  * 4) >= 129 # false 
False != (not True) # false 
True == 4 # false 
False == (847 == '847') # true

# 2. 

a = 2 
def even_or_odd(a):
    if a % 2 == 0:
        print('even')
    else: 
        print('odd')

# 3. 
# product2 and product not found 
# the case_ is the default if what enteres doesn't match

# 4. 

if foo():
   return 'bar'
else: 
    return qux()

# 5. 

# empty - [] is a falsy value, isnt recognized as a parameter 

# 6. 

def count_word (count): 
    if len(count) > 10: 
        return count.upper() 
    else: 
        return count

print(count_word('hello everyone'))

# 7. 

def count(number): 
    if number < 0 : 
        print('the value is less than 0')
    elif number <= 50: 
        print('the value is between 0 and 50')
    elif number <= 100: 
        print('the value is between 51 and 100')
    else: 
        print('number is greater than 100')

print(count(4))


value = int(input('enter a number:'))

if value == 3: 
    print('value is 3')

# if i enter 3 it prints it, if i put 4 it's empty 

value = int(input('enter a number: '))

if value == 3: 
    print('value is 3')
else: 
    print('value is not 3')

# prints value is not 3 this time

value = int(input('enter a number:'))

if value == 3: 
    print('value is 3')
else: 
    if value == 4: 
        print('value is 4')
    else: 
        print('value is not 3 or 4')

# prints it out based on the number i put in
 
value = int(input('enter a number:'))

if value == 3: 
    print('value is 3')
elif value == 4: 
    print('value is 4')
else: 
    print('value is not 3 or 4')

# there can be multiple elif statements

if value == 3: 
    print('value is 3')
elif value == 4: 
    print('value is 4')
elif value == 9: 
    pass 
else: 
    print('value is something else')

print('abc'.upper() == 'aBc'.upper())

# prints true
# truthy vs falsy is if theres something there or not. ie: is there value

!= is the opposite of ==

print (not True) 

# false 

print (not(4 == 4))

# false 

# not flips the boolean value 

print(1 and 2 or 3 )
print ((a and b) or (c and d))

value = 5 

match value: 
    case 5: 
        print('value is 5')
    case 6: 
        print('value is 6')
    case _: # default case 
        print('valuse is neither 5 or 6')

# value is 5 
# match and case are reserved words 

value = 5 

if value == 5: 
    print ('value is 5')
elif value == 6: 
    print ('value is 6')
else: 
    print('value is neither 5 or 6')
# value is 5 

value = 5

match value: 
    case 1 | 2 | 3 | 4: 
        print('value is <5 ')
    case 5 | 6: 
        print('value is 5 or 6')
    case _: 
        print( 'value is not from 1 to 6')
# value is 5 or 6

value1 if condition else value2

# it's better read 

(value1 if condition) else value2

# if its truthy, if statement is used, if falsy - else statement

print('triangle' if shape.sides() == 3 else 'square')

# runs the if statement, if it doesnt match, defaults to else 

