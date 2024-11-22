from collections import deque 

def HandleInput():
    to_queue = input().split()

    stack = deque()
    for piece in to_queue:
        stack.appendleft(piece)

    print(stack)

    return stack

def PrintAllTheA(to_sort):
    while(to_sort):
        last_word = to_sort.pop()         
        if 'a' in last_word:
            print(last_word)
        else:
          pass

PrintAllTheA(HandleInput())