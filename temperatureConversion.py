print("Is your starting temperature in Celsius or Farenheit?")
degrees = str(input("Please enter Celsius or Farenheit. "))

def convertFTC ( farenheit ):
    "converts Farenheit to Celsius"
    celsius = (farenheit - 32)/1.8
    print("Degrees in Celsius: %3.2f" % (celsius))
def convertCTF ( celsius ):
    "converts Celsius to Farenheit"
    farenheit = celsius * 1.8 +32
    print("Degrees in Farenheit: %3.2f" % (farenheit))

if degrees == "Farenheit":
    farenheit = float(input("Degrees in Farenheit: "))
    convertFTC(farenheit)
if degrees == "Celsius":
    celsius = float(input("Degrees in Celsius: "))
    convertCTF(celsius)