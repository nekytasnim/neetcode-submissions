class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        output = 0

        for i in nums:
            if (i - 1) not in set_nums:
                count = 0
                while (i + count) in set_nums:
                    count += 1
                output = max(count, output) 
        return output 
        