class Temperature:
    def __init__(self, value):
        self.value = value

    def convertFahrenheit(self):
        f = self.value * 9/5 + 32
        return f'{f} degree F'

    def convertCelsius(self):
        c = ( self.value - 32 ) * 5/9
        c = round(c, 2)
        return f'{c} degree C'


# C to F
t = Temperature(30)
print(t.convertFahrenheit())

# F to C
t = Temperature(40)
print(t.convertCelsius())

