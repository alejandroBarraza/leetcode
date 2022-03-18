class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        len_arr = len(nums)
        closes_num = nums[0] + nums[1] + nums[len_arr -1]
        for index in range(len_arr):
            l,r = index + 1, len_arr -1
            while l < r:
                summ = nums[index] + nums[l] + nums[r]  
                if summ == target:
                    return summ
                if abs(summ - target) < abs(closes_num - target):
                    closes_num = summ
                
                if summ > target:
                    r-=1
                else:
                    l+=1
        return closes_num
                
                
                
                    

            
        
        
        
        
        