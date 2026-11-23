"""Module 2 - Build and Use Data Structures.

Part 1: Linked List
Part 2: Stack Bracket Validator
Part 3: Queue Task Processor
"""

from collections import deque


# Part 1 - Linked List

# Each node stores a value and a link to the next node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # The head is the first node in the linked list.
        self.head = None

    def insert_at_end(self, data):
        # Create a new node with the given value.
        new_node = Node(data)

        # If the list is empty, the new node becomes the head.
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, move to the last node.
        current = self.head
        while current.next is not None:
            current = current.next

        # Connect the last node to the new node.
        current.next = new_node

    def display(self):
        # Print the values in order.
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, target):
        """Remove the first node with the target value. Return True if found."""
        current = self.head
        previous = None

        # Search until we find the target or reach the end.
        while current is not None:
            if current.data == target:
                if previous is None:
                    # The first node needs to be removed.
                    self.head = current.next
                else:
                    # Skip the matching node.
                    previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    def length(self):
        """Count the nodes in the list. O(n) time."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def to_list(self):
        """Return the linked list values as a regular Python list."""
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values


# Part 2 - Stack: Bracket Validator

def is_balanced(text):
    """Return True if (), [], and {} are properly matched in text."""
    stack = []
    brackets = {")": "(", "]": "[", "}": "{"}
