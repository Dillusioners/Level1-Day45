def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two numbers

    while True:
        # Generate the next number in the sequence by summing the previous two numbers
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        
        # Check if the next number exceeds the limit
        if next_number > limit:
            break

        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Taking limit from user.
limit = int(input("Enter the limit:- "))
fibonacci_sequence = generate_fibonacci(limit)
print("Fibonacci sequence up to", limit, ":")
print(fibonacci_sequence)
