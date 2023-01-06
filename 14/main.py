'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

from itertools import count
from collections import defaultdict
dict = defaultdict(int)


def determine_new_value(x):
    if x % 2 == 0:
        return x/2
    return x*3 + 1


def start_chain(n):
    x = n
    chain = []
    Found = False
    while not Found:
        chain.append(x)
        if x in dict:
            dict[n] += dict[x]
            break
        dict[n] += 1
        if x == 1:
            Found = True
        else:
            x = determine_new_value(x)
    # print(f"Starting number: {n} \n\n\n chain: {chain} \n length {dict[n]}")
    return dict[n]

if __name__ == '__main__':
    largest_chain = 0
    starting_number = 0
    #test
    n = start_chain(13)
    print(f"Test chain length {n}")
    dict = defaultdict(int)

    for n in count(1):
        if n > 1000000:
            print(f"Largest chain length {largest_chain} with starting number {starting_number}") #we do not need the largest chain we just need the number
            break
        chain = start_chain(n)
        if chain > largest_chain:
            largest_chain = chain
            starting_number = n

