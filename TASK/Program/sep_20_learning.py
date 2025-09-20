days_in_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp_of_days = [[20, 21, 22], [14, 15, 16], [60, 62, 64], [75, 78, 80], [30, 32, 34], [40, 42, 44], [50, 52, 54]]

# Create a dictionary by zipping the two lists together
my_dict = dict(zip(days_in_week, temp_of_days))
print("Days and their temperature readings:", my_dict)

for day, temps in my_dict.items():
    print(f"Day: {day}")
    for i, temp in enumerate(temps):
        print(f"  Reading {i + 1}: {temp}")

###########################################

days_in_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp_of_days = [[20, 21, 22], [14, 15, 16], [60, 62, 64], [75, 78, 80], [30, 32, 34], [40, 42, 44], [50, 52, 54]]

# rewrite below print statutment to keep a line break after each print line
print(list(zip(days_in_week, temp_of_days)))

#my_dict = dict(a=1, b=2) 
my_dict = dict(zip(days_in_week, temp_of_days))
print(my_dict)

print(my_dict.keys())
print(type(my_dict.keys()))
my_list = my_dict.values()
print(my_list)
print(type(my_list))

# keys = my_dict.keys()            # iterable view
# vals = my_dict.values() # iterable view
# pairs = my_dict.items() # iterable view

#print(my_dict.get("Monday"))
#print(my_dict["Monday"])
# my_dict.update({"Monday": 4, "Tuesday": 11}) #update multiple dictionary elements
# my_dict["Sunday"] = [25, 26]
# del my_dict["Sunday"]
# print(my_dict.pop("Sunday", None)) # remove and return value
# my_dict.popitem() # remove & return an arbitrary pair (Python 3.7+: last inserted)
# my_dict.clear()

############################################
days_in_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp_of_days = [[20, 21, 22], [14, 15, 16], [60, 62, 64], [75, 78, 80], [30, 32, 34], [40, 42, 44], [50, 52, 54]]
my_dict = dict(zip(days_in_week, temp_of_days))

def display_temp(day):
    day = day.title() # Capitalize the first letter of the day
    if day in my_dict:
        #print(f"Temperature readings for {day}: {my_dict[day]}")
        print(f"Temperature readings for {day}: {my_dict.get(day)}")

    else:
        print("Invalid day")

def delete_temp(day):
    day = day.title() # Capitalize the first letter of the day
    if day in my_dict:
        my_dict[day] = [] # Clear the temperature readings for the specified day
        print(f"Temperature readings for {day} have been deleted.")
        print(f"Updated temperature readings for week : {my_dict}")
    else:
        print("Invalid day")

def remove_day_from_week(day):
    day = day.title() # Capitalize the first letter of the day
    if day in my_dict:
        del my_dict[day] # Remove the specified day from the dictionary
        print(f"{day} has been removed from the week.")
        print(f"Updated days and their temperature readings for week : {my_dict}")
    else:
        print("Invalid day")

def insert_day_and_temp_reading(day):
    day = day.title() # Capitalize the first letter of the day
    if day not in my_dict:
        my_dict[day] = [] # Add the new day with an empty list for temperature readings
        print(f"New day {day} has been added to the week.")
        print(f"New week days and their temperature readings : {my_dict}")
    else:
        print("Day already exists")
        return
    
while True:
    input_day = input("Enter the day you want to display temperature readings for (or 'exit' to quit): ")
    display_temp(input_day)
    input_day = input("Enter the day you want to delete temperature readings for (or 'exit' to quit): ")
    delete_temp(input_day)
    input_day = input("Enter the day you want to delete (or 'exit' to quit): ")
    remove_day_from_week(input_day)
    input_day = input("Enter the day you want to insert (or 'exit' to quit): ")
    insert_day_and_temp_reading(input_day)

############################
