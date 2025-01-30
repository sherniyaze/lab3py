def solve(numheads, numlegs):
    x = (numlegs - 2*numheads)/2
    print(f"{x} chickens and {numheads - x} rabbits")
numheads = int(input())
numlegs = int(input())
solve(numheads, numlegs)
#12 chickens in there and 23 rabbits

