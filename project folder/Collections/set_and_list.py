#list
fruit = ['apple', 'orange', 'lemon', 'apple', 'orange']

#set:
#fruit = {'apple', 'orange', 'lemon', 'apple', 'orange'}

print(f"Fruit as set: {fruit}")

#convert List to Set
fruit_set = set(fruit)

print(f"Fruit as set: {fruit_set}")

#convert Set to List
fruit_list = list(fruit_set)
print(f"Fruits as list from set: \t {fruit_list}")

#make list_unic short

fruit_list_uniques=list(set(fruit))
print(f"Fruits unique list:\t\t {fruit_list_uniques}")