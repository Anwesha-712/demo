
def MonToFridayTempReading():
    temperature=[] #List data structure
    day_list = ["Mon","Tues","Wed","Thru","Fri"]
    for Day in day_list:
        for i in range(3):
            temp =input("enter the temperature of the  " + Day + "day 8hr interval : ")
            temperature.append(temp)
    print(temperature)

 

# Tak  the temp for mon -friday again and dispay
print("Hello")
MonToFridayTempReading()
# find tha average temp value for week 

# logic to find out the average temp for each day 

### line 13 - line 50
MonToFridayTempReading()