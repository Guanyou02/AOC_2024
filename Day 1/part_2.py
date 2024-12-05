user_file = open('input.txt', 'r')

col1 = []
col2 = []

# Extract the data
for line in user_file:
    number = line.split();
    col1.append(number[0])
    col2.append(number[1])
user_file.close()

similarity = 0
for i in range(len(col1)):
    similarity += int(col2.count(col1[i])) * int(col1[i])
print(similarity)