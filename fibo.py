def fibo(n):
    if n <= 0:
        raise ValueError
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    while n - 2:
        a, b = b, a + b
        n -= 1
    return b

def main():
    for i in range(1, 15):
        print(i, fibo(i))

if __name__ == '__main__':
    main()