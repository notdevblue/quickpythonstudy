# https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else: # 놀랍게도 올바른 코드..
        print(n, "is a prime number")

# try statement 에서 else 문은 아무런 exception 이 일어나지 않았을 떄 때 실행됨
# loop statement 에서 else 는 break 이 없었을 때 실행됨

print(5 / 2)    # classic division  # returns 2.5
print(5 // 2)   # floor division    # returns 2 (floored)
# python 3.0 ~ 에서 볼 생김

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue # 이건 C 랑 같음
    print("Found an odd number", num)

# while False:
#     pass # 이건 아무것도 안 함.

class MyEmptyClass:
    pass # 이렇게 빈 클레스를 만들거나

def MyEmptyFunction():
    pass # TODO: Implement this funciton
# 이렇게 사용할 수 있음

# match statement 는 expression 이나 값을 가지고 비교해서 하나 또는 하나 이상의 가능한 패턴을 실행함. switch 랑 비슷함
# Rust 에 match 와 제일 비슷함.

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404: # can combine literals
            return "Not found"
        case 410:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet m8"

print(http_error(410)) # -> >>> I'm a teapot

point = (1, 2)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")         # f-string. like a rust "{variable}". can format additional things, google.
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
# can unpack, and bind variables

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Coord(x = 0, y = 0): # can capture attributes into variables
            print("Origin")
        case Coord(x = 0, y = y):
            print(f"Y={y}")
        case Coord(x = x, y = 0):
            print(f"X={x}")
        case Coord():
            print("Somewhere on the universe")
        case _:
            print("Not a point")

where_is(Coord(1, 0))

var = 2
Coord(1, var)
Coord(1, y = var)
Coord(x = 1, y = var)
Coord(y = var, x = 1)
# these patterns are all equivalent

# Patterns can be arbitrarily nested
class Coord2:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

coord = [Coord2(0, 0), Coord2(0,2)]
match coord:
    case []:
        print("No points")
    case [Coord2(0, 0)]: # can create pattern like this.
          print("The origin")
    case [Coord2(x, y)]:
        print(f"Single point {x}, {y}")
    case [Coord2(0, y1), Coord2(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

match Coord2(1, 1):
    case Coord2(x, y) if x == y: # can add if clause, known as guard. If guard is false, match tries next block. Value capture happens before guard is evaluated.
        print(f"Y=X at {x}")
    case Coord2(x, y):
        print(f"Not on the diagonal")

# tuple and list patterns have exactly the same meaning and and actually match arbitrary sequences.
# they don't match iterators or strings
a = [1, 2, 3]
match a:
    case (1, 2, 3): # this is tuple, but it's matched
        print("AAA")
    case [1, 2, 3]: # match already hapened, this block is ignored
        print("Ignored")

# support extended unpacking: [x, y, *rest] and (x, y, *rest)
# name after * may also be _, so (x, y *_) matches a sequence of at least two items

match a:
    case (x, y, *_): # matched
        print(a)
    case _:
        print("none")
    
# Mapping patterns: {"han": h, "jan": j} captures the "han", "jan" values from a dictionary
# extra keys are ignored. **rest is supported (but **_ would be redundant, so not allowed)

hanjan = {"han": 1, "jan": 2}

match hanjan:
    case {"han": h, "jan": j, **rest}:
        print(hanjan, "hanjanjuan")
    case {"han": h, "jan": j}:
        print(hanjan, "hanjan")

# Subpatterns may be captured using the as keyword

match Coord2(1, 2):
    case Coord2(x, y) as c: # using as keyword
        print(c.x, c.y)

# most iterals are compared by equality, however the singletons True, False, and None are compared by identity

# Patterns may use named containts.
# must be dotted names to prevent being interpreted as capture variable
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

match Color('red'):
    case Color.RED:
        print("Red!")
    case Color.GREEN:
        print("Green!")
    case Color.BLUE:
        print("Jazz blues.")

