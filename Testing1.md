## Problem
You have a list of numbers, and you want to select some of them in a way that their total sum comes as close as possible to a target number.
### Solving the Problem
iteratively select numbers from the list such that their sum is as close as possible to the target value using the hill climbing algorithm.
```
    import random
    def find_closest_subset(numbers, target):
        current_sum = 0
        selected_numbers = []
        
        while current_sum != target:
            num = random.choice(numbers)
            
            # Check if adding the number gets closer to the target sum
            if abs(current_sum + num - target) < abs(current_sum - target):
                selected_numbers.append(num)
                current_sum += num
        
        return selected_numbers
    
    numbers = [3, 7, 12, 5, 9, 2]
    target = 20
    solution = find_closest_subset(numbers, target)
    print("Subset with sum closest to the target:", solution)
    print("Sum:", sum(solution))
```
