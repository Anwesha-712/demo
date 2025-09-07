Days_in_Week = ["Monday", "Tuesday", "Wednesday", "Thursday"]
temp_data_week = [[11, 12, 13], [14, 12, 16], [17, 18, 30], [25, 18, 27]]

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
i = 0
while i<4:
    print(temp_data_week[i]) # print [11, 12, 13] [14, 12, 16]    
    i = i +1
print("End of while  loop")