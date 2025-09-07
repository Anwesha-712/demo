Days_in_Week = ["Monday", "Tuesday", "Wednesday", "Thursday"]

# Initialize a list to hold temperature data for each day of the week
temp_data_week = [[] for list in range(4)] # nested list i.e few lists inside a list

def Insert_Day_and_temp_reading(Day):
    if Day not in Days_in_Week:
        # Days_in_Week.append(Day) # Add new day to the week at the end   
        # temp_data_week.append([]) # Add a new empty list for the new day
        # index = Days_in_Week.index(Day) # Get the index of the new day
        if Day == "Sunday":
            if "Saturday" not in Days_in_Week:
                if "Friday" not in Days_in_Week:
                    Days_in_Week.append("Friday")
                    temp_data_week.append([])
                Days_in_Week.append("Saturday")
                temp_data_week.append([])
            
            Days_in_Week.append("Sunday")
            temp_data_week.append([])
            index = Days_in_Week.index(Day) # Get the index of the new day
        elif Day == "Saturday":
            if "Friday" not in Days_in_Week:
                Days_in_Week.append("Friday")
                temp_data_week.append([])
            Days_in_Week.append("Saturday")
            temp_data_week.append([])
            index = Days_in_Week.index(Day) # Get the index of the new day
        elif Day == "Friday":
            if "Friday" not in Days_in_Week:
                Days_in_Week.append("Friday")
                temp_data_week.append([])
                index = Days_in_Week.index(Day) # Get the index of the new day
        else:
            print("Only Friday, Saturday and Sunday can be added")
            return

        print(f"Enter 3 temperature readings for {Day}:")
        for i in range(3): # Taking 3 readings for the new day
            temp = float(input(f"Reading {i + 1}: ")) # Taking temperature reading
            temp_data_week[index].append(temp) # Append the reading to the new day's list
    else:
        print("Day already exists")
    print(f"Updated temperature data for the week: {temp_data_week}")
    print(f"Updated days in the week: {Days_in_Week}")

def Delete_temp_reading_of_day(Day): # Delete temperature readings for a specific day
    if Day in Days_in_Week:
        index = Days_in_Week.index(Day)
        temp_data_week[index] = []
    else:
        print("Invalid day")
    print(f"Updated temperature data for the week after deletion : {temp_data_week}")

def Update_temp_reading_of_day(Day):
    # overwrite the existing temperature if data is present    
    if Day in Days_in_Week:
        index = Days_in_Week.index(Day) # 0 : Monday 1 : Tuesday ...
        print(f"Enter 3 temperature readings for {Day}:")
        for i in range(3):
            temp = float(input(f"Reading {i + 1}: "))
            # overwrite the existing temperature if data is present
            if len(temp_data_week[index]) > i:
                temp_data_week[index][i] = temp
            else:
                temp_data_week[index].append(temp)
    else:
        print("Invalid day")
    print(f"Updated temperature data for the week: {temp_data_week}")
def main():
    #run below code infinite times
    while True: # Infinite loop while(1)
        Day = input("Enter the day you want to update the temperature readings (e.g., Monday): ")
        Update_temp_reading_of_day(Day)
        Day = input("Delete the temperature readings of which day (e.g., Monday): ")
        Delete_temp_reading_of_day(Day)
        Day = input("Would you like to Insert a new day to the week (e.g., Sunday): ")
        if Day: # If a new day is provided
            Insert_Day_and_temp_reading(Day)
main()