'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

#takes a while
def can_be_divided(range):
    num = 1
    found = False
    while not found:
        b = True
        for x in range:
            if num % x != 0:
                num += 1
                b = False
                break
        found = b
    return num

if __name__ == '__main__':
    res = can_be_divided(list(range(1, 11)))
    print(f"result test: {res}")

    res = can_be_divided(list(range(1, 21)))
    print(f"result: {res}")