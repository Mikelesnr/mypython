def fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b


def print_fib(n):
    for i in fib(n):
        print(i)


while True:
    try:
        x = int(input('enter fibonacci range\n'))
        print_fib(x)
        break
    except:
        print('please anter valid positive integer\n')
