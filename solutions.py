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