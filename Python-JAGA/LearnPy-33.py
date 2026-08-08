print("Stack Add and remove Method")
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
s.push("Jaga Rabari")
s.push("Web Developer")
s.push("Python Programmer")
s.push("HTML, CSS, JavaScript")
s.push("Laravel Developer")
s.push("Frontend Developer")
s.push("Backend Developer")
s.push("Visual Studio Code")
print("Top element is : ", s.peek())
print("Stack size is : ", s.size())
print("Popped element is : ", s.pop())
print("Top element is : ", s.peek())
print("Stack is : ", s.stack)
