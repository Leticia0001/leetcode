nums = [100,4,200,1,3,2]


def longest_consecutive(nums):
    if not nums:
        return 0

    num_dict = {num: True for num in nums}  # use jdictionary
    max_length = 0

    for num in nums:
        # check num-1 != False ,this num is the first number 
        if not num_dict.get(num - 1, False):
            current_num = num
            length = 1

            # check the next number. if the number exsit , length+1 & current_num+1
            while num_dict.get(current_num + 1, False):
                current_num += 1
                length += 1

            max_length = max(max_length, length)

    return max_length

print(longest_consecutive(nums))




    