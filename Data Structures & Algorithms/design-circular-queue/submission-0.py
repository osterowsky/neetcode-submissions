class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.capacity = k
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = Node(val = value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            prev = self.tail
            self.tail = new_node
            prev.next = self.tail
            self.tail.next = self.head

        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        new_head = self.head.next if self.head.next else None
        self.head = new_head
        if self.tail:
            self.tail.next = new_head

        self.length -= 1
        return True

    def Front(self) -> int:
        return self.head.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.tail.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.capacity == self.length


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()