class Node(object):
    def __init__(self, value):
        self.left = self.right = None
        self.value = value

    def leftMost(self):
        left = self
        while left.left:
            left = left.left
        return left

    def findNextPair(self, value):
        matched = next = None
        if self.left:
            matched, next = self.left.findNextPair(value)
        if next:
            return matched, next
        if matched:
            next = self
            return matched, next
        if self.value == value:
            next = self.right.leftMost() if self.right else None
            return self, next
        if self.right:
            return self.right.findNextPair(value)
        return None, None

    def insert(self, value):
        if self.value > value:
            if self.left:
                self.left.insert(value)
            else:
                # print('%s left -> %s' % (self.value, value))
                self.left = Node(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                # print('%s right -> %s' % (self.value, value))
                self.right = Node(value)

    def leftMost(self):
        left = self
        while left.left:
            left = left.left
        return left

    def delete(self, value):
        if self.value == value:
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            leftMost = self.right.leftMost()
            self.value, leftMost.value = leftMost.value, self.value
            self.right = self.right.delete(value)
            return self

    def print(self, indent=0):
        print(' ' * indent, '->', self.value)
        if self.left:
            print(' ' * indent, 'left:')
            self.left.print(indent = indent + 2)
        if self.right:
            print(' ' * indent, 'right:')
            self.right.print(indent = indent + 2)


class BSTree(object):
    def __init__(self, values):
        self.root = None
        for value in values:
            self.insert(value)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def delete(self, value):
        if self.root:
            self.root = self.root.delete(value)

    def print(self):
        if self.root:
            self.root.print()

    def findNext(self, value):
        if self.root:
            matched, next = self.root.findNextPair(value)
            if next:
                return next.value
        return None

if __name__ == "__main__":
    bst = BSTree([5,3,2,1,4,8,6,7,9,10])
    bst.print()
    for value in [0,1,2,3,4,5,6,7,8,9,10,11]:
        next = bst.findNext(value)
        print('%s next %s' % (value, next))

