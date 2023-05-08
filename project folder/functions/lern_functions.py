
def outpoot_greeteng():
    """greeteng message."""
    print('hello')


outpoot_greeteng()

def welcome_message(name, age, locatio='Paris'):
    print(f'Welcome {name}. You {age} and You from {locatio}')
     
welcome_message('Stasy', 16, 'London')
welcome_message(locatio='Kiev', name='Dima', age=33)
welcome_message('Misha', 10) #locatio has defult value 'Paris'



