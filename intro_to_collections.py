# 1. 

people = ['people']
print(len(people))

# 2. 

stuff = ('hello', 'world', 'bye', 'now')
stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
print(stuff)

# 3. 

# tuples cant be changed, lists can 
# lists are [] and tuples are ()
# lists and tuples can have different things in them 
# can be indexed with a number

# 4. 

# they are built in 

# 5. 

# sequences are ordered, where sets arent

# 6. 

pi = 3.141592
str_pi = str(pi)
print(str_pi)

# 7. 

0-6
1,2,3,4,5
3,7,11
nothing
8,7,6,5,4

# range does not include the stop value 

# 8. 
print (list(range(3,17,4)))

# 9. 

# yes, both are lists 
# no, 2 diferent objects 
# yes, same list
# yes

# 10. 

# wont be alphabetical, sets are unordered

# 11. 

countries = {
    'Alice': 'USA',
    'Francois': 'France',
    'Inti' : 'Peru',
    'Monika' : 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka' : 'Japan',
}

print(countries['Sanyu'])

letters = ['a', 'b', 'c', 'd']
char = letters[2]
print(char is letters[2])

# true - is does a comparison 

numbers = {2,1,3,5,4}
print(numbers)

# prints it from 1-5 in order 

d = {'a':1}
print(d['a'])

a = range(1,20,3)
print(list(a))

# the list is needed, if not it'll just print range(1,20,3)

a = range(5)
print(list(a))

my_str = 'python'

my_list = list(my_str)
print(my_list)

# turns the words into a list
