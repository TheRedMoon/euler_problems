'''

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

from collections import deque
from itertools import combinations
from itertools import permutations

dirs = [(1,0), (0,1)]
width = 3
height =3

def bfs(start, end):
    queue = deque([start])
    found = 0
    w = width -1
    h = height -1
    while queue:
        coord = queue.pop()
        #print(f"coord {coord}")
        if coord == end:
            found += 1
        for dir in dirs:
            new_coord = tuple(p + q for p, q in zip(coord, dir))
            x1,y1 = new_coord

            if x1 < 0 or x1 > w or y1 < 0 or y1 > h:
                continue
            queue.append(new_coord)
    return found


def make_grid():
    grid = set()
    for y in range(height):
        for x in range(width):
            grid.add((y,x))
    return grid


def get_pascal(n):
    res = 1
    for x in range(1,n+1):
        res = res * (n + x) / x
    return res

if __name__ == '__main__':
    grid = make_grid()
    #print(f"grid {grid}")
    end = (width-1,height-1)
    start = (0,0)
    res = bfs(start, end)
    print(f"test {res}")

    #bigger numbers the above no longer works/takes way too long
    #instead look at the solution space (R,D) (R,D) for n=1 or 6 for n=2  where nxn = the grid
    # the above also shows solution space is 20 for n=3
    # Concluding this sequence we can see a pattern namely the pascal triangle
    #https://www.cuemath.com/algebra/pascals-triangle/
    res = get_pascal(2)
    print(f"test pascal {res}")

    res = get_pascal(20)
    print(f"pascal {res}")