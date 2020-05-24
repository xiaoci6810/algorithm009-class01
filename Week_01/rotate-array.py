class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = k % l
        if i == 0:
            return nums
        nums[:i], nums[i:] = nums[-i:], nums[:l-i]
        return nums
            