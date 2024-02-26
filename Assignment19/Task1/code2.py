# Definition of the Node class
class Node:
    # Constructor to initialize the node
    def __init__(self, data):
        self.data = data  # Store the data in the node
        self.next = None  # Initialize the next pointer to None

# Definition of the Stack class using a linked list
class Stack:
    # Constructor to initialize the stack
    def __init__(self):
        self.top_node = None  # Initialize the top node of the stack to None
        self.length = 0  # Initialize the length (size) of the stack to 0

    # Method to check if the stack is empty
    def empty(self):
        return self.length == 0  # Return True if the stack is empty

    # Method to get the current size of the stack
    def size(self):
        return self.length  # Return the number of elements in the stack

    # Method to get the top element of the stack
    def top(self):
        if not self.empty():
            return self.top_node.data  # Return the data of the top node
        else:
            raise IndexError("Stack Is Empty")  # Raise error if the stack is empty

    # Method to push a new element onto the stack
    def push(self, data):
        new_node = Node(data)  # Create a new node with the given data

        # Place the new node on top of the stack
        new_node.next = self.top_node
        self.top_node = new_node
        self.length += 1  # Increment the stack size

    # Method to pop the top element from the stack
    def pop(self):
        if not self.empty():
            popped_item = self.top_node.data  # Store the data of the top node
            self.top_node = self.top_node.next  # Remove the top node
            self.length -= 1  # Decrement the stack size
            return popped_item  # Return the popped item
        else:
            raise IndexError("Stack Is Empty")  # Raise error if the stack is empty

# Example usage of the Stack class
stack = Stack()
stack.push(1)  # Push elements onto the stack
stack.push(5)
stack.push(2)
stack.push(8)
stack.push(10)

print(stack.size())  # Print the size of the stack
print(stack.pop())   # Pop and print elements from the stack
print(stack.size())
print(stack.pop())
print(stack.size())
print(stack.pop())
print(stack.size())
print(stack.pop())
print(stack.size())
print(stack.pop())   # Stack should be empty after this pop
