class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # make None as the default value for next.

def count_nodes(head):
    current = head # assuming that head != None
    count = 1
    
    while current.next is not None:
        current = current.next
        count += 1
        
    return count

node_a = Node(6)
node_b = Node(3)
node_c = Node(4)
node_d = Node(2)
node_e = Node(1)

node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e

print(f"This linked list's length (should be 5): {count_nodes(node_a)}")
