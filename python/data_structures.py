
# Part 1 - Linked List

# Create a node to store a value and the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)

        # If the list is empty, make this the first node
        if self.head is None:
            self.head = new_node
            return

        # Move to the last node
        current = self.head
        while current.next is not None:
            current = current.next

        # Connect the last node to the new node
        current.next = new_node

    # Display all values in the linked list
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Delete the first node with the target value
    def delete(self, target):
        current = self.head
        previous = None

        # Search for the target value
        while current is not None:
            if current.data == target:

                # If target is the first node, move the head
                if previous is None:
                    self.head = current.next
                else:
                    # Skip the node we want to delete
                    previous.next = current.next

                return True

            # Move to the next node
            previous = current
            current = current.next

        # Return False if the value is not found
        return False

    # Count the number of nodes
    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    # Convert the linked list into a Python list
    def to_list(self):
        values = []
        current = self.head

        while current is not None:
            values.append(current.data)
            current = current.next

        return values


# Test the linked list
ll = LinkedList()

for val in [10, 20, 30, 40, 50]:
    ll.insert_at_end(val)

ll.display()
print(ll.length())

print(ll.delete(30))
ll.display()

print(ll.to_list())

# Test deleting a value that does not exist
print(ll.delete(100))

# Part 2 - Stack Bracket Validator

def is_balanced(text):
    # Create an empty stack
    stack = []

    # Store opening and closing bracket pairs
    brackets = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    # Check each character in the text
    for char in text:

        # Add opening brackets to the stack
        if char in "([{":
            stack.append(char)

        # Check closing brackets
        elif char in ")]}":

            # If stack is empty, there is no opening bracket
            if not stack:
                return False

            # Remove the last opening bracket
            last = stack.pop()

            # Check if the brackets match
            if last != brackets[char]:
                return False

    # If stack is empty, all brackets matched
    return len(stack) == 0


# Test the bracket validator
print(is_balanced("()"))
print(is_balanced("({[]})"))
print(is_balanced("(]"))
print(is_balanced("([)]"))
print(is_balanced("hello (world)"))

# Part 3 - Queue Task Processor

# Import deque to create a queue
from collections import deque


class TaskProcessor:
    def __init__(self):
        # Create an empty queue
        self.tasks = deque()

    # Add a new task to the queue
    def add_task(self, name):
        self.tasks.append(name)

    # Process the oldest task first
    def process_next(self):

        # Return None if the queue is empty
        if not self.tasks:
            return None

        # Remove and return the first task
        return self.tasks.popleft()


# Test the task processor
processor = TaskProcessor()

# Add tasks
processor.add_task("Send email")
processor.add_task("Update report")
processor.add_task("Backup files")

# Process tasks in the order they were added
print(processor.process_next())
print(processor.process_next())
print(processor.process_next())

# Test an empty queue
print(processor.process_next())
