#min() max()
#Take the temp reading of the day 10 reading
#use input/() to take the reading but use a for loop
# use min/() to find the minimum temp and max to find the maximum temp
temperature=[] #List data structure
for i in range(10):
    temp =int(input("enter the temperature of the day : "))
    temperature.append(temp)
print(f"The Temp reading of the day is {temperature}")

minTemp=min(temperature)
maxTemp=max(temperature)

print(f"The Min Temp of the day is {minTemp} and The Max Temp of the day is {maxTemp}")

