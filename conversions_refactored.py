import conversions

class ConversionNotPossibleException(Exception):
  """ raising custom ConversionNotPossible for the invalid unit conversion function  """
  pass

def convert(fromUnit, toUnit, value):
    """
    Convert
    """
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    if fromUnit == toUnit:
        return value
    
    elif fromUnit == "c" and toUnit == "k":
        return value + 273.15
    elif fromUnit == "c" and toUnit == "f":
        return ((value * 1.8) + 32)   
    
    elif fromUnit == "k" and toUnit == "c":
        return (value - 273.15)
    elif fromUnit == "k" and toUnit == "f":
        return (value * 9 / 5 - 459.67)

    elif fromUnit == "f" and toUnit == "k":
        return ((value + 459.67) * 5 / 9)
    elif fromUnit == "f" and toUnit == "c":
        return ((value - 32.0) * 5.0 / 9.0)

    elif fromUnit == "mi" and toUnit == "m":
         return (value * 1609.344)
    elif fromUnit == "mi" and toUnit == "yd":
         return (value * 1760)

    elif fromUnit == "m" and toUnit == "mi":
         return (value * 0.000621)
    elif fromUnit == "m" and toUnit == "yd":
         return (value * 1.093613)

    elif fromUnit == "yd" and toUnit == "m":
         return (value * 0.9144)
    elif fromUnit == "yd" and toUnit == "mi":
         return (value / 1760)
    elif fromUnit == "yd" and toUnit == "mi":
         return (value / 1760)

    else:
        raise ConversionNotPossibleException("Incompatible units entered")


