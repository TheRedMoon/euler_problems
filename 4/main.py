'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
from itertools import permutations
def get_permutations(range):
    return list(permutations(range, 2))

def is_palingdrome(digit:str):
    digit_length = len(digit)-1
    if (digit_length + 1) % 2 != 0:
        return False
    for idx, x in enumerate(digit):
        place = digit[idx]
        otherside_place = digit[digit_length-idx]
        if place != otherside_place:
            return False
    return True

if __name__ == '__main__':
    permu = get_permutations(range(1,1000))
    num = "580085"
    print(f"result test: {is_palingdrome(num)}")

    res = [x*y for x,y in permu if is_palingdrome(str(x*y))]
    res = sorted(res)
    print(res)