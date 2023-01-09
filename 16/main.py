'''

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

#ez with python. No integer cap
def calc(i,x):
    i += int(x)
    return i

if __name__ == '__main__':
    chars = str(2**15)
    res = sum([int(x) for x in chars])
    print(res)

    chars = str(2**1000)
    res = sum([int(x) for x in chars])

    #above is 1000 numbers in memory; cleaner is:
    i = 0
    for char in chars:
        i = calc(i,char)
    print(res)
    print(i)