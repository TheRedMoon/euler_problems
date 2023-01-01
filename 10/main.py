'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

def is_prime(n):
    for i in range(2, int(n ** 0.5)+1): #went too slow at first, optimized it to square root rounded
        if n % i == 0:
            return False
    return True

def t(r):
    l = []
    n = 2
    while n < r:
        if is_prime(n):
            l.append(n)
        n +=1
    return l

if __name__ == '__main__':
    prime = t(10)
    print(prime)
    print(f"result test: {sum(prime)}")

    prime = t(2000000)
    print(f"result: {sum(prime)}")