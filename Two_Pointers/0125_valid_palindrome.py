
class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s=s.lower()
        left,right=0,len(s)-1

        while left<right:
            if new_s[left].isalnum()==False:
                left+=1
            elif new_s[right].isalnum()==False:
                right-=1
            elif new_s[left]!=new_s[right]:
                return False
            else:
                left+=1
                right-=1
        
        return True
            
        
