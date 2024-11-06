# The Fractional Knapsack problem is a classic optimization problem that can be solved using a greedy approach. Unlike the 0/1 Knapsack problem, where items can only be taken fully or left behind, in the fractional knapsack problem, items can be divided into fractions, allowing us to take parts of an item to maximize the total value.

# Problem Description
# Given:
# A knapsack with a maximum weight capacity.
# A set of items, each with a specific weight and value.

# Objective:

# Maximize the total value in the knapsack by selecting items (or fractions of items) to fill the knapsack without exceeding the weight capacity.
# Greedy Strategy
# Calculate the value-to-weight ratio for each item.
# Sort items in descending order based on this ratio.
# Pick items in order of highest ratio until the knapsack is full. If an item can't be fully added due to weight constraints, take the fraction that fits.

# Example
# Let’s say we have a knapsack capacity of 50 and the following items:

# Item	Weight	Value	Value/Weight
# 1	    10	    60	    6
# 2	    20	    100	    5
# 3	    30	    120	    4
# The greedy strategy would select items by their highest value-to-weight ratio first.



# Class to represent an item with weight and value
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
    
    # Method to calculate value-to-weight ratio
    def value_per_weight(self):
        return self.value / self.weight

def fractional_knapsack(capacity, items):
    """
    Solve the fractional knapsack problem using a greedy approach.
    
    Parameters:
    capacity (int): The maximum weight capacity of the knapsack.
    items (list of Item): List of items with specific weights and values.
    
    Returns:
    float: The maximum value that can be obtained with the given capacity.
    """
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.value_per_weight(), reverse=True)
    
    total_value = 0.0  # Total value of items taken
    for item in items:
        # Check if item can be taken fully
        if capacity >= item.weight:
            capacity -= item.weight  # Reduce knapsack capacity
            total_value += item.value  # Add full value of item
        else:
            # Take fraction of the item that fits in the remaining capacity
            total_value += item.value_per_weight() * capacity
            break  # Knapsack is full, exit loop
    
    return total_value

# Testing the function
if __name__ == "__main__":
    # Define items with weight and value
    items = [
        Item(10, 60),
        Item(20, 100),
        Item(30, 120)
    ]
    capacity = 50
    max_value = fractional_knapsack(capacity, items)
    
    print(f"The maximum value for the given knapsack capacity is: {max_value}")
