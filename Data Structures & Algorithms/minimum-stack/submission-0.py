class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MinStack:
    def __init__(self):
        self.topNode = None
        self.height = 0
        self.minStack = []

    def push(self, val: int) -> None:
        new_node = Node(val)
        if self.height == 0:
            self.topNode = new_node
            self.minStack.append(val)
        else:
            temp = self.topNode
            self.topNode = new_node
            self.topNode.next = temp
            self.minStack.append(min(val, self.minStack[-1]))
        self.height += 1 

    def pop(self) -> None:
        if self.height == 0:
            return None 
        temp = self.topNode
        self.topNode = self.topNode.next
        temp.next = None
        self.minStack.pop()
        self.height -= 1

    def top(self) -> int:
        return self.topNode.value 

    def getMin(self) -> int:
        return self.minStack[-1]