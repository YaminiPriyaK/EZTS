""" Temperature Converter
Objective: Create a class to convert temperatures between Celsius and Fahrenheit.

Instructions:
Define a class TemperatureConverter with static methods for converting temperatures.
Implement a method to convert from Celsius to Fahrenheit and another method to convert from Fahrenheit to Celsius.
Demonstrate using the methods to convert temperatures in both directions.

Hint: Use the formulas F = C * 9/5 + 32 for Celsius to Fahrenheit conversion and C = (F - 32) * 5/9 for Fahrenheit to Celsius conversion."""


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
