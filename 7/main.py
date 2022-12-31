'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def t(r):
    l = []
    n = 2
    while len(l) < r:
        if is_prime(n):
            l.append(n)
        n +=1
    return l[-1]
if __name__ == '__main__':
    prime = t(6)
    print(f"result test: {prime}")

    prime = t(10001)
    print(f"result: {prime}")
