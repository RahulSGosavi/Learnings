def is_palindrome(s):
    """
    Checks if a given string is a palindrome.
    
    :param s: The input string
    :return: True if the string is a palindrome, False otherwise
    """
    s = s.lower().replace(" ", "") 
    return s == s[::-1] 

# Example usage:
word = input("Enter a string: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")