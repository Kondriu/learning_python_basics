sum_of_nums = 0

with open('number.txt', 'w') as nf:
    for num in nf:
        sum_of_nums += int(num)
        

print(sum_of_nums)