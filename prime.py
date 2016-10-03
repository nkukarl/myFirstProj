def is_prime(n):
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True

def get_next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n

def main():
    print(get_next_prime(10))

if __name__ == '__main__':
    main()