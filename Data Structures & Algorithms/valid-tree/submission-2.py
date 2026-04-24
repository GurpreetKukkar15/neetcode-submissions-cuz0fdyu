class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = [[] for _ in range(n)]
         
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        def dfs(root , prev):
            if root in visited:
                return False
            
            visited.add(root)
            for nei in adj[root]:
                if nei == prev:
                    continue
                if not dfs(nei, root):
                    return False
            return True

        return dfs(0,-1) and len(visited) == n
                