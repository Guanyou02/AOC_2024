data = open('input.txt', 'r')

number_set = []

for line in data:
    numbers = line.split()
    number_set.append([int(num) for num in numbers])  # Convert strings to integers
data.close()

safe = 0

difference = [1, 2, 3]

for numbers in number_set:
    all_safe = False
    if sorted(numbers) == numbers or sorted(numbers, reverse=True) == numbers: # Sorted will not change the original array
        all_safe  = True
        for i in range((len(numbers)-1)):
            if abs(numbers[i+1] - numbers[i]) not in difference:
                all_safe = False
                break

    if not all_safe:
        for i in range(len(numbers)):
            print(numbers)
            modified_numbers = numbers[:i] + numbers[i + 1:]
            if sorted(modified_numbers) == modified_numbers or sorted(modified_numbers, reverse=True) == modified_numbers:
                all_safe = True
                break

    if all_safe:
        safe += 1

print(safe)