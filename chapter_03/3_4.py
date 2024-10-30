num_list = [12, 34, 12, 5, 67, 95]

max_num = 0
min_num = 10000

for num in num_list:
    # 最大値を取得
    if num > max_num:
        max_num = num

    # 最小値を取得
    if num < min_num:
        min_num = num

print(f"最大の差 : {max_num - min_num}") # 最大の差は90

"""
計算量はO(N)
"""