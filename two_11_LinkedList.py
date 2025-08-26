class LinkedList:
    """
    A doubly linked list implementation that maintains references to both head and tail nodes.
    Supports operations: append, prepend, insert_after, and remove.
    """
    def __init__(self):
        """
        Initialize an empty linked list.
        Head and tail are set to None, indicating an empty list.
        """
        self.head = None  # Points to the first node in the list
        self.tail = None  # Points to the last node in the list

    def append(self, new_node):
        """
        Add a new node to the end of the list.
        
        Time Complexity: O(1) - constant time operation
        
        Args:
            new_node: The node to append
            
        State changes:
            Empty list: new_node becomes both head and tail
            Non-empty list: new_node becomes new tail, linked to old tail
        """
        if self.head == None:  # List is empty
            self.head = new_node  # new_node becomes the first node
            self.tail = new_node  # new_node is also the last node
        else:  # List has at least one node
            self.tail.next = new_node      # Link current tail to new node
            new_node.prev = self.tail      # Link new node back to current tail
            self.tail = new_node           # Update tail to new node

    def prepend(self, new_node):
        """
        Add a new node to the start of the list.
        
        Time Complexity: O(1) - constant time operation
        
        Args:
            new_node: The node to prepend
            
        State changes:
            Empty list: new_node becomes both head and tail
            Non-empty list: new_node becomes new head, linked to old head
        """
        if self.head == None:  # List is empty
            self.head = new_node  # new_node becomes the first node
            self.tail = new_node  # new_node is also the last node
        else:  # List has at least one node
            new_node.next = self.head      # Link new node to current head
            self.head.prev = new_node      # Link current head back to new node
            self.head = new_node           # Update head to new node

    def insert_after(self, current_node, new_node):
        """
        Insert a new node after a given node in the list.
        
        Time Complexity: O(1) - constant time operation
        
        Args:
            current_node: Node after which to insert
            new_node: Node to insert
            
        State changes:
            Empty list: new_node becomes both head and tail
            Insert after tail: new_node becomes new tail
            Insert in middle: new_node links to both predecessor and successor
        """
        if self.head is None:  # List is empty
            self.head = new_node  # new_node becomes the first node
            self.tail = new_node  # new_node is also the last node
        elif current_node is self.tail:  # Inserting after tail
            self.tail.next = new_node       # Link current tail to new node
            new_node.prev = self.tail       # Link new node back to current tail
            self.tail = new_node            # Update tail to new node
        else:  # Inserting between nodes
            successor_node = current_node.next   # Save the next node
            new_node.next = successor_node       # Link new node to successor
            new_node.prev = current_node         # Link new node to current
            current_node.next = new_node         # Link current to new node
            successor_node.prev = new_node       # Link successor back to new node

    def remove(self, current_node):
        """
        Remove the specified node from the list.
        
        Time Complexity: O(1) - constant time operation
        
        Args:
            current_node: The node to remove
            
        State changes:
            Updates next/prev links of surrounding nodes
            Updates head/tail if removing first/last node
        """
        successor_node = current_node.next      # Save next node
        predecessor_node = current_node.prev    # Save previous node

        # Update successor's prev pointer
        if successor_node is not None:
            successor_node.prev = predecessor_node

        # Update predecessor's next pointer
        if predecessor_node is not None:
            predecessor_node.next = successor_node

        # Update head if removing first node
        if current_node is self.head:
            self.head = successor_node

        # Update tail if removing last node
        if current_node is self.tail:
            self.tail = predecessor_node