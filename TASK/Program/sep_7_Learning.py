# Days_in_Week = ["Monday", "Tuesday", "Wednesday", "Thursday"]
# temp_data_week = [[11, 12, 13], [14, 12, 16], [17, 18, 30], [25, 18, 27]]

# for loop to compare the date between monday and tuesday
# for i in range(3): # 3 times execution
#     # if temp_data_week[2][i] > temp_data_week[3][i]:
#     #     print(f"{Days_in_Week[2]} is warmer : {Days_in_Week[2]}'s reading {temp_data_week[2][i]} is higher than {Days_in_Week[3]}'s reading {temp_data_week[3][i]}")
#     # elif temp_data_week[2][i] < temp_data_week[3][i]:
#     #     print(f"{Days_in_Week[3]} is warmer : {Days_in_Week[3]}'s reading {temp_data_week[3][i]} is higher than {Days_in_Week[2]}'s reading {temp_data_week[2][i]}")
#     # else:
#     #     print(f"{Days_in_Week[2]}'s reading {temp_data_week[2][i]} is equal to {Days_in_Week[3]}'s reading {temp_data_week[3][i]}")
#     if temp_data_week[2][i] == temp_data_week[3][i]:
#         print(f"{Days_in_Week[2]}'s reading {temp_data_week[2][i]} is equal to {Days_in_Week[3]}'s reading {temp_data_week[3][i]}")

# -------------- while loop
# i = 0
# num_list = [1,2,3,4,10,20,50,60,70]
# while i< len(num_list):
#     #search for the element i.e 50
#     if num_list[i] == 50:
#         print("the index of 50 is: ", i) # index :6
#         break

#     else:
#          print("50 is not present in the list")
        
#     print("While loop is runnung with iteration: ", i) 
#     i = i +1
    
# print("End of while  loop")
# i = 0
# num_list = [1,2,3,4,10,20,50,60,70]
# while i < len(num_list):
#     print(f"Value at the index {i} is: ",num_list[i])
    
#     if num_list[i] == 50 :
#         print("value found")
#         i = i +1 
#         continue
#     i = i +1

# Days_in_Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Temp_list = [[15,16,17], [15,10,33], [15,16,17], [15,10,33], [15,16,17], [15,10,33], [20,21,22]]

# i = 0
# while i < len(Days_in_Week):
#     if Days_in_Week[i] in ["Saturday", "Sunday"]:
#         i += 1
#         continue   
    
#     print(f"{Days_in_Week[i]} = {Temp_list[i]}")
    
#     if Days_in_Week[i] == "Friday":
#         break   
#     i += 1

Days_in_Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
Temp_list = [[15,16,17], [15,33,10], [15,16,17], [33,15,10], [15,16,17], [15,10,33], [20,21,22]]

i = 0
while i < 5 :
# if (index_no > 30 for t in Temp_list[i]):
#     break
# print(f"{Days_in_Week[i]} = {Temp_list[i]}")
#     i += 1
    temp_reading = Temp_list[i]
    print(f"Temp of {Days_in_Week[i]} is {temp_reading}")
    for readings in temp_reading:
        # print(f"Reading of {Days_in_Week[i]} : {readings}")
        if readings > 30: # this if and break used to terminate the for loop
            break
    if readings >30: # this if and break userd to terminate the while loop
        break
    i = i +1

print("End of loop")