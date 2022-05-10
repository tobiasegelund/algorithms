# https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

    def traversal(self) -> None:
        step = self.head
        while step is not None:
            print(step.val)
            step = step.next

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
    l = LinkedList()
    l.append(20)
    l.append(10)
    l.append(50)
    l.append(20)

    # l.traversal()
    l.head.next.next.next.next = l.head
    cycle = l.detect_cycle()
    print(cycle)
