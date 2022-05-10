class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val: int) -> None:
        node = Node(val)
        if self.head:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next

            node.prev = last_node
            last_node.next = node
        else:
            self.head = node

    def traversal(self) -> None:
        step = self.head
        while step is not None:
            print(step.val)
            step = step.next

    def reverse_traversal(self) -> None:
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        while last_node is not None:
            print(last_node.val)
            last_node = last_node.prev

    def pop(self) -> None:
        pass

    def detect_cycle(self) -> bool:
        slow = self.head
        fast = self.head.next

        try:
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except AttributeError:
            return False


if __name__ == '__main__':
    l = DoubleLinkedList()
    l.append(20)
    l.append(10)
    l.append(50)
    l.append(60)
    # l.traversal()
    l.reverse_traversal()

    # create cycle
    l.head.next.next.next.next = l.head
    cycle = l.detect_cycle()
    print(cycle)
