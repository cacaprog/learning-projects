# output numbers from 0 to 10
for i in range(11):
    print(i)

# resolve the classic rain problem
# Write a program that will read the amount of rainfall for each day. 
# A negative value of rainfall should be rejected since this is invalid and inadmissible. 
# The program should print out the number of valid recorded days, 
# the number of rainy days, the rainfall over the period, 
# and the maximum amount of rain that fell on any one day. 
# Use a sentinel value of 9999 to terminate the program.
# Path: copilot_rain.py
rain = 0
days = 0
rainy_days = 0
max_rain = 0
while rain != 9999:
    rain = int(input("Enter the amount of rainfall: "))
    if rain < 0:
        print("Invalid input")
    elif rain == 9999:
        print("End of program")
    else:
        days += 1
        if rain > 0:
            rainy_days += 1
        if rain > max_rain:
            max_rain = rain
print("Number of valid recorded days: ", days)
print("Number of rainy days: ", rainy_days)
print("Rainfall over the period: ", rain)
print("Maximum amount of rain that fell on any one day: ", max_rain)


"""
Outup hello world
"""
print("Hello World")





