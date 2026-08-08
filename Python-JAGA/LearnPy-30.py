print("Linked List Implementation")
print()
class Node:
    def __init__(self, contents=None, next=None):
        self.contents = contents
        self.next = next
    def getContents(self):
        return self.contents
    def __str__(self):
        return str(self.contents)
    def print_list(node):
        while node:
            print(node.getContents())
            node = node.next
        print()
    def testList():
        node1 = Node("HTML")
        node2 = Node("CSS")
        node3 = Node("JavaScript")
        node4 = Node("Python")
        node5 = Node("Java")
        node6 = Node("C++")
        node7 = Node("C")
        node8 = Node("C#")
        node9 = Node("PHP")
        node10 = Node("Ruby")
        node11 = Node("Rust")
        node12 = Node("Go")
        node13 = Node("Swift")
        node14 = Node("Kotlin")
        node15 = Node("Dart")
        node16 = Node("Scala")
        node17 = Node("Perl")
        node18 = Node("Lua")
        node19 = Node("Haskell")
        node20 = Node("Erlang")
        node21 = Node("Elixir")
        node22 = Node("F#")
        node23 = Node("OCaml")
        node24 = Node("R")
        node25 = Node("MATLAB")
        node26 = Node("SAS")
        node27 = Node("SPSS")
        node28 = Node("Stata")
        node29 = Node("Tableau")
        node30 = Node("Power BI")
        node1.next = node2
        node2.next = node3  
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node7
        node7.next = node8
        node8.next = node9
        node9.next = node10
        node10.next = node11
        node11.next = node12
        node12.next = node13
        node13.next = node14
        node14.next = node15
        node15.next = node16
        node16.next = node17
        node17.next = node18
        node18.next = node19
        node19.next = node20
        node20.next = node21
        node21.next = node22
        node22.next = node23
        node23.next = node24
        node24.next = node25
        node25.next = node26
        node26.next = node27
        node27.next = node28
        node28.next = node29
        node29.next = node30
        Node.print_list(node1)
Node.testList()
