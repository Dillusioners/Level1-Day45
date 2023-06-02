def find_most_frequent(numbers):
    # Create a dictionary to store the frequency of each number
    frequency = {}

    # Iterate over the list of numbers
    for number in numbers:
        # If the number is already in the dictionary, increment its count
        if number in frequency:
            frequency[number] += 1
        # If the number is not in the dictionary, add it with count 1
        else:
            frequency[number] = 1

    # Find the number with the maximum frequency
    most_frequent_number = max(frequency, key=frequency.get)

    return most_frequent_number

# Example usage
numbers = [1, 3, 5, 2, 1, 3, 2, 2, 4, 1, 5, 1]
most_frequent = find_most_frequent(numbers)
print("The number that appears most frequently is:", most_frequent)
