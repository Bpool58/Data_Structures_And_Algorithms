# Import required Node and LinkedList classes
from Node import Node
from LinkedList import LinkedList

# Create a new empty linked list
num_list = LinkedList()

# Create individual nodes with their data values
node_a = Node(14)    # Create node with value 14
node_b = Node(2)     # Create node with value 2
node_c = Node(20)    # Create node with value 20
node_d = Node(31)    # Create node with value 31
node_e = Node(16)    # Create node with value 16
node_f = Node(55)    # Create node with value 55

# Build the linked list using different insertion methods
num_list.append(node_a)   # List: 14
num_list.append(node_b)   # List: 14 -> 2
num_list.append(node_c)   # List: 14 -> 2 -> 20

# Add node_d at the beginning of the list
num_list.prepend(node_d)  # List: 31 -> 14 -> 2 -> 20

# Insert node_e after node_b (value 2)
num_list.insert_after(node_b, node_e)  # List: 31 -> 14 -> 2 -> 16 -> 20

# Insert node_f after node_c (current tail)
num_list.insert_after(node_c, node_f)  # List: 31 -> 14 -> 2 -> 16 -> 20 -> 55

# Print the current state of the list
print('List after adding nodes:', end=' ')
# Traverse the list from head to end
node = num_list.head
while node != None:
    print(node.data, end=' ')  # Print each node's data
    node = node.next          # Move to the next node
print()  # New line after printing all nodes

# Remove nodes from the list
num_list.remove(node_f)  # Remove 55 (tail node)
num_list.remove(node_d)  # Remove 31 (head node)
# List is now: 14 -> 2 -> 16 -> 20

# Print the final state of the list
print('List after removing nodes:', end=' ')
# Traverse the list again from head to end
node = num_list.head
while node != None:
    print(node.data, end=' ')  # Print each node's data
    node = node.next          # Move to the next node
print()  # New line after printing all nodes