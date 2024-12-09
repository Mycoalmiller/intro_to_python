# 1. Classify the following potential non-constant variable names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.

index         # illegal - reserved word in web development
CatName       # non-idiomatic - capitals
lazy_dog      # idiomatic
quick_Fox     # idiomatic
1stCharacter  # illegal - has a number at the begining
operand2      # idiomatic
BIG_NUMBER    # non-idiomatic - capitals 
π             # illegal - reserved 

# 2. is the same as 1. 

# 3. Classify the following potential constant names as idiomatic, non-idiomatic, or illegal.
# For the non-idiomatic and illegal names, explain your choice.

index         # illegal - reserved word 
CatName       # non-idiomatic - camelcase
LAZY_DOG3     # idiomatic 
quick_Fox     # non-idiomatic - lowercase
1stCharacter  # illegal - has a number at the begining
operand2      # non-idiomatic - lowercase
BIG_NUMBER    # idiomatic  
π             # illegal - reserved 

# 4. Classify the following potential class names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.

index      # non-idiomatic - isnt camelcase
CatName    # idiomatic 
Lazy_Dog   # non-idiomatic - underscore
1ST        # illegal - starts with a digit
operand2   # non-idiomatic - not camelcase
BigNumber3 # idiomatic
Πi         # illegal - not in ascll  

# 5. 

name = 'victor'
print('Good Morning, ' + name +'.' )
print('Good Afternoon, ' + name + '.')
print('Good Evening, ' + name + '.')

# 6. 

def number(age):
    return age + 10

print('you are',  number(12),  'years old.')
print( 'In 10 years, you will be', number(22), 'years old.')
print( 'In 20 years, you will be', number(32), 'years old.')
print( 'In 30 years, you will be', number(42), 'years old.')
print( 'In 40 years, you will be', number(52), 'years old.')

# 7. 

# it runs as intended, since the string and NAME are both strings. 

# 8. 

balance = (1000 * (1.05 ** 5))
print (balance)

# 9. 

balance = 1000
balance *= (1.05 ** 5)
print(balance)

# 10. 

obj = 42

obj = 'ABcd'       # Reassign
obj.upper()        # nothing - correct syntax but needs a value to assign it to
obj = obj.lower()  # makes the letters lowercase
print(len(obj))    # northing 
obj = list(obj)    # reassignes to a list 
obj.pop()          # mutate - doesnt specify which character to take out of the list
obj[2] = 'X'       # mutate - assigns X to the 3rd letter in the list
obj.sort()         # mutate - sorts it in ascending order in the alphabet
set(obj)           # nothing - makes it a set {} but not added to a variable
obj = tuple(obj)   # makes it a tuple ()


answer_the_ultimate_question 

# snake case 

EIGHTY_SEVEN 

# naming for constants that never change 

HelloWorld 

# used for class names 

first,last = ['michael', 'miller']
print(first,last)

# assign multiple labels to multiple values 

# creating constants

PINING_FOR = 'abcd'

# for variables that never change

# expressions and assignment 

left_side = 5
right_side = 32
total = left_side + right_side 
print(total)

# 37 

def square(number): 
    return number * number 

forty_two_squared = square(42)
print(forty_two_squared)

# 1764
# define a def with a word and () 
# return value is whats inside the def body
# assign a number inside the ()
# print results 

# augmented assignment

foo = 5 
foo *= 5
print(foo)

# the *= is an assignment operator, and is easier than 
# writting out the whole thing  

bar = 'abc'
bar += 'xyz'
print(bar)

# can add strings together too
# can be used on lists and sets 


my_list[1] = 42
my_dict['b'] = 3
my_list = [2,3,4]
my_dict = {'x': 0 }

# can reassign and change values and labels in a variable

