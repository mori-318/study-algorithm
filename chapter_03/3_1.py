list_a = [1, 23, 542, 656, 88, 4, 3, 6, 4, 33, 32, 23] #indexは0~11
target_num = 23

max_index = 0
for index in range(len(list_a)):
    if list_a[index] == target_num:
        max_index = index

print(f"max_index : {max_index}") # 答えは11

"""
計算量O(N)
"""