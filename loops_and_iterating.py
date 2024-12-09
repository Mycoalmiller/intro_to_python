# 1. 

# because the counter number hasnt been increased when it iterates

# 2. 

ages = int(input('how old are you'))
print(f'you are {ages} years old.')

for future_age in range(10, 50, 10): 
    print(f'in {future_age} years, you will be {future_age + ages} years old.')

# 3. 

mylist = [6,3,0,11,20,4,17]
index = 0 

while index < len(mylist):
   print(mylist[index])
   index += 1

for char in [6,3,0,11,20,4,17]:
    print(char)

# 4. 

mylist = [6,3,0,11,20,4,17]

index = 0
while index < len(mylist):
    mylist_2 = mylist[index]
    if mylist_2 % 2 == 0: 
       print(mylist_2)

    index += 1

mylist = [6,3,0,11,20,4,17]

for number in mylist: 
    if number % 2 != 0: 
        print(number)

# 5. 

mylist = [
    [1,3,6,11], 
    [4,2,4], 
    [9,17,16,0],
]
# zipped = zip(mylist)

for list in mylist: 
    for list2 in list: 
        if list2 % 2 == 0: 
           print(list2)


# 6. 

mylist = [
    1,2,6,11,
    4,2,4,9,
    17,16,0,
]

for number in mylist: 
    if number % 2 == 0: 
        print(f'{number} is even number')
    else: 
        print(f'{number} is odd number')

mylist = [
    1,2,6,11,
    4,2,4,9,
    17,16,0,
]

result = []
for number in mylist: 
    if number % 2 == 0: 
        result.append('even')
    else: 
        result.append('odd')

print(result)

# this redos the current list, 
# rather than making a new one

# 7. 

def find_integers(my_tuple): 
    return[ element
    for element in my_tuple 
    if type(element) is int]

my_tuple = (1, 'a', '1', 3, [7], 3.1415, -4, None, {1,2,3}, False)

integers = find_integers(my_tuple)
print(integers)

# 8. 

my_set = {
    'fluffy', 
    'butterscotch', 
    'pudding', 
    'cheddar', 
    'cocoa',
}

my_set = { name: len(name)
        for name in my_set
        if len(name) % 2 != 0
        }
print(my_set)
    
# 9. 

a  = input('what is the integer?')
b = int(a)

def factorial(b): 
    result = 1
    for number in range(1, b+1):
        result *= number

    return result
    
print(factorial(b))




def fatorial(n): 
    result = 1
    while n > 0: 
        result *= n
        n -= 1

    return result 

# 10. 

import random 

highest = 10
while True: 
    number = random.randrange(highest + 1)
    print(number)
    if number == highest: 
        break 

while number != highest: 
    number = random.randrange(highest + 1)
    print(number)

# 11. 

my_list = [
    [1,3,6,11], 
    [4,2,4], 
    [9,17,16,0],
]

outer_index = 0
while outer_index < len(mylist): 
    inner_index = 0
    while inner_index < len(mylist[outer_index]):
        number = my_list[outer_index][inner_index]
        if number % 2 == 0: 
            print(number)

        inner_index += 1 

    outer_index += 1 





counter = 1
while counter <= 10: 
    print(counter)
    # counter += 1

# every time it runs, its called an iteration

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0 

while index < len(names): 
    upper_name = names[index].upper()
    upper_name.append(upper_name)
    index += 1 

print(upper_names) 

index = 0 
while index < len(collection): 
    index +=1 
# collection not defined 

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names: 
    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)

# is a for loop

for char in 'launch shool':
    print(char)

# prints launch school in a line 

for word in 'launch school'.split():
    print(word)

# splits the word and prints it

my_set = {1000, 2000, 3000, 4000, 5000}
for member in my_set: 
    print(member)

# not in a sequence becuase its from a set

my_dict = {'a':1, 'b':2, 'c':3}
for key in my_dict.keys(): 
    print(key)

my_dict = {'a':1, 'b':2, 'c': 3}
for value in my_dict.values():
    print(value)

# print out values and keys from 

my_dict = {'a':1, 'b':2, 'c':3}
for item in my_dict.items(): 
    print(item)

# uses model

my_dict = {'a':1, 'b': 2, 'c': 3}
for key,value in my_dict.items(): 
    print(f'{key} = {value}')

# print it in a better order 

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 
         'jack', 'queen', 'king', 'ace', ]
deck = []
for rank in ranks: 
    for suit in suits: 
        card = f'{rank} of {suit}'
        deck.append(card)

print(deck)

# nested for loops dont matter in this case 
# new variable is needed to be used in the nested for

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names: 
    if name == 'Max': 
        continue 

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)

# when the name is Max, skip it (continue on)

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names: 
    if name != 'Max': 
        upper_name = name.upper()
        upper_names.append(upper_name)

print(upper_names)

# != can be used in place of continue 

numbers = [3,1,5,9,2,6,4,7]
found_item = -1
index = 0

while index < len(numbers): 
    if numbers[index] == 5: 
        found_item = index
        break
    index += 1 

print(found_item)

keep_going = True 
while keep_going: 
    answer = input('play again? (y/n)')
    if answer == 'n': 
        keep_going = False

# if y it goes in circles 
# used to show the syntax of a while statement 
# something above then if below, then break 

while True: 

    answer = input('play again? (y/n)')
    if answer == 'n': 
        break 

forenames = ['Ken', 'Lynn', 'Pat', 'Nancy',]
surnames = ['Camp', 'Blake', 'Flanagan', 'Short',]

index = 0
while index < len(forenames): 
    if index >= len(surnames): 
        break 

    forename = forenames[index]
    surname = surnames[index]
    print(f'{forename} {surname}')

    index += 1

forenames = ['Ken', 'Lynn', 'Pat', 'Nancy',]
surnames = ['Camp', 'Blake', 'Flanagan', 'Short',]

zipped_names = zip(forenames,surnames)
for forename, surname in zipped_names:
    print(f'{forename} {surname}')

[print(foo) for foo in collection]

# compressed for loop 

[expression for element in iterable if condition]

# list comprehension 
# for element in iterable describes the iterable 
# basically a for loop 

squares = [number * number for number in range(5)]
print(squares)

squares = []
for number in range(5): 
    square = number * number 
    squares.append(square)

print(squares)

# the two create the same result 
# top one is quicker to write 

multiples_of_6 = [number for number in range(20)
                if number % 6 == 0]
                
# if its in a range, it takes the ones that divide by 6

even_squares = [number * number 
                for number in range(10)
                if number % 2 == 0]

print(even_squares)

# square roots of even numbers 

cats_colors = {
    'Tess': 'brown', 
    'Leo': 'orange', 
    'Fluffy': 'gray', 
    'Ben': 'black', 
    'Kat': 'orange', 
}

names = [name.upper() for name in cats_colors.values()]
print(names)

# uppercase the last names 

cats_colors = {
    'Tess': 'brown', 
    'Leo': 'orange', 
    'Fluffy': 'gray', 
    'Ben': 'black', 
    'Kat': 'orange', 
}

names = [name.upper() for name in cats_colors if cats_colors[name] == 'orange']
print(names)

cats_colors = {
    'Tess': 'brown', 
    'Leo': 'orange', 
    'Fluffy': 'gray', 
    'Ben': 'black', 
    'Kat': 'orange', 
}

names = [name.upper() 
        for name in cats_colors 
        if cats_colors[name] == 'orange'
        if name[0] == 'L']
print(names)

suits = ['clubs', 'diamonds', 'hearts', 'spades',]
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
        'jack', 'queen', 'king', 'ace' ]

deck = [f'{rank} of {suit}'
for suit in suits 
for rank in ranks
]
print(deck)

{key: value for element in iterable if condition}

# dicitionary comprehension

squares = {f'{number}-squared': number * number
            for number in range(1,6)}
print(squares)

{expression for element in iterable if condition}

# set comprehension 

squares = {number * number for number in range(1,6)}
print(squares)

squares = (number * number for number in range (1,6))
print(squares)

# prints it as an object because its a tuple 

result = empty_collection 
for item in collection: 
    result.append(item)