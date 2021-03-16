##1
def convertCelsiusToKelvin(celsius):
    """
    Converts celsius to kelvin
    """
    kelvin = celsius + 273.15
    return kelvin

##2
def convertCelsiusToFahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit 
    """
    fahrenheit = ((celsius*1.8) + 32)
    return fahrenheit

##3
def convertKelvinToCelsius(kelvin):
    """
    Converts celsius to kelvin  
    """
    celsius = (kelvin - 273.15)
    return celsius

##4
def convertKelvinToFahrenheit(kelvin):
    """
    Converts Celsius to Fahrenheit
    """
    fahrenheit = kelvin * 9/5 - 459.67    
    return fahrenheit

##5
def convertFahrenheitToKelvin(fahrenheit):
    """
    Converts Fahrenheit to kelvin
    """
    kelvin =(fahrenheit + 459.67)* 5/9
    return kelvin

##6
def convertFahrenheitToCelsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius
    """
    celsius = (fahrenheit - 32.0) * 5.0 / 9.0
    return celsius