class Solution:
    
    def sumOfSquare(self, number: int) -> int:
        out = 0
        while number:
            digit = number % 10
            digit = digit ** 2
            out += digit
            number = number // 10
        return out
        
    
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquare(n)
            if n == 1:
                return True
        return False
            
            
            
        
        
        