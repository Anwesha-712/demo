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

my_dict = dict(zip(days_in_week, temp_of_days))
print(my_dict)

print(my_dict.keys())
print(type(my_dict.keys()))
my_list = my_dict.values()
print(my_list)
print(type(my_list))

#print(my_dict.get("Monday"))

############################################
