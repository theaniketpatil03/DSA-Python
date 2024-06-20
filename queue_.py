from collections import deque

# generally queue means - First in First out

class Queue:

    def __init__(self) -> None:
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)


pq = Queue()

pq.enqueue({
    'name': 'aniket'
})
pq.enqueue({
    'name': 'parle'
})
pq.enqueue({
    'name': 'vinayak'
})

print(pq.buffer)
print(pq.dequeue())
print(pq.buffer)