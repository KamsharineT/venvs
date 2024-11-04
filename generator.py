'''
This script contains example of generators of python
'''

def gene(*args):
    for i in args:
        yield i

numbers = gene(7)

for n in numbers:
    print(n)

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Create a generator object
counter = count_up_to(5)

# Iterate through the generator
for number in counter:
    print(number)
# Output:
# 1
# 2
# 3
# 4
# 5
