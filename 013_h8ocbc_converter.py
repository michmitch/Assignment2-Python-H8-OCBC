def celc_and_kelv(temp, to):
	'''
	This function is for converting celcius to kelvin or otherwise
	Input: temp = temperature to convert, to = convert to celcius or kelvin (use 'c' or 'k')
	Output: converted temperature
	'''
    if(to.lower() == 'c'):
        print(f'{temp} K = {temp - 273} C')
        return temp - 273
    else:
        print(f'{temp} C = {temp + 273} K')
        return temp + 273

def to_fahrenheit(temp, inp):
	'''
	This function is for converting celcius or kelvin to fahrenheit
	Input: temp = temperature to convert, inp = from celcius or kelvin (use 'c' or 'k')
	Output: converted fahrenheit temperature
	'''
    if(inp == 'k'):
        temp2 = celc_and_kelv(temp, 'c')
        temp2 = temp2 * 9/5 + 32
        print(f'{temp} K = {temp2} F')
        return temp2
    else:
        temp2 = temp * 9/5 + 32
        print(f'{temp} C = {temp2} F')
        return temp2

def from_fahrenheit(temp, outp):
	'''
	This function is for converting fahrenheit to celcius or kelvin
	Input: temp = temperature to convert, outp = convert to celcius or kelvin (use 'c' or 'k')
	Output: converted fahrenheit temperature
	'''
    if(outp == 'k'):
        temp2 = (temp - 32) * 5/9
        temp2 = celc_and_kelv(temp2, 'k')
        print(f'{temp} F = {temp2} K')
        return temp2
    else:
        temp2 = (temp - 32) * 5/9
        print(f'{temp} F = {temp2} C')
        return temp2

celc_and_kelv(1, 'k')
celc_and_kelv(273, 'c')

to_fahrenheit(64, 'c')
to_fahrenheit(300, 'k')

from_fahrenheit(45, 'k')
