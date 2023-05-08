
cource_a = {'James', 'Mark', 'Kath', 'Brooke', 'Peter'}
cource_b = {'Sadme', 'Squesh', 'Kath', 'Mark', 'Joiee'}

# Students who took both cources (intersections)

intersect = cource_a & cource_b

print(f"toock both cources: {intersect}")

# Studens from all curses (union)
union = cource_b | cource_a

print(f'All students: {union}')


# Simmetric difference
# who took only one cource

sym_diff = cource_a ^ cource_b

print(f'Took only obe cource: {sym_diff}')