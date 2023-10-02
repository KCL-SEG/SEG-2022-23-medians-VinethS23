"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
#integer division - x//y = x divided by y, the answer is rounded DOWN to the nearest int

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        itemCount = len(numbers) # not numbers.len()
        numbers.sort()
        if (itemCount % 2) == 1:
            median = numbers[itemCount//2]
        elif (itemCount % 2) == 0:
            x = itemCount//2
            y = (itemCount//2)+1
            median = (numbers[x] + numbers[y])//2
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print("Median: ", median)
print(numbers)