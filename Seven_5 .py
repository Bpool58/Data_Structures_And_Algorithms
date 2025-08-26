# Function to maintain max heap property by moving a node down the heap. until it's in the correct position
def max_heap_percolate_down(node_index, heap_list, list_size):
    # Calculate the index of the left child using the heap property formula
    # (for any node at index i, left child is at 2i + 1)
    child_index = 2 * node_index + 1
    
    # Store the value of the current node we're trying to percolate down
    value = heap_list[node_index]

    # Continue while there are still children to compare with.
    # (while the left child index is within the heap size).
    while child_index < list_size:
        # Initialize variables for finding the maximum value among parent and children
        max_value = value          # Start with parent's value as max
        max_index = -1            # Will store the index of the maximum value
        i = 0                     # Counter to check both left (i=0) and right (i=1) children
        
        # Check both children (if they exist)
        while i < 2 and i + child_index < list_size:
            # If child is greater than current max_value
            if heap_list[i + child_index] > max_value:
                # Update max_value to be this child's value
                max_value = heap_list[i + child_index]
                # Store this child's index
                max_index = i + child_index
            i = i + 1    # Move to check the next child

        # If the parent is already the largest value, we're done
        if max_value == value:
            return

        # Swap the parent with the larger child using a temporary variable
        temp = heap_list[node_index]
        heap_list[node_index] = heap_list[max_index]
        heap_list[max_index] = temp

        # Update indices to continue percolating down
        node_index = max_index                # Move to the position we just swapped with
        child_index = 2 * node_index + 1     # Calculate new left child index


# Main heap sort function that sorts an array in-place
def heap_sort(numbers):
    # Phase 1: Build max heap (heapify)
    # Start from last non-leaf node (len//2 - 1) and work backwards to root
    i = len(numbers) // 2 - 1
    while i >= 0:
        # Call max_heap_percolate_down on each node to ensure max heap property
        max_heap_percolate_down(i, numbers, len(numbers))
        i = i - 1

    # Phase 2: Extract elements from heap one by one
    i = len(numbers) - 1
    while i > 0:
        # Swap root (largest element) with last unsorted position
        temp = numbers[0]
        numbers[0] = numbers[i]
        numbers[i] = temp

        # Restore max heap property for remaining elements
        # Note: i is used as size because we're reducing heap size by 1 each iteration
        max_heap_percolate_down(0, numbers, i)
        i = i - 1    # Move to next last unsorted position