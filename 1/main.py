'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def find_multiples(multiples: list, r: int):
      res = [x for x in range(r) for y in multiples if x % y == 0]
      res = set(res)
      return list(res)

if __name__ == '__main__':
    test_m = [3,5]
    test_range = 10
    multiples = find_multiples(test_m, test_range)
    print(f"result test: {sum(multiples)}")

    real_m = [3,5]
    real_range = 1000
    multiples = find_multiples(real_m, real_range)
    print(f"result: {sum(multiples)}")