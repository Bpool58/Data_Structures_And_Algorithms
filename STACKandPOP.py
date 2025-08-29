from three_7_1_Stack import Stack

from three_7_1_Quene import Queue

# stack operations

num_stack = Stack()

num_stack.push(45)
num_stack.push(56)
num_stack.push(11)

#Output stack

print('Stack after push:', end=' ')

node = num_stack.list.head

while node != None:
    print(node.data, end=' ')
    node = node.next
print()

# POP 11

popped_item = num_stack.pop()

print('Popped:', popped_item)

#Output Final Stack
print('Stack after pop: ', end=' ')
node = num_stack.list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print('\n')




