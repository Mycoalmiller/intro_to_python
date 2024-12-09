# 1. 
print('whats your name?')
name = input()

print(f'good morning, {name}!')

# 2. 

sum1 = input('what is your first name?')
sum2 = input('what is your last name?')
sum = sum1 + '' + sum2
print (f'hello {sum}')

# 3. 

age = input( 'how old are you?')
age = int(float(age))

print( f' you are {age} years old '
    f' in 10 years, you will be {age + 10} '
    f' in 20 years, you will be {age + 20} '
    f' in 30 years, you will be {age + 30} '
    f' in 40 years, you will be {age + 40} ' )

name = 'jane'
print(f'good morning, {name}!')

print ({
    'a' : 1, 
    'b' : {8,9,10}
})

# can have sets within sets

import time 
print(time.asctime())

print ([1], 4, False, {2,3})

# can print different data types at the same time

print(1,2,3, sep=',')

# 1,2,3

print('a', 'b', 'c', sep='')

# abc 

print('whats your name?')
name = input()

print(f'good morning, {name}!')


name = input('whats your name?')

print(f'good morning {name}!')

# has the question in the prompt bar 

number1 = input ('first number')
number2 = input ('second number')
sum = int(number1) + int(number2) 

print(f'the numbers {number1} and {number2} '
      f'add to {sum} ')
