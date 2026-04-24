class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        cpu tasks 
        where tasks[i] 
        range A - Z
        int n = same task must be separated by n CPU cycle ( to cooldown )

        each cycle we can only complete one task
            - constraint
        task may be completed in any order
            - relax
        
        eg . Input: tasks = ["X","X","Y","Y"], n = 2
        '''

        count = Counter(tasks)
        maxHeap = [ -cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # insert [ -cnt, time of availibility = time + n]

        while maxHeap or q:
            time += 1

            # get the time of the first element from the q
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])                    
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time




