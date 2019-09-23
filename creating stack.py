class stacks():
    def __init__(self):
        self.items = []
    def push(self,element):
        self.items.append(element)
    def length(self):
        return len(self.items)
    def empty(self):
        return self.items == []
    def pop(self):
        return self.items.pop()
    def show(self):
        print(self.items)
    def peek(self):
        if self.items == []:
            print("stack empty")
        else:
            return self.items[-1]



s = stacks()
s.push(2)
s.push(3)
s.push(4)
s.pop()
print(s.peek())

s.show()



