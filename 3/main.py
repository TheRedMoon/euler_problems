'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
def get_prime(n):
    i = 2
    factors = []
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

if __name__ == '__main__':
    prime = get_prime(13195)
    print(f"result test: {prime}")

    prime = get_prime(600851475143)
    print(f"result test: {prime}")