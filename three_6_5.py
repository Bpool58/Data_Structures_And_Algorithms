def resize(self):
    # Calculate the new size by doubling the current queue capacity
    # This is a common strategy for dynamic arrays to maintain amortized O(1) insertion
    new_size = len(self.queue_list) * 2
    
    # Check if there's a maximum length limit and if our new size would exceed it
    # self.max_length >= 0 means there IS a maximum limit (negative values might indicate no limit)
    if self.max_length >= 0 and new_size > self.max_length:
        # If we would exceed the limit, cap the new size to the maximum allowed
        new_size = self.max_length

    # Create a new list filled with zeros (or you could use None)
    # This will be our new, larger queue storage
    new_list = [0] * new_size
    
    # Copy all existing elements from the old circular queue to the new linear arrangement
    # We iterate through all current elements (self.length is the number of items in queue)
    for i in range(self.length):
        # Calculate the actual index in the old circular queue
        # self.front_index is where the queue starts, and we use modulo to wrap around
        # This handles the circular nature of the original queue
        item_index = (self.front_index + i) % len(self.queue_list)
        
        # Copy the element to the new list in linear order (index i)
        # This "linearizes" the circular queue data
        new_list[i] = self.queue_list[item_index]

    # Replace the old queue with the new, larger one
    self.queue_list = new_list
    
    # Reset the front index to 0 since we've linearized the data
    # All elements are now stored starting from index 0
    self.front_index = 0