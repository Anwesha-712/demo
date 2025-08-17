# temperature1= input("Enter the temperature in Celsius for 8am:")
# temperature2 = input("Enter the temperature in Celsius for 12pm:")
# temperature3 = input("Enter the temperature in Celsius for 4pm:")
#ctrl+/ :comment/uncomment
for i in range(4, 7):
    temperature = input(f"Enter the temperature in Celsius for {8 + (i - 1) * 4}am: ")
    if i == 1:
        temperature1 = temperature
    elif i == 2:
        temperature2 = temperature
    else:
        temperature3 = temperature
average_temperature = (float(temperature1) + float(temperature2) + float(temperature3)) / 3
#print("The average temperature for the day is:", average_temperature, "Celsius")
print(f'The average temperature for the day is: {average_temperature} Celsius')

