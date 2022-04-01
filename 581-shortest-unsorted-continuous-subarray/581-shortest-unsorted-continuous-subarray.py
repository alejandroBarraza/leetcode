class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr_len = len(nums)
        low, high = 0, arr_len -1
        
        # find smallest unorder
        while (low < arr_len - 1 and nums[low] <= nums[low+1]):
            low+=1
    
        if low == arr_len -1: return 0
                
        while (high > 0 and nums[high] >= nums[high-1]):
            high-=1
        
        # after find low and high. find min and max from sub array
        min_sub = float('inf')
        max_sub = float('-inf')
        
        for index in range(low,high+1):
            min_sub = min(min_sub,nums[index])
            max_sub = max(max_sub,nums[index])
        # check if there's grather on left or smalller on right
        while (low > 0 and nums[low-1] > min_sub):
            low-=1
        while (high < arr_len -1 and nums[high+1] < max_sub):
            high+=1
        
        return high - low + 1
        
        