from collections import defaultdict 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        seen=defaultdict(int)
        count=0
        current_sum=0
        seen[0]=1

        for num in nums:
            current_sum+=num
            prev_running_sum=current_sum-k

            if prev_running_sum in seen:
                count+=seen[prev_running_sum]

            seen[current_sum]+=1

        return count




            


