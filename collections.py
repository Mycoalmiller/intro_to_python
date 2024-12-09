# 1. 

a = range(0,25,3)
print(a[6])

# 2. 

a = 'launch school'
print(a[4:10 ])

# 3. 

a = (1,2,3,4,5)
print(tuple(reversed(a[1:4])))

# 4. 

pets = {
    'Cat': 'Meow', 
    'Dog': 'Bark', 
    "Bird": "Tweet",
}

# part 1 

# a = pets['Dog']
# print(a)

# part 2 

print(pets.get('Lizard'))

# part 3 

print(pets.get('Lizard', '<silence>'))

# 5. 

# the main word is key. keys cant have multiple keys in them.  

# 6. 

# 'abcdef' and '31415' are true. The rest are false because 
# the methods used are strict

# 7. 

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
a = info.split(':')
b = '+'.join(a)
print(b)

# 8. 

# line 3 is defined at index 21, and is reverse found at 35, is the value from 35
# line 4 is defined at index 0, reverse find is done at 35, is then 29
text = "it's probably pining for the fjors!"
# 'for the fjords' 
print(text[21:35].rfind('f'))

# it's probably pining for the fjords!
print(text.rfind('f', 21, 35))

# 9. 

stuff = [
    ['hello', 'world'], 
    ['example', 'mem', None, 6, 88], 
    [4,8,12], 
]
stuff[1][3] = 606
print(stuff[1][3])

# 10. 

cats = {
    'Pete': {
        'Cheddar' : {
            'color': 'orange', 
            'enjoys': { 
                'sleeping', 
                'snuggling', 
                'meowing', 
                'eating', 
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black', 
            'enjoys': {
                'eating', 
                'sleeping', 
                'playing', 
                'chewing',
            },
        }, # type: ignore
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

# 11. 

# false 
# true
# true 
# false 
# true
# false
# false
# true 
# true - its false
# false - it true

# 12. 

numbers1 = [1,3,5,7,9,11]
numbers2 = []
numbers3 = [2,4,6,8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']
print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

# 13. 

# true 
# false 
# true 
# false

# 14. 

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)
a = zip(my_str, my_list, my_tuple, my_range)
print(list(a))

# 15. 

'Cat' , 'Bird', 'Snake'

seq = ('a', 'b', 'c', 'd')
if len(seq) > 3: 
    print(seq[3])

# will print if length is greater than 3 

seq = ('a', 'b', 'c')
last_index = len(seq) - 1 # takes the length, minus 1
print(seq[last_index]) # then puts it in an index

seq = ('a', 'b', 'c')
print(seq[-1])

# c 

seq = 'abcdefghi'
print(seq[3:7])

# defg

seq = [1,2,3,4,5,6,7,8,9,10]
print(seq[3:7])

# [4,5,6,7]

my_dict = {
    'a' : 'abc', 
    37 : 'def', 
    (5,6,7): 'ghi', 
    fronzenset([1,2]): 'jkl',
}

print(my_dict['a'])
print(my_dict.get('a'))
my_dict['a'] = 'ABC'

my_set1 = [1,2,3,4,5,6,7,8]
print (min(my_set1), max(my_set1))

print(min(3,5,-1), max(3,5,-1))

names = ['joe', 'mark']
print(names.index('joe'))

numbers = [1,1,2]
print(numbers.count(1))

# prints 2, since 1 came up twice in the list

iterable1 = [1,2,3]
iterable2 = [4,5,6,7]

zipped_iterable = zip(iterable1, iterable2, strict=True)
print(list(zipped_iterable))
print(list(zipped_iterable))

# zip functions can only be called once

people_phones = {
    'abby' : '123', 
    'joe' : '456', 
}

print(people_phones.keys())
print(people_phones.values())
print(people_phones.items())

# a dictionary can referenced through a key, value
# or a key/value option

people_phons = {
    'chris': '111-2222', 
    'Pete': '333-4444', 
    'clare': '555-7777', 
}

keys = people_phones.key()
values = people_phones.values()
people_phones['max'] = '123'
people_phones['pete'] = '456'
del people_phones['chris']

print(keys)
print(values)

# adds updated values into the variables, automatically 

numbers = [1,2]

numbers.append(10)
print(numbers)

# adds it to the end of the list 

numbers = [1,2]
numbers.insert(0,8) 
print(numbers)

numbers = [1,2]
numbers.extend([7,8])
print(numbers)

my_list = [2,4,6,8,10]
my_list.remove(8)
print(my_list)

# takes out the 8 

my_list = [2,4,6,8,10]
print(my_list.pop(1))
print(my_list)

# takes out an item by the index number

my_list = [2,4,6,8,10]
my_list.clear()
print(my_list)

# deletes the list 

names = ('grace', 'kevin', 'ben')
# print(sorted(names))
names = list(names)
print(names.sort()) # blank
print(names)

names = ['hello', 'world']
# print(sorted(names, reverse=True))

names.sort(reverse=True)
print(names)

# prints it in reverse

words = ['def', 'abc']
print(sorted(words, key=str.casefold))

# organizes them alphabetically

numbers = ['20', '5', '100']
numbers.sort(key=int)
print(numbers)
# organize them by integer

names = ('grace', 'clare', 'trevor')
reversed_names = reversed(names)
# print(reversed_names)
# print(tuple(reversed(names))) # reverse the order 

names = list(names)
print(names.reverse())
print(names)

names = ('grace', 'clare', 'trever')
for name in reversed(names): 
    print(name)

'hello'.isalpha()

# tests if its all alphabetical - True

'123'.isdigit()

# tests if its all digitis - True

text = 'abcde'
for char in text: 
    print(char)

text = '''
hello 
world 
'''

print(text.strip().splitlines())

words = ['you', 'were', 'lucky']
print(''.join(words))

# joins the words together 

school = 'launch school'
# print(school.find('hoo'))

# can find the string in a string, says the index number 
print(school.rfind('l'))

# goes from the back of the string to find it

