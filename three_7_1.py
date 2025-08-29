class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_after(self, current_node):
        # Special case, remove head
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self.head = succeeding_node
            if succeeding_node == None:  # Remove last item
                self.tail = None
        elif current_node is not None and current_node.next != None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None:  # Remove tail
                self.tail = current_node


class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)
        # Insert the node as the list head (top of stack)
        self.list.prepend(new_node)

    def pop(self):
        # Check if stack is empty
        if self.list.head is None:
            raise IndexError("pop from empty stack")
        
        # Copy data from list's head node (stack's top node)
        popped_item = self.list.head.data
        # Remove list head
        self.list.remove_after(None)
        # Return the popped item
        return popped_item

    def is_empty(self):
        return self.list.head is None


num_stack = Stack()
num_stack.push(45)
num_stack.push(56)
num_stack.push(11)

# Output stack
print('Stack after push:', end=' ')
node = num_stack.list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()

# Pop 11
popped_item = num_stack.pop()
print('Popped:', popped_item)

# Output final stack
print('Stack after pop:', end=' ')
node = num_stack.list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print('\n')