class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class NodeList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            head = self.head
            while head.next is not None:
                head = head.next
            head.next = node

    def prepend(self, value):
        ndoe = Node(value)
        head = self.head
        self.head = node
        node.next = head

    def count(self):
        if self.head is None:
            return 0
        head = self.head
        count = 1
        while head.next:
            head = head.next
            count += 1
        return count

    def extend(self, values):
        for value in values:
            self.append(value)

    def remove(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        head = self.head
        while head.next is not None:
            next = head.next
            if next.value == value:
                head.next = next.value
                return

    def print(self):
        if self.head is None:
            print(None)
            return
        head = self.head
        while head is not None:
            print("%s" % head.value, end="->")
            head = head.next
        print(None)

    def isPalindom(self):
        stack = []
        head = self.head
        while head is not None:
            stack.append(head.value)
            head = head.next
        rev = list(reversed(stack))
        if stack == rev:
            return True
        else:
            return False

    def removeDuplicated(self):
        if self.head is None:
            return
        head = self.head
        while head is not None and head.next is not None:
            if head.value == head.next.value:
                head.next = head.next.next
            else:
                head = head.next

if __name__ == "__main__":
    nodeList = NodeList()
    nodeList.extend([1,1,2,2,2,3,3])
    nodeList.print()
    nodeList.removeDuplicated()
    nodeList.print()

