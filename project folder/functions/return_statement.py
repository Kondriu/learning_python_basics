def create_and_return_greeteng(name, age, location):
    """create and return message"""
    message = f'Welcome {name}. You {age} and you from {location}!'
    return message

greeteng = create_and_return_greeteng("Dima", 43, "Ukraine")
print(greeteng)