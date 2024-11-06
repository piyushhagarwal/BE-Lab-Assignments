# Recursive solution without memoization
class Solution:
    # Recursive function to solve the knapsack problem
    def solve(self, weight, index, value, n, max_weight):
        # Base case: If we are at the last item
        if index == n - 1:
            # Check if the weight of the last item exceeds the available capacity
            if max_weight < weight[n - 1]:
                return 0  # Cannot include the last item
            else:
                return value[index]  # Include the last item's value

        # Initialize the maximum value if the current item is included
        include = 0

        # Check if the weight of the current item is within the available capacity
        if max_weight >= weight[index]:
            include = value[index] + self.solve(weight, index + 1, value, n, max_weight - weight[index])

        # Calculate the maximum value by excluding the current item
        exclude = self.solve(weight, index + 1, value, n, max_weight)

        # Return the maximum value between including and excluding the current item
        return max(include, exclude)

    # Main function to solve the knapsack problem
    def knapsack(self, weight, value, n, max_weight):
        return self.solve(weight, 0, value, n, max_weight)

# Recursive solution with memoization
class Solution2:
    # Recursive function to solve the knapsack problem with memoization
    def solve(self, weight, index, value, n, max_weight, dp):
        # Base case: If we are at the last item
        if index == n - 1:
            if max_weight >= weight[n - 1]:
                return value[index]
            else:
                return 0

        # Check if result is already computed
        if dp[index][max_weight] != -1:
            return dp[index][max_weight]

        # Initialize the maximum value if the current item is included
        include = 0

        # Check if including the current item is feasible
        if max_weight - weight[index] >= 0:
            include = value[index] + self.solve(weight, index + 1, value, n, max_weight - weight[index], dp)

        # Calculate the maximum value by excluding the current item
        exclude = self.solve(weight, index + 1, value, n, max_weight, dp)

        # Memoize the result
        dp[index][max_weight] = max(include, exclude)
        return dp[index][max_weight]

    # Main function to solve the knapsack problem
    def knapsack(self, weight, value, n, max_weight):
        dp = [[-1 for _ in range(max_weight + 1)] for _ in range(n)]
        return self.solve(weight, 0, value, n, max_weight, dp)

# Test functions
def test_knapsack():
    # Test case 1
    weight = [1, 3, 4, 5]
    value = [1, 4, 5, 7]
    n = len(weight)
    max_weight = 7

    # Solution without memoization
    sol = Solution()
    result = sol.knapsack(weight, value, n, max_weight)
    print(f"Solution without memoization (max value for max_weight = 7): {result}")
    
    # Solution with memoization
    sol2 = Solution2()
    result = sol2.knapsack(weight, value, n, max_weight)
    print(f"Solution with memoization (max value for max_weight = 7): {result}")

    # Additional test cases for verification
    weight = [2, 3, 5, 7]
    value = [10, 5, 15, 7]
    n = len(weight)
    max_weight = 10

    result = sol.knapsack(weight, value, n, max_weight)
    print(f"Solution without memoization (max value for max_weight = 10): {result}")

    result = sol2.knapsack(weight, value, n, max_weight)
    print(f"Solution with memoization (max value for max_weight = 10): {result}")

# Run the test function
test_knapsack()
