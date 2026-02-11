from random import randint
import math

def is_prime(n: int):
    if n <= 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True

def get_primes(list: list):
    primes = []
    for i in list:
        if is_prime(i):
            primes.append(i)

    return primes

def main():
    list = []
    
    for i in range(1, 100):
        list.append(randint(1, 100))
    print("Lista:\n")
    print(list)
    print()

    odd_list = get_primes(list)
    print("Lista apenas com os primos:\n")
    print(odd_list)
    print()

if __name__ == "__main__":
    main()