"""
Unit converter from meter to imperial units
"""

print("Welcome to BTH air's unit converter")

# m is meter units
height_m = input("Distance from sea level(m)?: \n")
speed_m = input("How fast is the plane going(kmh): \n")
temp_m = input("What's the outside temperature(°C): \n")

# i is imperial units
height_i = float(height_m) * 3.28084
speed_i = float(speed_m) * 0.62137
temp_i = float(temp_m) * (9/5) + 32

print ("You are " + str(round(height_i,2)) + " feet over sea level")
print ("You are going " + str(round(speed_i,2)) + " mph")
print ("The temperature outside is " + str(round(temp_i,2)) + "°F")
