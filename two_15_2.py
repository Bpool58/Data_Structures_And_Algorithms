def insertion_sort_singly_linked(self):
    before_current = self.head
    current_node = self.head.next
    while current_node != None:
        next_node = current_node.next
        position = self.find_insertion_position(current_node.data)
        if position == before_current:
            before_current = current_node
        else:
            self.remove_after(before_current)
            if position == None:
                self.prepend(current_node)
            else:
                self.insert_after(position, current_node)
        current_node = next_node

def find_insertion_position(self, data_value):
    position_a = None
    position_b = self.head
    while (position_b != None) and (data_value > position_b.data):
        position_a = position_b
        position_b = position_b.next
    return position_a