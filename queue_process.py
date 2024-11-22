from collections import deque 

def HandleInput():
    to_queue = input().split()

    stack = deque(to_queue)

    print(stack)

    return stack

def PrintAllTheA(to_sort):
    for word in to_sort:
        if 'a' in word:
            print(word)

PrintAllTheA(HandleInput())