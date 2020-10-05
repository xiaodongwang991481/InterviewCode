class Node(object):
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert(self, node):
        if self.value > node.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

    def print(self, indent = 0):
        print(' ' * indent, self.value)
        if self.left is not None:
            print(' ' * indent, 'left:')
            self.left.print(indent + 2)
        if self.right is not None:
            print(' ' * indent, 'right:')
            self.right.print(indent + 2)

def calcLeftPosition(node, leftPositionByDepth, depth, position):
    if depth not in leftPositionByDepth:
        leftPositionByDepth[depth] = position
    else:
        leftPositionByDepth[depth] = min(leftPositionByDepth[depth], position)
    if node.left:
        calcLeftPosition(node.left, leftPositionByDepth, depth + 1, position * 2)
    if node.right:
        calcLeftPosition(node.right, leftPositionByDepth, depth + 1, position * 2 + 1)

def calcRightPosition(node, rightPositionByDepth, depth, position):
    if depth not in rightPositionByDepth:
        rightPositionByDepth[depth] = position
    else:
        rightPositionByDepth[depth] = max(rightPositionByDepth[depth], position)
    if node.right:
        calcRightPosition(node.right, rightPositionByDepth, depth + 1, position * 2 + 1)
    if node.left:
        calcRightPosition(node.left, rightPositionByDepth, depth + 1, position * 2)

def maxWidth(node):
    leftPositionByDepth = {}
    rightPositionByDepth = {}
    calcLeftPosition(node, leftPositionByDepth, 0, 0)
    calcRightPosition(node, rightPositionByDepth, 0, 0)
    widthByDepth = {}
    for depth, leftPosition in leftPositionByDepth.items():
        rightPosition = rightPositionByDepth[depth]
        widthByDepth[depth] = rightPosition - leftPosition + 1
    return max(widthByDepth.values())

if __name__ == "__main__":
    node = Node(5)
    node.insert(Node(3))
    node.insert(Node(7))
    # node.insert(Node(1))
    node.insert(Node(4))
    node.insert(Node(6))
    # node.print()
    print(maxWidth(node))