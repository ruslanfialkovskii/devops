print("What temperature in (Fahrenheit) would you like","converted to Celcius?",sep='\n')
temperature_fahrenheit = input()
temperature_celcius = (int(temperature_fahrenheit) - 32) * 5/9
print(str(temperature_fahrenheit), "F is", str(round(temperature_celcius,2)), "C")