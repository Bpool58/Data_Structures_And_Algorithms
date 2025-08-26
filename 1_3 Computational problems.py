def find_max(input_array):
    # Handle the edge case of an empty array
    # Return None if the array is empty to avoid errors
    if not input_array:
        return None
    
    # Initialize our maximum value with the first element
    # This gives us a starting point for comparisons
    max_value = input_array[0]
    
    # Iterate through the array starting from index 1
    # We start from 1 because we already used element at index 0 as initial max
    # range(1, len(input_array)) creates a sequence from 1 to len(input_array)-1
    for i in range(1, len(input_array)):
        # Compare current element with our current maximum
        # If we find a larger element, update our maximum
        if input_array[i] > max_value:
            max_value = input_array[i]
    
    # After examining all elements, return the largest value found
    return max_value


# Alternative implementation using Python's built-in max() function
def find_max_simple(input_array):
    # max() handles empty sequences by raising ValueError
    # so we need to check for empty input
    if not input_array:
        return None
    
    # max() efficiently finds the maximum value in any iterable
    # it uses optimized C implementation under the hood
    return max(input_array)