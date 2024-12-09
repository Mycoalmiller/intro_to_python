# 1. 

# the == determines if the objects have the same value 
# the is determines if the objects are pointing to the same id object


# 2. 

set1 = {42, 'monty python', ('a', 'b', 'c')}
set2 = set1 
set1.add(range(5,10))
print(set2)

# 3. 

# it will print out the life of brian
# if the change happened in dict 1 originally, it would print out 
# holy grail when dict2 is called, but dict 1 is the original variable, 
# and dict 2 is the target variable.
# 
# they arent the same object because of the dict

# 4. 

[1, 42,3]

# 5. 

import copy

dict1 = {
    'a': [[7,1], ['aa', 'aaa']], 
    'b': ([3,2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)

print(dict1 is dict2)
print(dict1['a'] is dict2['a'])
print(dict1['a'][0] is dict2 ['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b'] is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

# 6. 


dict1 = {
    'a': [{7,1}, ['aa', 'aaa']], 
    'b': ({3,2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1 is dict2)
print(dict1['a'] is dict2['a'])
print(dict1['a'][0] is dict2 ['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b'] is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])






a = 42
a *= 2 
print(a)

# prints 84

a = [1,2,3]
a += [4,5]
print(a)

numbers = 34
numbers2 = numbers 
print(id(numbers) == id(numbers2))
print(numbers is numbers2)

print(id(numbers))
print(id(numbers2))

import copy 
orig = [[1,2], 3,4,]
dup = copy.deepcopy(orig)

print(orig is dup)
print(orig == dup)
orig[2] == 44
print(orig)
print(dup)

print(orig[0] is dup[0])
orig[0][1] = 22 
print(dup[0])