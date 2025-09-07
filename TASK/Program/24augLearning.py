#min() max()
#Take the temp reading of the day 10 reading
#use input/() to take the reading but use a for loop
# use min/() to find the minimum temp and max to find the maximum 
# temperature = 12
# _temperature = 12
# temperature1 = 12
# Temperature1 = 12
# tempe1rature1 = 12
# tempe_rature1 = 12
# #1temperature = 12
# Temp_Mon_Celsius = 10
# Temp_Mon_Fareh_Bangalore_2025 = 10 

# ctrl + / : comments multiple lines

# temp = {}
# temperature = 12
# day = "Monday"
# bulb = False

# print(f"Type of Temperature is : {type(temperature)} and  Value is : {temperature}")
# print(type(day))
# print(type(bulb))
# print(type(temp))


temperature=[] #List data structure
day_list = ["Mon","Tues","Wed","Thru","Fri"]
for Day in day_list:
    for i in range(3):
        temp =input("enter the temperature of the  " + Day + " day 8hr interval " + str(i+1) +": ")
        daily_temps.append(temp)
        temperature[day] = daily_temps

        for day, temps in temperature.items(): 
         print(f"{day} = {temps}")

