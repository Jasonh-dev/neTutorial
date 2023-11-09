cas_number = '7732-18-5'
rho = 1000
mu = 1
Tm = 273.15
Tb = 373.15
k = 0.58

def convert_to_kelvin(temperature,units):
    if (type(temperature)==float or type(temperature)==int) and (type(units)==str) and len(units)==1:
        units=units.upper()
        if units=="K":
            return temperature
        elif units=="C":
            return temperature + 273.15
        elif units=="F":
            return (temperature - 32) * 5/9 + 273.15
        else:
            return None
    else:
        return None

def is_gas(temperature):
    if (type(temperature)==float or type(temperature)==int):
        if temperature>=Tb:
            return True
        else:
            return False
    else:
        return None

def is_liquid(temperature):
    if (type(temperature)==float or type(temperature)==int):
        if Tm<=temperature<Tb:
            return True
        else:
            return False
    else:
        return None

def is_solid(temperature):
    if (type(temperature)==float or type(temperature)==int):
        if temperature<Tm:
            return True
        else:
            return False
    else:
        return None

if __name__=="__main__":
    units = input("Units please: ")
    if units=="K" or units=="C" or units=="F":
        temperature = input("Temperature please: ")
        temperature_check = str.isdigit(temperature)
        if temperature_check is True:
            temperature_in_kelvin=convert_to_kelvin(float(temperature),units)
            if temperature_in_kelvin is not None:
                if is_gas(temperature_in_kelvin):
                    print("gas")
                elif is_liquid(temperature_in_kelvin):
                    print("liquid")
                elif is_solid(temperature_in_kelvin):
                    print("solid")
                else:
                    print("Invalid input!")
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
