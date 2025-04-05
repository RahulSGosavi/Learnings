# Question : Write a function that takes an array of numbers and returns the sum.

# Answer:
def calculate_sum(arr):
    """
    Calculates and returns the sum of numbers in an array.

    :param arr: List of numbers
    :return: Sum of the numbers
    """
    total = 0  # Initialize sum as 0
    for num in arr:  # Loop through each number in the array
        total += num  # Add each number to total
    return total  # Return the final sum

# Example usage:
numbers = [10, 20, 30, 40]
print("Sum of the array:", calculate_sum(numbers))
