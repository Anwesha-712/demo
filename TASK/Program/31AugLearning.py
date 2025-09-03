# Take temperature readings for each day and print in one line

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# days = ["Monday", "Tuesday"]
# temp_data_week = []

# for day in days:
#     readings = []
#     print(f"Enter 3 temperature readings for {day}:")
#     for i in range(3):
#         temp = float(input(f"  Reading {i+1}: "))
#         readings.append(temp)
#     temp_data_week.append(readings)

# # Print all days and their readings in one line
# print(" ".join([f"{day} = {temps}" 
# for day, temps in zip(days, temp_data_week)]))


days = ["Monday", "Tuesday"]
temp_data_week = []

for day in days:    
    print(f"Enter 3 temperature readings for {day}:")
    readings = []
    for i in range(3):
        temp = float(input(f"Reading {i+1}: "))
        readings.append(temp)
    temp_data_week.append(readings)


print(temp_data_week) # nested list
# print the day data in simple way
for i in range(len(days)):
    print(days[i], "=", temp_data_week[i]) # days[0] = Monday temp_data_week[0] = [12,13,14]

# step -1 : Take the input (day) from user ex: monday or tuesday
# step -2: Identify the  index value of the nested list based on the day
# step  3: update the temp of that day 


day = input("Enter the day which you want to update : ")
print(f"You have entered {day}")

reading = int(input("Enter the Reading which you want to update : "))
print(f"You have entered the reading {reading}")

if day == "Monday": #comparision operator >= or <= or == or != or 
    index = 0 
elif day == "Tuesday":
    index = 1
elif day == "Wednesday":
    index = 2
elif day == "Thursday":
    index =3    
else:
    print("Invalid day")
    exit()  

Reading_Temp = float(input(f"Enter the reading {reading} of {day}:"))
# readings = []
# for i in range(3):
#     temp = float(input(f"{day} Reading {i+1}: "))
#     readings.append(temp)
# temp_data_week[index] = readings

temp_data_week[index][reading] = Reading_Temp
# temp_data_week.insert()

print(f"temp of the week :{temp_data_week}")


Reading_Temp_Remove = float(input(f"Enter the reading to be removed : "))
temp_data_week[index].remove(Reading_Temp_Remove)

print(f"temp of the week after removing the data :{temp_data_week}")



