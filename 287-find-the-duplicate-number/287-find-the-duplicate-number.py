class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        
        # find the duplicated
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # slow has the matching value
        
        # the diference between the beginning , to beginning of the cicle
        # same as from slow,fast match and the beginnig of the cicle
        # so, set a new pointer at the beginning and will match with the slow pointer
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
        
            
        