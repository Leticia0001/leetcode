nums = [-1, 3, 8, -4]
max_len_array = len(nums)
max_sum = float('-inf')  # 如果全部都是負數，初始值不能設為 0

for i in range(max_len_array):
    target = i
    while target < max_len_array:
        total = 0
        for j in range(i, target + 1):
            total += nums[j]
        if total > max_sum:
            max_sum = total
        target += 1

print("最大子陣列總和為:", max_sum)
