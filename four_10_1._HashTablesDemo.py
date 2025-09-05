# Import different hash table implementations to compare their behaviors
# Note: These imports may show errors if the corresponding files don't exist yet
from ChainingHashTable import ChainingHashTable
from LinearProbingHashTable import LinearProbingHashTable
from QuadraticProbingHashTable import QuadraticProbingHashTable
from DoubleHashingHashTable import DoubleHashingHashTable

# Test data: City names as keys, airport codes as values
# This represents a mapping of cities to their primary airport codes
keys = [
    "Los Angeles", "Houston", "Washington",        # First 3 cities
    "Chicago", "San Francisco", "Dallas",          # Next 3 cities
    "Tokyo", "New York", "Vancouver"               # Last 3 cities
]

# Corresponding airport codes for each city
values = [
    "LAX", "IAH", "IAD",    # Airport codes for Los Angeles, Houston, Washington
    "ORD", "SFO", "DAL",    # Airport codes for Chicago, San Francisco, Dallas
    "NRT", "JFK", "YVR"     # Airport codes for Tokyo, New York, Vancouver
]

# Set initial capacity for all hash tables
# Using 11 (a prime number) is good practice for hash table sizing
initialCapacity = 11

# Create instances of four different hash table implementations
# This allows us to compare how different collision resolution strategies work
tables = [
    # Chaining: Uses linked lists to handle collisions
    ChainingHashTable(initialCapacity),
    
    # Linear Probing: Uses open addressing, checks next available slot sequentially
    LinearProbingHashTable(initialCapacity),
    
    # Quadratic Probing: Uses open addressing with quadratic function (1^2, 2^2, 3^2...)
    # Parameters: c1=1, c2=1 for the quadratic function: hash + c1*i + c2*i^2
    QuadraticProbingHashTable(1, 1, initialCapacity),
    
    # Double Hashing: Uses two hash functions to determine probe sequence
    DoubleHashingHashTable(initialCapacity)
]

# Insert the same key-value pairs into each hash table
# This allows us to see how each collision resolution method handles the same data
for i in range(len(keys)):  # Iterate through each key-value pair
    # Insert current key-value pair into each of the four hash tables
    for j in range(len(tables)):  # Iterate through each hash table type
        # Insert city name (key) and airport code (value) into current table
        tables[j].insert(keys[i], values[i])

# Create descriptive names for each hash table type for display purposes
tableNames = [
    "Chaining",           # Uses separate chaining with linked lists
    "Linear probing",     # Uses linear probing for collision resolution
    "Quadratic probing",  # Uses quadratic probing for collision resolution
    "Double hashing"      # Uses double hashing for collision resolution
]

# Display the contents of each hash table after all insertions
for j in range(len(tables)):  # Iterate through each hash table
    # Print header showing which type of hash table we're displaying
    print("%s: initial table:" % tableNames[j])
    
    # Print the hash table contents (this calls the __str__ method of each table)
    print(tables[j])

# Demonstrate removal operation by removing the first 3 key-value pairs
# This shows how each collision resolution method handles deletions
for i in range(3):  # Remove first 3 entries: "Los Angeles", "Houston", "Washington"
    for j in range(len(tables)):  # Remove from each hash table type
        # Remove the current key from the current hash table
        tables[j].remove(keys[i])

# Note: After removals, you could print the tables again to see the effect:
# print("\nAfter removing first 3 entries:")
# for j in range(len(tables)):
#     print("%s:" % tableNames[j])
#     print(tables[j])


class ChainingHashTableItem:
    """
    Represents a single node in a linked list for chaining hash table collision resolution.
    
    This class is used in hash tables that implement separate chaining - when multiple
    keys hash to the same bucket, they are stored in a linked list structure.
    """
    
    def __init__(self, itemKey, itemValue):
        """
        Initialize a new hash table item (node in the linked list).
        
        Args:
            itemKey: The key to store in this node
            itemValue: The value associated with the key
        """
        # Store the key-value pair
        self.key = itemKey      # The key for this hash table entry
        self.value = itemValue  # The value associated with the key
        
        # Initialize the link to the next node in the chain
        # None indicates this is currently the last node in the chain
        self.next = None