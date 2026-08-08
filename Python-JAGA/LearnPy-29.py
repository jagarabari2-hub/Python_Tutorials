print("Queues Implementation")
print()
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Front element is : ", q.peek())
print("Queue size is : ", q.size())
print("Dequeued element is : ", q.dequeue())
print("Front element is : ", q.peek())