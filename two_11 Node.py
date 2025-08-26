class Node:
    """
    A Node class for a doubly linked list that stores data and maintains references to next and previous nodes.
    """
    def __init__(self, initial_data):
        """
        Initialize a new node with data and null references to next and previous nodes.
        
        Args:
            initial_data: The data to be stored in the node (can be any data type)
        
        Attributes:
            data: Stores the node's data
            next: Reference to the next node (None by default)
            prev: Reference to the previous node (None by default)
        """
        self.data = initial_data    # Store the actual data in the node
        self.next = None            # Reference to the next node (initially None)
        self.prev = None            # Reference to the previous node (initially None)