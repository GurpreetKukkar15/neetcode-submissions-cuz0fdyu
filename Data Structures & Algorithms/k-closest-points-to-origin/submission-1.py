class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        given points[i] as [xi, yi]
            - points in XY plane
        to return K closest to the (0,0)
            - k closest point to the origin
            - nearer first , with duplicates
            - farther later , with duplicates
        where distance from origin is Eucledian
            - which can we simplied to sqrt ( x**2 + y**2)
        
        Input: points = [[0,2],[2,0],[2,2]], k = 2
            - let's call them points A B C
        [ A, B, C] , k = 2 ( 2 closest point to the origin)

        treat it as another problem:
        make a hashmap of tuple(xi, yi) : (dist from origin)

        I can take one point at a point and insert it into a heap
            - insert the key value pair of (xi,yi):(dist from origin)
            - while the heap is done using vale(dist from origin)
        heap keep tracks of the min.
            - we can just keep k points in the heap to reduce TC to k
        so when we complete the heap
            - we find the min k dist points
        pop them all and return them into a list

        '''
        # max heap
        maxHeap = []
        for x,y in points:
            #calcualte dist
            dist = - ((x**2)  + (y**2))

            # we just want to insert k values into the heap

            if len(maxHeap)<k:
            # fill the maxheap
                heapq.heappush(maxHeap, [dist,x,y])
            else:
                heapq.heappushpop(maxHeap,[dist,x,y])
        
        return [[x,y] for (dist,x,y) in maxHeap]











        
        