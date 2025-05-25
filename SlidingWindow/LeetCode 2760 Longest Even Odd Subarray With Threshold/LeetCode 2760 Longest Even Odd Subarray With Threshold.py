class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        longest_len=0
        n=len(nums)
        for l in range(n):
            if nums[l] <= threshold and nums[l] % 2 == 0:
                current_len = 1 
                longest_len = max(longest_len,current_len)
                for r in range(l+1,n):
                    if nums[r] <= threshold and nums[r-1]%2 != nums[r]%2:
                        current_len=(r-l)+1
                        longest_len=max(longest_len,current_len)
                    else:
                        break 
        return longest_len
        