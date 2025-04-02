#Question. Write a function that checks if a given string is a palindrome (same forwards and backwards).

#Solustion:
def is_palindrome(s):
    """
    Checks if a given string is a palindrome.
    
    :param s: The input string
    :return: True if the string is a palindrome, False otherwise
    """
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Check if the string is the same when reversed

# Example usage:
word = input("Enter a string: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
