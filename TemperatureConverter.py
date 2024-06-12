class TemperatureConverter:
    @staticmethod
    def celsiusToFahrenheit(C):
        return C * 9/5 + 32

    @staticmethod
    def fahrenheitToCelsius(F):
        return (F - 32) * 5/9

C = 67
F = 100

celsiusToFahrenheit = TemperatureConverter.celsiusToFahrenheit(C)
print(celsiusToFahrenheit)
fahrenheitToCelsius = TemperatureConverter.fahrenheitToCelsius(F)
print(fahrenheitToCelsius)