
students_count = {
    'cource1': 923,
    'cource2': 1985,
    'cource3': 332,
}

# for loop through items on dictionary 
for k, v in students_count.items():
    print(f"{k}: {v}")

#count the totul num of stidents
total_students = 0
for k,v in students_count.items():
    total_students += v
    #total_students = total_students + v
print(f"Total students: {total_students}")


#get all keys
cources = students_count.keys()

print(f"cources is: {cources}")
