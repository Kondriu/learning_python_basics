things = ('Cup', 'Fan', 'Car', 'Mug', 'Glas', 'Mug')

print(things)

#count number of "Mug" appars
mug = things.count("Mug") 
print(f"Mug appers by {mug} times.")

# index of 'Mug'
mug_index = things.index("Mug")
print(f"Index of 'Mug' is: {mug_index}.")

#first item
first_item = things[0];
print(f'first item: {first_item}.')

#tuple immutable
#things[0] = 'New items' 
# #causes error: TypeError: 'tuple' object does not support item assignment