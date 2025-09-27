# with open('weather.txt', 'r') as data_file:
#     data = data_file.readlines()
#     print(data)
# temp_data_dict = {}
# data_file = open('weather.txt', 'r')
# data = data_file.readlines()
# for line in data:
#     day = line.split(':')[0].strip()
#     print(f"Day found : {day}")
#     temp_data_dict[day] = []
#     temps = line.split(':')[1].strip()
#     temps = list(temps.split(','))

#     print(f"Temperatures found : {temps}")
#     print(f"Type of temps : {type(temps)}")
#     temp_data_dict[day] = temps
# print(f"Temperature data dictionary: {temp_data_dict}")
# data_file.close()
###################################

import os
# weather_file = 'C:/Users/ABAL2/Downloads/delete/weather_data.txt'
print(f"Present working directory: {os.getcwd()}")

def display_temp(day):
    
    data_file = open('weather.txt', 'r')
    data = data_file.readlines()
    for line in data:
        if day.lower() == line.split(':')[0].strip().lower():
            print(f"Temperature readings for {day}: {line.split(':')[1].strip()}")
            data_file.close()
            return
    data_file.close()
    print(f"No temperature readings found for {day}")
def delete_temp(day):
    data_file = open('weather.txt', 'r')
    data = data_file.readlines()
    for line in data:
        if day.lower() == line.split(':')[0].strip().lower():
            data.remove(line)
            with open('weather.txt', 'w') as data_file:
                data_file.writelines(data)
            data_file.close()
            return
    data_file.close()
    print(f"No temperature readings found for {day} to delete")

def insert_day_and_temp_reading(day):
    temps = input(f"Enter temperature readings for {day} separated by commas: ")
    new_entry = f"{day}: {temps}\n"
    with open('weather.txt', 'a') as data_file:
        data_file.write(new_entry)
    data_file.close()
    print(f"Inserted temperature readings for {day}")
while True:
    input_day = input("Enter the day you want to display temperature readings for (or 'exit' to quit): ")
    display_temp(input_day)
    input_day = input("Enter the day you want to delete temperature readings for (or 'exit' to quit): ")
    delete_temp(input_day)
    # input_day = input("Enter the day you want to delete (or 'exit' to quit): ")
    # remove_day_from_week(input_day)
    input_day = input("Enter the day you want to insert (or 'exit' to quit): ")
    if len(input_day) > 3:
        insert_day_and_temp_reading(input_day)
