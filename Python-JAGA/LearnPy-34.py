print("Queues Add and Delete Operations")
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
q.enqueue("Abstarct Class")
q.enqueue("Interface")
q.enqueue("Inheritance")
q.enqueue("Polymorphism")
q.enqueue("Encapsulation")
q.enqueue("Data Abstraction")   
q.enqueue("Method Overloading")
q.enqueue("Method Overriding")
q.enqueue("Multiple Inheritance")
q.enqueue("Multilevel Inheritance")
q.enqueue("Hierarchical Inheritance")
q.enqueue("Hybrid Inheritance")
q.enqueue("Constructor")
q.enqueue("Destructor")
q.enqueue("Super() Function")
q.enqueue("Python OOPs Concepts")
q.enqueue("Errors and Exceptions")
print("Front element is : ", q.peek())
print("Queue size is : ", q.size())
print("Dequeued element is : ", q.dequeue())
print("Front element is : ", q.peek())
print("The Queue is : ", q.queue)
