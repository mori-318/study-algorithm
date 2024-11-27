a_list = [8, 12, 16]

count = 10000

# 配列の要素がすべて偶数か調べる
is_all_even = True
for a in a_list:
    if a%2 != 0:
        is_all_even = False

if is_all_even: # 配列の要素がすべて偶数の場合
    for a in a_list:
        temp_count = 0
        while(a%2 == 0):
            a = a / 2
            temp_count += 1
        if temp_count < count:
            count = temp_count

    print(f"最小は{count}") # 答えは２（要素１２の場合）