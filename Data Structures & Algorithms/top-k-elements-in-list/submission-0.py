class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        result = []
        bucket = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            if i not in freq_dict:
                freq_dict[i] = 0
            freq_dict[i] += 1 
        
        for num, freq in freq_dict.items():
            bucket[freq].append(num)
        
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
            if len(result) == k:
                return result
            
         
            

