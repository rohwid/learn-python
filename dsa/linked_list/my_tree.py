class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum_values(root):
    if (root == None):
        return 0
    return root.data + sum_values(root.left) + sum_values(root.right)


#  Our example tree looks like this:
#         1
#       /   \
#      2     3
#     / \
#    4   5

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_2.right = node_5

print(f"Sum of all values of this tree (should be 15): {sum_values(node_1)}")