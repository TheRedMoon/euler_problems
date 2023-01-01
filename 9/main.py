'''
<p>A Pythagorean triplet is a set of three natural numbers, <var>a</var> &lt; <var>b</var> &lt; <var>c</var>, for which,</p>
<div class="center"> <var>a</var><sup>2</sup> + <var>b</var><sup>2</sup> = <var>c</var><sup>2</sup></div>
<p>For example, 3<sup>2</sup> + 4<sup>2</sup> = 9 + 16 = 25 = 5<sup>2</sup>.</p>
<p>There exists exactly one Pythagorean triplet for which <var>a</var> + <var>b</var> + <var>c</var> = 1000.<br />Find the product <var>abc</var>.</p>


'''

from itertools import combinations
def get_permutations(range):
    return list(combinations(range, 3))

def check_conditions(entry):
    a,b,c = sorted(entry) #force condition a < b < c
    #print(a,b,c)
    if (a**2 + b**2) == c**2:
        #print("gert", a, b, c)
        if a + b + c == 1000:
            return True
    return False
if __name__ == '__main__':
    ns = get_permutations(range(500))
    for n in ns:
        if check_conditions(n):
            a,b,c = n
            print(f"result test: {a*b*c}")
