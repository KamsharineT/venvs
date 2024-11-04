
# The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers. For example,

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, …

# Mathematically we can describe this as:

# xn= xn-1 + xn-2

#method (i)
def fibonacci(n):
    fibonacci_ser = []

    for i in range(n):
        try:
            fibonacci_ser.append(fibonacci_ser[-1]+fibonacci_ser[-2])
        except:
            fibonacci_ser.append(i)
    return fibonacci_ser


## Method (ii)
def fibonacci2(n2):
    fibonacci_ser = [0,1]
    while(len(fibonacci_ser)<n2):
        fibonacci_ser.append(fibonacci_ser[-1]+fibonacci_ser[-2])
    return fibonacci_ser

n = int(input())

print(fibonacci(n))

n2 = int(input())

print(fibonacci2(n2))

