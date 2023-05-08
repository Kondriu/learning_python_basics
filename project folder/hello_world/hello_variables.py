name = 'Mark W'
age = 31
isRegistred = True


print(name)
print(age)
print(isRegistred)


message1 = 'Hello %s (%i)' % (name, age) #old
message2 = 'Hello {} ({})'.format(name, age) #new
message3 = f'Hello {name} ({age})' # newest format

print('m1: ' + message1)
print('m2: ' + message2)
print('m3: ' + message3)


