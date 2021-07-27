#Week 13 Prove - Diogo Rangel Dos Santos
#The Last

#Requirement 1 :Write a function to calculate and return the wind chill 
#based on a given temperature and wind speed.
air_temperature = 0
wind_speed = 0

air_temperature = float(input("What is the temperature? "))
#Requirment 03 Allow the user to enter the temperature in Celsius of Fahrenheit
input_celsius_type = str(input("Fahrenheit or Celsius (F/C)? enter with just F or C: "))
#Requirement 1 :Write a function to calculate and return the wind chill 
#based on a given temperature and wind speed
def calculate_wild_chill(air_temperature,wind_speed):
        wind_chill = 35.74 +\
        (0.6215 * air_temperature) -\
        (35.75*(wind_speed**0.16)) +\
        (0.4275*air_temperature*(wind_speed**0.16)) 
        return wind_chill

#Requirment 02 Write a function to convert from Celsius to Fahrenheit. 
#The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.
def celsius_to_fahrenheit(air_temperature):
        conversion_celsius = air_temperature * (9/5) + 32
        return conversion_celsius
        
def conversion_celsius_fahrenheit(air_temperature):
        conversion_celsius = celsius_to_fahrenheit (air_temperature)
        conversion_celsius_for_fahrenheit = 35.74 +\
        (0.6215 * conversion_celsius) -\
        (35.75*(wind_speed**0.16)) +\
        (0.4275*conversion_celsius*(wind_speed**0.16))
        return conversion_celsius_for_fahrenheit

#Requirment 03 . If they provide it in Celsius, first convert it to Fahrenheit before using the formula above.
def system(air_temperature,wind_speed,input_celsius_type):        
        if input_celsius_type == 'C':
                conversion_celsius = celsius_to_fahrenheit (air_temperature)
                conversion_celsius_for_fahrenheit = conversion_celsius_fahrenheit (air_temperature)
                wind_chill = calculate_wild_chill(air_temperature,wind_speed)
                #Requirement 5 : Display the wind chill value to 2 decimals of precision.
                print(f"At temperature {conversion_celsius}F, and wind speed {wind_speed}mph, the windchill is: {conversion_celsius_for_fahrenheit:.2f}F")
                return conversion_celsius_for_fahrenheit
        elif input_celsius_type == 'F':
                wind_chill = calculate_wild_chill(air_temperature,wind_speed)
                #Requirement 5 : Display the wind chill value to 2 decimals of precision.
                print(f"At temperature {air_temperature}F, and wind speed {wind_speed}mph, the windchill is: {wind_chill:.2f}")
                return wind_chill
        else:
                print("invalid input")
                return print
#Requirement 5:Loop through wind 
#speeds from 5 to 60 miles per hour, incrementing by 5, and calculate and display the wind chill for each of these wind speeds 
for wind_speed in range(5,65,5):
        system(air_temperature,wind_speed,input_celsius_type)
print("Try again to obtain a other temperature. I see you")
        