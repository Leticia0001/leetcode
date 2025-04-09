nums = [-1, 3, 8, -4]
max_sum = current_sum = nums[0]

for num in nums[1:]:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print("最大子陣列總和為:", max_sum)

