# (1) - Hello World with Python
print('Hello, World!')

# (2) - Python if-else
n = int(input())

if (n % 2 != 0):
    print('Weird')
elif (n % 2 == 0) and (n >= 2) and (n <= 5):
    print('Not Weird')
elif (n % 2 == 0) and (n >= 6) and (n <= 20):
    print('Weird')
elif (n % 2 == 0) and (n > 20):
    print('Not Weird')
else:
    print('Not Available')

# (3) - Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

# (4) - Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

# (5) - Loops
if __name__ == '__main__':
    n = int(input())
    l = []
    
    while n > 0:
        n = n - 1
        l.append(n)
        
    l.reverse()
    
    for i in l:
        print(i ** 2)

# (6) - Write a function
def is_leap(year):
    leap = False
    
    if year % 4 != 0:
        leap = False
    elif year % 100 == 0 and year % 400 != 0:
        leap = False
    else:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))

# (7) - Print function
if __name__ == '__main__':
    n = int(input())
    l = []
    l.append(n)
    while n > 1:
        n = n - 1
        l.append(n)
    
    l.reverse()
    
    for i in l:
        print(str(i), end = '')

# (8) - Arrays
import numpy

def arrays(arr):
    return numpy.array(arr, dtype = float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# (9) - Shape and Reshape
import numpy as np

def array_fun(arr):
    arr = np.array(arr)
    arr.shape = (3, 3)
    return arr

arr = input().strip().split(' ')
list = []
for i in arr:
    i = int(i)
    list.append(i)
result = array_fun(list)
print(result)