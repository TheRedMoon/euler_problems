'''
<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
'''

#takes a while
def square(range):
    res = sum([x**2 for x in range])
    res_2 = sum(range)**2
    print(res, res_2)
    return res_2- res


if __name__ == '__main__':
    res = square(list(range(1, 11)))
    print(f"result test: {res}")

    res = square(list(range(1, 101)))
    print(f"result: {res}")