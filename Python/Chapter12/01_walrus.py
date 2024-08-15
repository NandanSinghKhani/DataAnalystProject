# Using walrus operator
numbers = [1, 2, 3, 4, 5] 
if (n := len(numbers)) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") # Output: List is too long (5 elements, expected <= 3)