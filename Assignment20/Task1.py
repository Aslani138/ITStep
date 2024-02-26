class Node:
    # Node class for each node in the binary tree
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    # BinaryTree class with root node initialization
    def __init__(self, root_value):
        self.root = Node(root_value)

    def printLeafNodes(self, node):
        # Prints the leaf nodes (nodes with no children)
        if node:
            if not node.left and not node.right:
                print(node.value, end=' ')
            self.printLeafNodes(node.left)
            self.printLeafNodes(node.right)

    def countEdges(self, node):
        # Counts the number of edges in the tree
        if not node or (not node.left and not node.right):
            return 0
        return 1 + self.countEdges(node.left) + self.countEdges(node.right)

# Example Usage
bt = BinaryTree(1)  # Creating a binary tree
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)

# Output leaf nodes and number of edges
print("Leaf Nodes:")
bt.printLeafNodes(bt.root)
print("\nNumber of Edges:", bt.countEdges(bt.root))
