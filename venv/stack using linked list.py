class node:
    def __init__(self,data):
        self.next = None
        self.data = data
class Stack:
    def __init__(self):
        self.root = None
    def push(self,data):
        newnode = node(data)
        newnode.next  = self.root
        self.root = newnode
        print(f"{data} is pushed onto the stack")
    def isEmpty(self):
        return True if self.root is None else False
    def pop(self):
        if (self.isEmpty()):
            return float("-inf")

        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped
    def peek(self):
        if (self.isEmpty()):
            return float("-inf")
        return self.root.data
    # def

s = Stack()
s.push(2)
s.push(20)
s.push(30)
s.push(40)
print(s.pop())
v = s.peek()
print(v)

