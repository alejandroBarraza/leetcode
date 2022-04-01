class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        p_word1, p_word2 = 0,0
        len_word1 = len(word1)
        len_word2 = len(word2)
        while (p_word1 < len_word1  and p_word2< len_word2):
            result+= word1[p_word1]
            result+= word2[p_word2]
            p_word1 +=1
            p_word2 +=1
             
        if p_word1 < len_word1:
            result+=word1[p_word1:]
            
            
        if p_word2 <  len_word2:
            result+=word2[p_word2:]
        return result
        
            
            
        