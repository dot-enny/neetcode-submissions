class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        count, most_freq = {}, []
        
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        j = 0
        while j < k:
            max_key = max(count, key=count.get)
            most_freq.append(max_key)
            del count[max_key]
            j+=1

        return most_freq
