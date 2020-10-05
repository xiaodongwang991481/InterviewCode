class Node(object):
    def __init__(self, label, next = None, random = None):
        self.label = label
        self.next = next
        self.random = random

    def __str__(self):
        randomValue = None
        if self.random:
            randomValue = self.random.label
        if self.next:
            return '%s (random %s) -> %s' % (self.label, randomValue, self.next)
        else:
            return '%s (random %s)' % (self.label, randomValue)

def listDeepCopy(head):
    nodeMap = {}
    node = head
    copiedHead = None
    copiedNode = None
    while node:
        newNode = Node(node.label)
        nodeMap[node] = newNode
        if copiedNode is not None:
            copiedNode.next = newNode
        copiedNode = newNode
        if copiedHead is None:
            copiedHead = copiedNode
        node = node.next
    node = head
    newNode = copiedHead
    while node:
        if node.random:
            newNode.random = nodeMap[node.random]
        node = node.next
        newNode = newNode.next
    return copiedHead

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node1.random = node3
node2.random = node4
head = node1
newHead = listDeepCopy(head)
print(newHead)