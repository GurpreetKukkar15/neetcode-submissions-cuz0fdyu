class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack= []
        for asteroid in asteroids:
            alive=True
            while stack and alive:
                if stack[-1]>0 and asteroid < 0:
                    if abs(asteroid)<stack[-1]:
                        alive=False
                    elif abs(asteroid)==stack[-1]:
                        stack.pop()
                        alive= False
                    else:
                        stack.pop()
                else:
                    break
            if alive:
                stack.append(asteroid)
        return stack


            
                
            