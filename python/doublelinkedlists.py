
# Doubly Linked List Assignment

# Each node stores data and two pointers
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        # Head points to the first node
        self.head = None

        # Tail points to the last node
        self.tail = None

    # Add a node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # Connect the new node to the old tail
        new_node.prev = self.tail
        self.tail.next = new_node

        # Update the tail
        self.tail = new_node

    # Delete the first node with the target value
    def delete(self, target):
        current = self.head

        # Search for the target
        while current is not None:
            if current.data == target:

                # Update the previous node's next pointer
                if current.prev is None:
                    self.head = current.next
                else:
                    current.prev.next = current.next

                # Update the next node's prev pointer
                if current.next is None:
                    self.tail = current.prev
                else:
                    current.next.prev = current.prev

                return True

            current = current.next

        # Target not found
        return False

    # Count the nodes
    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    # Display the linked list forward
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Display the linked list backward
    def display_reverse(self):
        current = self.tail

        while current is not None:
            print(current.data, end=" -> ")
            current = current.prev

        print("None")

    # Convert the linked list to a Python list
    def to_list(self):
        values = []
        current = self.head

        while current is not None:
            values.append(current.data)
            current = current.next

        return values


# Test the doubly linked list
ll = LinkedList()

# Add five values
for val in [10, 20, 30, 40, 50]:
    ll.insert_at_end(val)

print("Forward:")
ll.display()

print("Reverse:")
ll.display_reverse()

print("Length:", ll.length())

# Delete node containing 30
print("Delete 30:", ll.delete(30))

print("After deletion:")
ll.display()

print("Reverse after deletion:")
ll.display_reverse()

print("Python list:", ll.to_list())

# Test a missing value
print("Delete 100:", ll.delete(100))
