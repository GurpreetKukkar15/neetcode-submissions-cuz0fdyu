class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sp, fp= 0, len(numbers)-1

        while sp < fp:
            if numbers[sp]+numbers[fp] < target:
                sp+=1
            elif numbers[sp]+numbers[fp] > target:
                fp-=1
            else:
                return [sp+1, fp+1]
        return []
