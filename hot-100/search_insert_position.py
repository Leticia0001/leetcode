def binary_search_insert(arr,target):
    low,high=0,len(arr)-1
    
    while low<=high:
        mid= (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    arr.insert(low,target)

    return low

arr = [5, 12, 17, 23, 38, 45, 59, 72, 88]
print(binary_search_insert(arr, 2))   # 插在最前面 → index 0
print(arr)
