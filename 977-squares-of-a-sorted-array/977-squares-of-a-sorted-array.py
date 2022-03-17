class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        len_arr = len(nums) 
        squares = [ 0 for index in range(len_arr)]
        high_index = len_arr - 1
        
        l, r = 0, len_arr -1
        while l <= r:
            left_squares = nums[l] * nums[l]
            right_squares = nums[r] * nums[r]
            
            if left_squares > right_squares:
                squares[high_index] = left_squares
                l+=1
            else:
                squares[high_index] = right_squares
                r-=1
            high_index -=1
            
        return squares
            
        
        
        
        
         
        