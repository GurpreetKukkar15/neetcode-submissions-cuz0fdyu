class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=sorted(zip(position, speed))
        stack= []
        
        for pos, spd in reversed(pairs):
            if stack and ((target-pos)/spd) > stack[-1]:
                stack.append((target-pos)/spd)
            elif not stack:
                stack.append((target-pos)/spd)   
        
        return len(stack)