# This method include the function pointer.
# you could replace the method to other problem

class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def __init__(self):
        self.funcIndex = {'check_odd': self.check_odd}        

    def partitionArray(self, nums):
        # write your code here
        if nums is []:
            return None
        length = len(nums)
        index1 = 0
        index2 = length - 1
        while (index1 < index2):
            if self.funcIndex['check_odd'](nums[index1]) is False and self.funcIndex['check_odd'](nums[index2]):
                temp = nums[index1]
                nums[index1] = nums[index2]
                nums[index2] = temp
                index1 += 1 
                index2 -= 1
            if self.funcIndex['check_odd'](nums[index1]):
                index1 += 1
            if self.funcIndex['check_odd'](nums[index2]) is False:
                index2 -= 1

    def check_odd(self, num):
        if num%2 != 0:
            return True
        else:
            return False

