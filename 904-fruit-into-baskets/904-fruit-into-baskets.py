class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window_start, max_len = 0, 0
        visited_fruits = {}
        
        for window_end in range(len(fruits)):
            fruit = fruits[window_end]
            if not fruit in visited_fruits:
                visited_fruits[fruit] = 0
            visited_fruits[fruit] +=1
                
            while len(visited_fruits) > 2:
                fruit_delete = fruits[window_start]
                visited_fruits[fruit_delete] -=1
                if visited_fruits[fruit_delete] == 0:
                    del visited_fruits[fruit_delete]
                window_start +=1             
            max_len = max(max_len, window_end - window_start + 1  )
            
        return max_len
            
            
        