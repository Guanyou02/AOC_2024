user_file = open('input.txt', 'r')

col1 = []
col2 = []

# Extract the data
for line in user_file:
    number = line.split();
    col1.append(number[0])
    col2.append(number[1])
user_file.close()

# Sort the data in ascending order
col1.sort()
col2.sort()

total_distance = 0;
for i in range(len(col1)):
    total_distance += abs(int(col1[i]) - int(col2[i]))
print(total_distance)