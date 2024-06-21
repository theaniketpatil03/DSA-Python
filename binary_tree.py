'''
for no duplications
for sorting, searching
makes search base half at every iterationkf
'''

class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data == self.data:
            return 
        
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = BinaryTree(data)
        
        if data > self.data:
            if self.right:
                self.right.add(data)
            else:
                self.right = BinaryTree(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree first
        if self.left:
            elements += self.left.in_order_traversal()
        
        # visit base node
        elements.append(self.data)

        # visit right base node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val)
            else: 
                return False
        
        if val > self.data:
            # val might be in right subtree

            if self.right:
                return self.right.search(val)
            else:
                return False

    

def build_tree(elements):
    root = BinaryTree(elements[0])

    for elem in elements:
        root.add(elem)

    return root


numbers = [2, 1, 0, 5, 8, 10, 9]
strings = ['aniket', 'patil', 'sunil', 'akanksha', 'aaditya', 'anushka', 'pawar', 'santosh']

tree = build_tree(numbers)
string_tree = build_tree(strings)
print(tree.in_order_traversal())
print(tree.search(20))
print(string_tree.in_order_traversal())

    