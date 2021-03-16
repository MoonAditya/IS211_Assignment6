import unittest
import conversions
import conversions_refactored

msg = "\nPrinting the tempareture conversion from '{}' to '{}'"
class ConversionFunctions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        celsius = 300
        expected = 573.15
        actual = conversions.convertCelsiusToKelvin(celsius)
        self.assertAlmostEqual(expected, actual, places=2, msg=
        msg.format("Celsius", "Kelvin"))

    def test_convertCelsiusToFahrenheit(self):
        celsius = 300
        expected = 572.00
        actual = conversions.convertCelsiusToFahrenheit(celsius)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Celsius", "Fahrenheit"))

    def test_convertKelvinToCelsius(self):
        kelvin = 300
        expected = 26.85
        actual = conversions.convertKelvinToCelsius(kelvin)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Kelvin", "Celsius"))

    def test_convertKelvinToFahrenheit(self):
        kelvin = 300
        expected = 80.33
        actual = conversions.convertKelvinToFahrenheit(kelvin)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Kelvin", "Fahrenheit"))

    def test_convertFahrenheitToKelvin(self):
        fahrenheit = 300
        expected = 422.04
        actual = conversions.convertFahrenheitToKelvin(fahrenheit)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Fahrenheit", "Kelvin"))

    def test_convertFahrenheitToCelsius(self):
        fahrenheit = 300
        expected = 148.89
        actual = conversions.convertFahrenheitToCelsius(fahrenheit)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Fahrenheit", "Celsius"))

    def test_convertCtoK(self):
         fromUnit = 'C'
         toUnit = 'K'
         value = 350
         expected = 623.15
         actual = conversions_refactored.convert(fromUnit, toUnit, value)
         self.assertAlmostEqual(expected, actual, places=2, msg=
         msg.format("Celsius", "Kelvin"))
    
    def test_convertCtoF(self):
        fromUnit = 'C'
        toUnit = 'F'
        value = 350
        expected = 662
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Celsius", "Fahrenheit"))

    def test_convertKtoC(self):
        fromUnit = 'K'
        toUnit = 'C'
        value = 350
        expected = 76.85
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Kelvin", "Celsius"))

    def test_convertKtoF(self):
        fromUnit = 'K'
        toUnit = 'F'
        value = 350
        expected = 170.33
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Kelvin", "Fahrenheit"))

    def test_convertFtoK(self):
        fromUnit = 'F'
        toUnit = 'K'
        value = 350
        expected = 449.82
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Fahrenheit", "Kelvin"))

    def test_convertFtoC(self):
        fromUnit = 'F'
        toUnit = 'C'
        value = 350
        expected = 176.67
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Fahrenheit", "Celsius"))

    def test_convertMilesToMeters(self):
        fromUnit = 'Mi'
        toUnit = 'm'
        value = 5
        expected = 8046.72
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Miles", "Meters"))

    def test_convertMilesToYards(self):
        fromUnit = 'mi'
        toUnit = 'yd'
        value = 5
        expected = 8800
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Miles", "Yards"))

    def test_convertYardsToMiles(self):
        fromUnit = 'yd'
        toUnit = 'mi'
        value = 150
        expected = 0.085
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=3,
        msg=msg.format("Yards", "Miles"))

    def test_convertYardsToMeters(self):
        fromUnit = 'yd'
        toUnit = 'm'
        value = 5
        expected = 4.57
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Yards", "Meters"))

    def test_convertMetersToMiles(self):
        fromUnit = 'M'
        toUnit = 'mi'
        value = 2000
        expected = 1.24
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Meters", "Miles"))

    def test_convertMetersToYards(self):
        fromUnit = 'm'
        toUnit = 'Yd'
        value = 15
        expected = 16.40
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Meters", "Yards"))


        # test meters to meters
    def test_convertMetersToYards(self):
        fromUnit = 'm'
        toUnit = 'm'
        value = 15
        expected = value
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2,
        msg=msg.format("Meters", "Meters"))

        ## test incompatible unit
    def test_convertMetersToYards(self):
        fromUnit = 'm'
        toUnit = 'ft'
        value = 2
        expected = "Incompatible units entered"
        actual = ""
        try:
            conversions_refactored.convert(fromUnit, toUnit, value)
        except Exception:
            actual = "Incompatible units entered"
        self.assertEqual(expected, actual,  msg= "Exception has thrown") # **not a practical test to demonstrate
if __name__ == '__main__':
    unittest.main()
