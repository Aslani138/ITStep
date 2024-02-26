class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def delete_at_index(self, index):
        if self.head is None:
            raise ValueError("List is empty")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        current_index = 0
        while current is not None and current_index < index - 1:
            current = current.next
            current_index += 1

        if current is None or current.next is None:
            raise IndexError("Index out of bounds")

        current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Example usage
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list.display()  # Display the list

# Deleting elements by index
try:
    linked_list.delete_at_index(2)
    linked_list.display()  # Display list after deletion

    linked_list.delete_at_index(0)
    linked_list.display()  # Display list after another deletion
except (IndexError, ValueError) as e:
    print(e)
