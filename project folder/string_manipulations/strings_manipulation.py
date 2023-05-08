name = "Dima"
age = 33

#set ordering of using arguments
message = 'Hello {1} ({0})'.format(name, age)

#named key-word argument
message = 'Hello {name} ({age})'.format(name=name, age=age)


print(message)