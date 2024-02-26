# Definition of the Node class
class Node:
    # Constructor to initialize the node
    def __init__(self, data):
        self.data = data  # Store the data in the node
        self.next = None  # Initialize the next pointer to None

# Definition of the LinkedList class
class LinkedList:
    # Constructor to initialize the linked list
    def __init__(self):
        self.head = None  # Initialize the head of the list to None

    # Method to append a new node at the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data

        # If the list is empty, make the new node the head of the list
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, traverse to the end of the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # Link the last node to the new node
        last_node.next = new_node

    # Method to insert a new node at a specified index
    def insert(self, data, index):
        new_node = Node(data)  # Create a new node with the given data

        # If inserting at the head, adjust the head pointer
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse the list to find the position to insert
        current_node = self.head
        current_index = 0
        while current_node.next and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        # Insert the new node at the correct position
        new_node.next = current_node.next
        current_node.next = new_node

    # Method to remove a node with specific data
    def remove(self, data):
        # If the list is empty, there's nothing to remove
        if self.head is None:
            return

        # If the head needs to be removed
        if self.head.data == data:
            self.head = self.head.next
            return

        # Otherwise, find the node to remove
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        # Remove the node if it exists
        if current_node.next:
            current_node.next = current_node.next.next

    # Method to display the contents of the list
    def display_info(self):
        current_node = self.head

        # Traverse through the list and print each node
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()

# Example usage of the LinkedList class
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(2)
linked_list.append(5)
linked_list.append(4)
linked_list.append(4)
linked_list.append(4)
linked_list.append(11)
linked_list.append(25)
linked_list.display_info()  # Display the list
linked_list.insert("Irakli", 3)  # Insert a node
linked_list.insert(10.1, 5)  # Insert another node
linked_list.display_info()  # Display the list after insertion
linked_list.remove("Irakli")  # Remove a node
linked_list.remove(4)  # Remove another node
linked_list.display_info()  # Display the final list
