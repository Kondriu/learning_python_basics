import os

with open('number.txt', 'w') as num_file:
    for num in range(1, 1000001):
        num_file.write(f'{num}\n')
print('>finished creting new file')