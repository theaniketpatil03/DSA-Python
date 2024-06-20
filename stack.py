'Last in First out'

s = []

s.append(1)
s.append(2)
s.append(3)

print(s)
print(s.pop())
print(s)

'''dont use list as it is dynamic array and when requires it add extra coapacity - current capacity * 20 then it will copy everything to new locations'''
'use collection.deque'

from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
print(stack)
print(stack.pop())
print(stack)


# creating own stack
class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)