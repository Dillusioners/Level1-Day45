'''
Author - Debag101
Purpose - Checks if a string is palindrome or not
Date - 02 - 06 - 2023
'''

# Main method
def main():
    # Gets the string via input
    string_original = input("Enter the string => ")
    
    # Checks if string is equal to itself reversed
    if string_original == string_original[::-1]: 
        print(f"{string_original} is a palindrome !") # If condition is true
    else:
        print(f"{string_original} is not a palindrome !") # If condition is false

# Invoking main
if __name__ == '__main__':
    main()
