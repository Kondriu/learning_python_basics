names = ["Mark", "Sad", "Susy", "Sveta"]

#update name
names[2] = "Michael"

#append name
names.append("Boghdan")

#extends list by 
#names.extend(list2)
names.extend(["Sade", "Sasha"])

#remove
names.remove('Sveta')

#remove 
removed_from_list = names.pop(0)
print(f'Removed: {removed_from_list}' )

#print list
print(names)

#print name by index
print(names[0])

if ('Sad') in names:
    print("Sad in the list")

if ('Susy') not in names:
    print('No susi')