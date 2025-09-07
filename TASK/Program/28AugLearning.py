def MonToFridayTempReading():
    temperature=[] #List data structure
    day_list = ["Mon","Tues","Wed","Thru","Fri"]
    # day_list = ["Mon","Tues"]
    temperature_data_monday = []
    temperature_data_tuesday = []
    temperature_data_wed = []
    temperature_data_thru = []  
    temperature_data_fri = []
    for Day in day_list:
        for i in range(3):
            temp =input("enter the temperature of the  " + Day + "day 8hr interval : ")
            if Day == "Mon":
                temperature_data_monday.append(temp)
            elif Day == "Tues":
                temperature_data_tuesday.append(temp)
            elif Day == "Wed":
                temperature_data_wed.append(temp)   
            elif Day == "Thru":
                temperature_data_thru.append(temp)
            elif Day == "Fri":
                temperature_data_fri.append(temp)   
    
    print("Monday = ", temperature_data_monday)
    print("Tuesday = ", temperature_data_tuesday)
    print("Wednesday = ", temperature_data_wed)
    print("Thursday = ", temperature_data_thru) 
    print("Friday = ", temperature_data_fri)


 

# Tak  the temp for mon -friday again and dispay
 
print("Hello")
# MonToFridayTempReading()

# find tha average temp value for week 

# logic to find out the average temp for each day 

### line 13 - line 50
# MonToFridayTempReading()

# -----------------------------

# mylist = []
# temp_mon = [11,12,13]
# temp_tue = [11,16,13]
# temp_wed = [11,14,13]

# mylist.append(temp_mon)
# mylist.append(temp_tue)
# mylist.append(temp_wed)




# print(type(mylist))

# print(mylist)
# print("Monday =", mylist[0])
# print("Tuesday =", mylist[1])
#mylist = [[11,12,13],[11,16,13],[11,14,13]] # list of lists

#---------------------------

#day_list = ["Mon","Tues", "Wed"]
# temp_data_week = [] #list of lists
# temperature_data_day = []

# for day in day_list:
#     for temp in range(3):
#         temp =input("enter the temperature of the  " + day + "day 8hr interval : ")
#         temperature_data_day.append(temp)   
#     temp_data_week.append(temperature_data_day)
#     #clear the day list to hold the next data from beginning
#     temperature_data_day = []

#print(temp_data_week)

# Monday = [12,13,14] Tuesday = [14, 15, 16]
# use for loop and only one print statement


days = ["Monday", "Tuesday"]
temp_data_week = []

for day in days:    
    print(f"Enter 3 temperature readings for {day}:")
    readings = []
    for i in range(3):
        temp = float(input(f"Reading {i+1}: "))
        readings.append(temp)
    temp_data_week.append(readings)


print(temp_data_week)
# print the day data in simple way
for i in range(len(days)):
    print(days[i], "=", temp_data_week[i]) # days[0] = Monday temp_data_week[0] = [12,13,14]