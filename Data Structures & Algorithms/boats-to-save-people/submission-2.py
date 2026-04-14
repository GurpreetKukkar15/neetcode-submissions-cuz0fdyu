class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people)-1
        boat= 0
        while i <= j:
            remaining_limit = limit - people[j]
            j-=1
            boat+=1
            if i <= j and remaining_limit >= people[i]:
                i+=1

        return boat
                

