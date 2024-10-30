num_list = [23, 12, 44, 23, 12, 44, 55, 77, 65, 92]

lower_1 = 10000
lower_2 = 10000

for num in num_list:
    if num < lower_1:
        lower_1 = num
    if (num < lower_2) and (num > lower_1):
        lower_2 = num

print(f"lower_2 : {lower_2}") # lower_2は23

"""
計算量はO(N)
"""