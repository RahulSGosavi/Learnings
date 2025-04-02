#Question: Write a function that takes an array of numbers and returns the largest value.

#Answer:

def find_max(arr):
    """
    Finds and returns the largest number in an array.

    :param arr: List of numbers
    :return: The largest number in the list
    """
     # Check if the array is empty
    if not arr: 
    # Return None for an empty array
        return None  
    
# Assume the first element is the largest
    max_value = arr[0]

# Loop through each number in the array  
    for num in arr:
    # If a number is greater than the current max_value
        if num > max_value: 
    # Update max_value 
            max_value = num
    # Return the largest number 
    return max_value

# Example usage:
numbers = [10, 45, 78, 23, 89, 34]
print("Largest number:", find_max(numbers))
