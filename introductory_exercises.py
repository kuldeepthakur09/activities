Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
Factor:  Calculate temperature that a person feels because of the wind (Python3)
Note: Naming Convention Files: Crate files based on the purpose of the exercise eg: If calculating factor then use factor.py  
'''
'''

#Arithmetic
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)


#Conversion
num = float(input("Enter a number: "))
unit = input("Enter the unit of measurement for the number: ")
target_unit = input("Enter the unit of measurement to convert to: ")


if unit == "feet":
    factor = 0.3048
elif unit == "miles":
    factor = 1609.34
elif unit == "inches":
    factor = 0.0254


converted_num = num * factor

print(num, unit, "is equal to", converted_num, target_unit)



#Earthquake Impact
magnitude = float(input("Enter the magnitude of the earthquake: "))

impact = 10**(1.5*magnitude - 5.75)

print("The potential impact of the earthquake is", impact)



#Factor
import math

wind_speed = float(input("Enter the wind speed in miles per hour: "))
temperature = float(input("Enter the temperature in degrees Fahrenheit: "))

factor = 35.74 + 0.6215*temperature - 35.75*math.pow(wind_speed, 0.16) + 0.4275*temperature*math.pow(wind_speed, 0.16)

print("The wind chill factor is", factor, "degrees Fahrenheit.")