class Car:
    ''''Car objects'''
    #miles = 0  #-- we no longer need thos var, becouse it set by init meethod

#constructor (in time create variables, without declaration)
    def __init__(self, colour, make, model, miles=0):
        '''set initial details'''
        self.colour = colour
        self.make = make
        self.model = model
        self.miles = miles


    def add_miles(self, miles):
        """increase miles by number"""
        self.miles += miles

    def display_miles(self):
        #print( f"Current miles of {self.model} is : {self.miles}")
        print(
            f'{self.make}, {self.model}, ({self.colour}) '
            f'has driven {self.miles} miles.'
        )



astra = Car('Red', 'Vasuall', 'Astra', 120)
astra.display_miles()
astra.add_miles(48)
astra.display_miles()

prius = Car("Grey", "Toyota", "Prius", 240)
prius.add_miles(270)
prius.display_miles()
astra.display_miles()