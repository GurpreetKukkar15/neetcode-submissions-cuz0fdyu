from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Use a set. It's more direct for O(1) existence checks.
        if not nums:
            return 0
            
        num_set = set(nums)

        # 2. Find the valid start of sequences (your logic was perfect)
        valid_start = []
        for num in num_set: # Bonus: Iterating the set is faster if nums has duplicates
            if (num - 1) not in num_set:
                valid_start.append(num) # Fixed the typo!

        # 3. Follow the sequence and check how long it goes
        longest = 0
        for start in valid_start:
            count = 1  # Fix 1: A sequence always has at least 1 number (the start)
            
            # Fix 2: Use a 'while' loop to *follow* the sequence
            current_num = start
            while (current_num + 1) in num_set:
                count += 1
                current_num += 1 # Move to the next number in the sequence
            
            longest = max(longest, count)
            
        return longest

        # Note: Your logic will return 0 if nums is empty, which is correct
        # if you initialize longest = 0. My added "if not nums" is just
        # a quick exit. Your way is fine too if longest starts at 0.