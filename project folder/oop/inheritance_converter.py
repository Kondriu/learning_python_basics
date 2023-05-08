class TempMixing:
    '''convert metrics to empirials'''
    
    def c_to_f(self, c):
        return(c * 1.8) + 32
    
    def f_to_c(self, f):
        return (f - 32) / 1.8


class DistanceMixixng:
    '''convert metrics to empirials'''

    def m_to_km(self, miles):
        return miles * 1.60934
    
    def km_to_m(self, km):
        return km * 0.6213712
    

class DiditalStorageMixing:
    '''' converts GB to MG '''

    def gb_to_mb(self, gb):
        return gb * 1000
    
    def mb_to_gb(self, mb):
        return mb / 1000
    
class Wheather (TempMixing, DistanceMixixng):

    def __init__(self, celsius, kmph):
        self._celsius = celsius
        self._kmph = kmph

    def display(self, metric=True):
        '''display weather values'''
        if metric:
            temp = self._celsius
            wind = self._kmph
        else:
            temp = self.c_to_f(self._celsius)
            wind = self.km_to_m(self._kmph)
        
        print(f'Temp is {temp}, Wind speed is: {wind}.')
        print("End of wheather")



lomdon = Wheather(12, 7)
lomdon.display(True)
lomdon.display(False)


class HardDrive(TempMixing, DiditalStorageMixing):

    def __init__(self, space, celsius):
        self._space = space
        self._celsius = celsius
    
    def status(self, metric = True):
        if metric:
            temp = self._celsius
        else: 
            temp = self.c_to_f(self._celsius)

        space = self.mb_to_gb(self._space)
        print(f"Space:  {space}Gb, Temp: {temp}." )
        print("end of HDD status...")


hd = HardDrive(230000, 46)
hd.status()
hd.status(metric=False)

 
        