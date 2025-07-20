class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        # assign the provided 'data' and initialize 'next' to None
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        # initialize 'head' to None to represent an empty list
        self.head = None

    def insert_at_front(self, data):
        """
        Create a new Node and insert it at the front of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Create a new Node and insert it at the end of the list.
        """
        new_node = Node(data)
        if not self.head:
            # if list is empty, new node becomes head
            self.head = new_node
            return
        # otherwise, traverse to the end
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """
        Return the sum of all node data using recursion.
        """
        def _sum(node):
            if not node:
                return 0
            return node.data + _sum(node.next)

        return _sum(self.head)

    def recursive_search(self, target):
        """
        Return True if 'target' is found in the list; otherwise False.
        """
        def _search(node):
            if not node:
                return False
            if node.data == target:
                return True
            return _search(node.next)

        return _search(self.head)

    def recursive_reverse(self):
        """
        Reverse the list in-place using recursion.
        """
        def _reverse(prev, curr):
            # base case: end of list reached
            if not curr:
                return prev
            next_node = curr.next
            curr.next = prev
            # recurse with curr as new prev and next_node as new curr
            return _reverse(curr, next_node)

        # update head to new head returned by helper
        self.head = _reverse(None, self.head)

    def display(self):
        """
        Print the contents of the list for debugging.
        """
        elems = []
        current = self.head
        while current:
            elems.append(str(current.data))
            current = current.next
        print(" -> ".join(elems) + " -> None")