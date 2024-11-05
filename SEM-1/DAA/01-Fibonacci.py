# Recursive Fibonacci calculation
def fibonacci_recursive(n):
    """
    Recursive function to calculate Fibonacci number at position n.
    
    Parameters:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The Fibonacci number at position n.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Time complexity analysis
# The time complexity of the recursive Fibonacci calculation is O(2^n). This is because each call to the function results in two more calls, leading to an exponential growth in the number of function calls. This makes the recursive Fibonacci calculation inefficient for large values of n.

# Space complexity analysis
# The space complexity of the recursive Fibonacci calculation is O(n). This is because the function calls are stored on the call stack, and the depth of the call stack is proportional to the value of n. This can lead to stack overflow errors for large values of n.


# Iterative Fibonacci calculation
def fibonacci_iterative(n):
    """
    Iterative function to calculate Fibonacci number at position n.
    
    Parameters:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The Fibonacci number at position n.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Initialize variables to store the previous two Fibonacci numbers
    prev = 0
    curr = 1
    # Calculate the Fibonacci number at position n
    for i in range(2, n + 1): # n + 1 because range is exclusive
        next = prev + curr
        prev = curr
        curr = next
    return curr

# Time complexity analysis
# The time complexity of the iterative Fibonacci calculation is O(n). This is because the function iterates through the range of values from 2 to n, calculating the Fibonacci number at each position in constant time. This makes the iterative Fibonacci calculation more efficient than the recursive approach for large values of n.

# Space complexity analysis
# The space complexity of the iterative Fibonacci calculation is O(1). This is because the function uses a constant amount of space to store the previous two Fibonacci numbers and the current Fibonacci number. This makes the iterative Fibonacci calculation more memory-efficient than the recursive approach.