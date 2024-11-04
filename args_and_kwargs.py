# use of *args and **kwargs in python

def multiply(*args):
    output = 1

    for i in args:
        output *= i

    print(output)



def add(*args):

    ans = 1
    one = 1

    for val in args:
        one += val
        print(one)
        ans *= one
        print(ans)

    print(ans)

multiply(5,6,2)
add(10,2,5)


def studens(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    
studens(name = 'radha', age = 29)

