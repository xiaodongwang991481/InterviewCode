import bisect

class Node(object):
    def __init__(self, value):
        self.left = self.right = None
        self.value = value
        self.next = None

    def thread(self, prev=None):
        if self.left:
            prev = self.left.thread(prev)
        if prev:
            print('%s -> %s' % (prev.value, self.value))
            prev.next = self
        prev = self
        if self.right:
            prev = self.right.thread(prev)
        return prev

    def printThread(self):
        head = self
        while head.left:
            head = head.left
        while head:
            print('%s' % head.value, end='->')
            head = head.next
        print('')

    def print(self, indent = 0):
        print(' ' * indent, ' - ', self.value)
        print(' ' * indent, ' left:')
        if self.left:
            self.left.print(indent = indent + 2)
        print(' ' * indent, ' right:')
        if self.right:
            self.right.print(indent = indent + 2)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def print(self):
        if self.root:
            self.root.print()

    def buildTree(self, preorders, inorders):
        stack = []
        nextRightSet = set()
        inorderOffset = 0
        for order in preorders:
            orderNode = Node(order)
            if not self.root:
                self.root = orderNode
            if stack:
                topMost = stack.pop()
                if topMost.value not in nextRightSet:
                    topMost.left = orderNode
                    stack.append(topMost)
                else:
                    topMost.right = orderNode
                    nextRightSet.remove(topMost.value)
            stack.append(orderNode)
            lastMatched = None
            while True:
                if stack:
                    top = stack.pop()
                    if top.value != inorders[inorderOffset]:
                        stack.append(top)
                        break
                    lastMatched = top
                    inorderOffset += 1
                else:
                    break
            if lastMatched:
                stack.append(lastMatched)
                nextRightSet.add(lastMatched.value)

    def buildThread(self):
        if self.root:
            return self.root.thread()
        return None

    def printThread(self):
        if self.root:
            self.root.printThread()


if __name__ == "__main__":
    preorder = [1, 2, 4, 5, 3, 6]
    inorder = [4, 2, 5, 1, 3, 6]
    bst = BinaryTree()
    bst.buildTree(preorder, inorder)
    bst.print()
    bst.buildThread()
    bst.printThread()


