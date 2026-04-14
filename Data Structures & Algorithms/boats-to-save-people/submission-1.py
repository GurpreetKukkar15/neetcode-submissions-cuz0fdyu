class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people)-1
        boat= 0
        while i <= j:
            current_weight= people[i]+people[j]
            if current_weight > limit:                
                j-=1
            else:
                i+=1
                j-=1
            boat+=1
        return boat
                

