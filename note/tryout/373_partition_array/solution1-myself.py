class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        if nums is []:
            return None
        length = len(nums)
        index1 = 0
        index2 = length - 1
        while (index1 < index2):
            if nums[index1]%2 == 0 and nums[index2]%2 != 0:
                temp = nums[index1]
                nums[index1] = nums[index2]
                nums[index2] = temp
                index1 += 1 
                index2 -= 1
            if nums[index1]%2 != 0:
                index1 += 1
            if nums[index2]%2 == 0:
                index2 -= 1

