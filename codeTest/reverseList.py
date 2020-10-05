class Node(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        if self.next:
            return '%s -> %s' % (self.value, self.next)
        else:
            return str(self.value)


def reverse(head):
    if head is None or head.next is None:
        return head
    next = head.next
    head.next = None
    while next:
        nextNext = next.next
        next.next = head
        head = next
        next = nextNext
    return head


head = Node(1, Node(2, Node(3, Node(4))))
newHead = reverse(head)
print(newHead)