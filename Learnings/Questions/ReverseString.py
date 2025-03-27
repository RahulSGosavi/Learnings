#Write a function that reverses a string without using the built-in reverse() method
def reverse_string(s):
    return s[::-1] 

string = "Hello, World!"
print(reverse_string(string))