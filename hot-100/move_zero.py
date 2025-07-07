class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insertPos=0
        for i in range (len(nums)):
            if nums[i]!=0:
                nums[insertPos],nums[i]=nums[i],nums[insertPos] 
                insertPos=insertPos+1