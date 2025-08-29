# Time Complexity: O(n)
# - n is the length of nums.
# - Binary search takes O(log n), but inserting into a Python list
#   is O(n) in the worst case (due to shifting elements).
#
# Space Complexity: O(1)
# - Only a few extra variables are used.
#
# Idea:
# - Use binary search to locate the correct position for target.
# - If target already exists, return immediately.
# - Otherwise, after the loop ends, low points to the insertion index.
# - Insert target at low using arr.insert(low, target).
# - This ensures the array remains sorted.

def binary_search_insert(arr,target):
    #定義低位置與高位置的序列，預設low是第0個值，預設high是最後一個值(由於從0開始扣除1)
    low,high=0,len(arr)-1
    
    #只要 low <= high，表示搜尋區間還"有效"，裡面還有元素要檢查：當low>high時，則表示搜尋區域結束。
    while low<=high:
        mid= (low+high)//2 #優先定義切中間的值，取原本預設的整除2，不會有小數點
        
    # 定義在arr串列中mid內的值是否與target相同，若是相同則回傳mid的位置。
    # 若是比target的值小，調整原本low的位置比原本的mid的值往右邊移一格。
    # 若是比target的值大，調整原本high的位置比原本的mid的值往左邊移一格。
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    
    #若是超出區域則新增於target值在arr這個串列中，在low 前插入一個元素 target
    arr.insert(low,target)

    #回傳目前low的值
    return low

arr = [5, 12, 17, 23, 38, 45, 59, 72, 88]

print(binary_search_insert(arr, 2))   # 插在最前面 → index 0
print(binary_search_insert(arr, 90))   # 插在最前面 → index 10
print(arr)
