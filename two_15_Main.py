class Node:
    """
    Represents a single node in a doubly linked list.
    Each node contains data and pointers to both next and previous nodes.
    """
    def __init__(self, data):
        """
        Constructor to create a new node with given data.
        
        Args:
            data: The value to store in this node
        """
        self.data = data    # Store the actual data/value in this node
        self.next = None    # Pointer to the next node (initially no connection)
        self.prev = None    # Pointer to the previous node (initially no connection)

# ==============================================================================
# DOUBLY LINKED LIST CLASS DEFINITION
# ==============================================================================

class LinkedList:
    """
    A doubly linked list where each node points to both next and previous nodes.
    Maintains references to both the first (head) and last (tail) nodes.
    """
    def __init__(self):
        """
        Constructor to create an empty linked list.
        """
        self.head = None    # Pointer to the first node (empty list = None)
        self.tail = None    # Pointer to the last node (empty list = None)
    
    def append(self, node):
        """
        Add a new node to the end of the list.
        
        Args:
            node: The node object to add to the list
        """
        if self.head is None:
            # Case 1: List is completely empty
            self.head = node    # This node becomes the first node
            self.tail = node    # This node is also the last node (only one node)
        else:
            # Case 2: List already has at least one node
            self.tail.next = node    # Current last node points forward to new node
            node.prev = self.tail    # New node points backward to current last node
            self.tail = node         # Update tail pointer to new last node
    
    def insertion_sort_doubly_linked(self):
        """
        Sorts the doubly linked list using insertion sort algorithm.
        Works by taking each node and inserting it into its correct position
        among the already sorted nodes to its left.
        
        Time Complexity: O(n²) in worst case, O(n) in best case (already sorted)
        Space Complexity: O(1) - sorts in place
        """
        
        # Edge cases: empty list or single node list is already sorted
        if self.head is None or self.head.next is None:
            return    # Nothing to sort, exit early
        
        # Start with the second node (first node is considered "sorted" by itself)
        current = self.head.next
        
        # Process each node from left to right
        while current is not None:
            # Save the next node before we potentially move current
            next_node = current.next
            
            # Start searching backwards from current node's left neighbor #PTR references POINTER (:
            search_ptr = current.prev
            
            # STEP 1: Find the correct position for current node
            # Move backwards while we find nodes with larger values
            while search_ptr is not None and search_ptr.data > current.data:
                search_ptr = search_ptr.prev    # Keep moving left
            
            # STEP 2: Check if current node is already in correct position
            if search_ptr == current.prev:
                # Current node is already in the right place, no movement needed
                current = next_node    # Move to next node to process
                continue               # Skip the removal and insertion steps
            
            # STEP 3: Remove current node from its current position
            # We need to "unlink" current from where it currently sits
            
            if current.next is not None:
                # If current is not the tail, update the next node's prev pointer
                current.next.prev = current.prev
            else:
                # If current is the tail, update tail to point to previous node
                self.tail = current.prev
            
            # Update the previous node's next pointer (current.prev is never None here)
            current.prev.next = current.next
            
            # STEP 4: Insert current node at its new correct position
            
            if search_ptr is None:
                # Case A: Insert at the very beginning of the list
                current.prev = None           # New first node has no previous
                current.next = self.head      # Point to current first node
                self.head.prev = current      # Old first node points back to new first
                self.head = current           # Update head pointer to new first node
            else:
                # Case B: Insert somewhere in the middle (after search_ptr)
                current.next = search_ptr.next       # Point to node that comes after search_ptr
                current.prev = search_ptr            # Point back to search_ptr
                search_ptr.next.prev = current       # Next node points back to current
                search_ptr.next = current            # search_ptr points forward to current
            
            # STEP 5: Move to the next node to process
            current = next_node

# ==============================================================================
# MAIN PROGRAM EXECUTION
# ==============================================================================

# Create an empty linked list to hold our numbers
num_list = LinkedList()

# Create individual node objects with different integer values
node_a = Node(72)    # Create node containing the value 72
node_b = Node(91)    # Create node containing the value 91
node_c = Node(53)    # Create node containing the value 53
node_d = Node(12)    # Create node containing the value 12

# Add all nodes to the list in the order: 72 -> 91 -> 53 -> 12
num_list.append(node_a)    # List: [72]
num_list.append(node_b)    # List: [72, 91]
num_list.append(node_c)    # List: [72, 91, 53]
num_list.append(node_d)    # List: [72, 91, 53, 12]

# Display the original unsorted list
print('List after adding nodes:', end=' ')    # Print label without newline
node = num_list.head                           # Start at the first node
while node != None:                            # Continue until we reach the end
    print(node.data, end=' ')                  # Print current node's data
    node = node.next                           # Move to the next node
print()                                        # Print a newline at the end

# Sort the list using insertion sort algorithm
num_list.insertion_sort_doubly_linked()

# Display the sorted list
print('List after insertion sort:', end=' ')  # Print label without newline
node = num_list.head                           # Start at the first node again
while node != None:                            # Continue until we reach the end
    print(node.data, end=' ')                  # Print current node's data
    node = node.next                           # Move to the next node
print()                                        # Print a newline at the end

# Expected output:
# List after adding nodes: 72 91 53 12 
# List after insertion sort: 12 53 72 91