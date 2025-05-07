list_a = [1, 323, 243 ,23 ,3323 ,125, 12, 124, 22, 23, 99, 23]
target_num = 23

count = 0
for num in list_a:
    if num == target_num:
        count += 1

print(f"count：{count}") # countは３

"""
計算量はO(N)
"""