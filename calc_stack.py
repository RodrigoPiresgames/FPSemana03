from collections import deque 

def HandleInput():
    to_queue = list (map(int, input().split()))

    stack = deque(to_queue)

    print(stack)

    return stack

def DotheMath(to_math):
    while(to_math):
        result = to_math.pop() * 2
        print(result)

DotheMath(HandleInput())