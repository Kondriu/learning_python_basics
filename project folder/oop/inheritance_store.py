class User():
    '''User class'''

    def __init__(self, name, password):
        '''initial setup'''
        self._name = name
        self._password = password
        self._logged_in = False

    def login(self, password):
        '''check password and user login'''
        if password == self._password:
            self._logged_in = True
        else:
            print(f'Incorrect password.')

    def show_status(self):
        '''print status of user'''
        if self._logged_in:
            print(f'{self._name} is logged in')
        else:
            print(f"{self._name} You is not loggen in!")
    
customer = User(
    name="Bruce",
    password="Superpassword213"
)

customer.login('sdfsdfsdfsfs')
customer.show_status()
customer.login("Superpassword213")
customer.show_status()


class Admin(User):
    '''admin role'''

    def __init__(self, name, password, staff_id):
        super().__init__(name, password)
        self._staff_id = staff_id

    def add_product(self, name):
        '''add new product to invetary'''
        if self._logged_in:
            print(f'{self._name} ({self._staff_id}) added to inventory product {name}.')
        else:
            print('login to add product')


staff = Admin(
    name="Mark",
    password="Passw123",
    staff_id=2134
)

staff.add_product("cofee")
staff.login("Passw123")
staff.add_product("cofee")

