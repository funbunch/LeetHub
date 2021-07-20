class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        
        """
        - count consective ones and track high score
        
        - count counsective zeros and track high score
        
        - return high_ones > high_zeroes
        
         - count consective ones and track high score
        - return high score

        """
        
        one_counter = 0 
        one_high_score = 0

        zero_counter = 0
        zero_high_score = 0
        
        for i in s:
            if i == '1':
                one_counter += 1
                one_high_score = max(one_counter, one_high_score)
                zero_counter = 0
            if i == "0":
                zero_counter += 1
                zero_high_score = max(zero_counter, zero_high_score)
                one_counter  = 0
                
            # if i == 1
                # increment our one_counter
                # check of this is newest high score for ones
                # reset the zero_counter
            # if i == 0
                # increment our zero_counter
                # check if this is newest high score for zeroes
                # reset the one_counter
                
        return one_high_score > zero_high_score
                
            
       