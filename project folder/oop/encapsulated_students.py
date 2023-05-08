class Students:
    '''represent students'''

    def __init__(self, name):
        self._name = name
        self._results = {}

    def _calc_predicted_results(self):
        '''calculate predict resuls'''
        results = self._results.values()
        return sum(results)/len(results)
    
    def add_results(self, year, result):
        '''add results'''
        #self._years.append(year)
        #self._results.append(result)
        self._results[year] = result

    def display_predicted_results(self):
        '''display predicted results'''
        result = self._calc_predicted_results()
        print(f"Student {self._name} is predicted: {result}")

s = Students('One')
s.add_results(2020, 98)
s.add_results(2021, 88)
s.add_results(2022, 85)
s.display_predicted_results()
