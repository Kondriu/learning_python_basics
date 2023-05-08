sum_of_nums = 0

with open('number.txt', 'w') as num_file:
    for num in range(1, 1000001):
        sum_of_nums += int(num)
        str = f'{num}: \t sum pf prevoius is {sum_of_nums}\n'
        num_file.write(str)