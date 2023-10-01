class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0  # Initialize the maximum consecutive count to 0
        current_count = 0  # Initialize the current consecutive count to 0
        
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)  # Update max_count if needed
            else:
                current_count = 0  # Reset current_count when encountering 0
            
        return max_count
