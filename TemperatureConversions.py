def main():
    controlLoop()

def convertToKelvin(temp):
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Kelvin
    newTemp = ((temp - 32) * (5/9) + 273.15)
    #return Kelvin
    return newTemp

def convertToCentigrade(temp):
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Centigrade
    newTemp = (temp - 32) * (5/9)
    #return Centigrade
    return newTemp

def doConversion():
    #getFahrenheit(), get back Fahrenheit
    fTemp = getFahrenheit()
    #convertToKelvin(), send Fahrenheit get back Kelvin
    kTemp = convertToKelvin(fTemp)
    #ConvertToCentigrade, sends Fahrenheit gets back Centigrade
    cTemp = convertToCentigrade(fTemp)
    #prints for example: 'Fahrenheit: xx Kelvin xx Centigrade: xx'
    print(f"Farenheit: {fTemp} Kelvin: {kTemp} Centigrade: {cTemp}")

def repeat():
    #Inputs How many conversions would you like to do this time?
    repeatAmount = int(input("How many conversions would you like to do this time? "))
    #for x in range how many
    for x in range(repeatAmount):
        #doConversion()
        doConversion()

def controlLoop():
    #Inputs 'Do you want to do some conversions(Yes or No)?'
    inputYorN = input("Do you want to do some conversions(Yes or No)? ")
    #if 'yes' repeat()
    if inputYorN == "yes":
        repeat()

def getFahrenheit():
    #Inputs 'Enter Fahrenheit temperature (must be -50 to 130):'
    fTemp = int(input("Enter Fahrenheit temperature (must be -50 to 130): "))
    #(validation loop)'Please re-enter'
    if -50.0 <= fTemp <= 130.0:
        return fTemp
    else:
        print('Invalid temp')
    #return Fahrenheit
    return fTemp

# Call the main function.
if __name__ == '__main__':
    main()
