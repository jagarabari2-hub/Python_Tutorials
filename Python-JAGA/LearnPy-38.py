print()
print("|========================================|"
      "| Illustration of Access Modifiers "
      "||========================================|")
print()
memory = {0:0, 1:1}
class Fibonacci():
        def mem_fib(self, num):
            if not num in memory:
                memory[num] = self.mem_fib(num-1) + self.mem_fib(num-2)
            return memory[num]
obj = Fibonacci()
obj.num = 987
print("Given Number is :",obj.num)
print("Fibonacci Number :",obj.mem_fib(obj.num))