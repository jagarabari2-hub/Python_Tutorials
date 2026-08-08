print("Stack Implementation")
print()
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Top element is : ", s.peek())
print("Stack size is : ", s.size())
print("Popped element is : ", s.pop())
print("Top element is : ", s.peek())
print("The Stack is : ", s.stack)