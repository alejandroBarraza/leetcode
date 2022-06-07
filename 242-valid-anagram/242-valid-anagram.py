class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        # fill in tDic with 
        tDic  = {}
        for char in t:
            if char not in tDic:
                tDic[char] = 1
            else:
                tDic[char] +=1
                
        # check every word of s if tDic
        # if one word is not there
        # return false
        
        for char2 in s:
            if char2 in tDic:
                tDic[char2] -=1
                if tDic[char2] == 0:
                    del tDic[char2]
            else:
                return False
        if len(tDic) == 0: 
            return True
        else:
            return False
                
            
                
           
                
        
                
        
            
            
            
        