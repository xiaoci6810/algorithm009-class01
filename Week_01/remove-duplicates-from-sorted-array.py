class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
           return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i +=1 
                nums[i] = nums[j]
        nums = nums[:i+1]
        return i+1
