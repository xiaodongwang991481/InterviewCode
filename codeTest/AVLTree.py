class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.height = 1

    def getBalance(self):
        leftHeight = self.left.height if self.left else 0
        rightHeight = self.right.height if self.right else 0
        return leftHeight - rightHeight

    def rightRotate(self):
        left = self.left
        self.left = left.right
        left.right = self
        self.height = self.getHeight()
        left.height = left.getHeight()
        return left

    def leftRotate(self):
        right = self.right
        self.right = right.left
        right.left = self
        self.height = self.getHeight()
        right.height = self.getHeight()
        return right

    def getHeight(self):
        return max(
            self.left.height if self.left else 0,
            self.right.height if self.right else 0
        ) + 1

    def rebalance(self):
        balance = self.getBalance()
        if balance > 1:
            childBalance = self.left.getBalance()
            if childBalance < 0:
                self.left = self.left.leftRotate()
            return self.rightRotate()
        elif balance < -1:
            childBalance = self.right.getBalance()
            if childBalance > 0:
                self.right = self.right.rightRotate()
            return self.leftRotate()
        return self

    def getLeftMost(self):
        left = self
        while left.left is not None:
            left = left.left
        return left

    def insert(self, value):
        if self.value > value:
            if self.left:
                self.left = self.left.insert(value)
            else:
                self.left = Node(value)
            self.height = max(self.height, self.left.height + 1)
        else:
            if self.right:
                self.right = self.right.insert(value)
            else:
                self.right = Node(value)
            self.height = max(self.height, self.right.height + 1)
        return self.rebalance()

    def delete(self, value):
        if self.value > value:
            if self.left:
                self.left = self.left.delete(value)
        elif self.value < value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if not self.left and self.right:
                return self.right
            elif not self.right and self.left:
                return self.right
            elif not self.left and not self.right:
                return None
            else:
                leftMost = self.right.getLeftMost()
                if leftMost:
                    self.value, leftMost.value = leftMost.value, self.value
                    self.right = self.right.delete(value)
        self.height = self.getHeight()
        print('before rebalance')
        self.print()
        print('----------------')
        newRoot = self.rebalance()
        print('after rebalance')
        newRoot.print()
        print('-----------------')
        return newRoot


    def print(self):
        print("node level %s: %s" % (self.height, self.value))
        if self.left:
            print("left nodes:")
            self.left.print()
        if self.right:
            print("right nodes:")
            self.right.print()

class BST(object):
    def __init__(self, values):
        self.root = None
        self.insert(values)

    def insert(self, values):
        for value in values:
            if not self.root:
                self.root = Node(value)
            else:
                self.root = self.root.insert(value)

    def delete(self, values):
        for value in values:
            if not self.root:
                return
            else:
                self.root = self.root.delete(value)

    def print(self):
        if self.root:
            self.root.print()

if __name__ == "__main__":
    bst = BST([1,2,3,4,5,6,7,8,9])
    bst.print()
    print('_______delete________')
    bst.delete([3, 5, 7])
    bst.print()