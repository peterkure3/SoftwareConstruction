def sum_of_even(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum

# Test Case 1: Regular positive integers
assert sum_of_even([1, 2, 3, 4, 5, 6]) == 12

# Test Case 2: Regular mixed positive and negative integers
assert sum_of_even([-1, 2, -3, 4, -5, 6]) == 12

# Test Case 3: All even numbers
assert sum_of_even([2, 4, 6, 8, 10]) == 30

# Test Case 4: All odd numbers
assert sum_of_even([1, 3, 5, 7, 9]) == 0

# Test Case 5: Empty list
assert sum_of_even([]) == 0

print("All tests passed successfully!")
