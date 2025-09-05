class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for c, p in prerequisites:
            adj[c].append(p)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            if states[node] == VISITED:
                return True
            if states[node] == VISITING:
                return False

            states[node] = VISITING

            for c in adj[node]:
                if not dfs(c):
                    return False

            states[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
