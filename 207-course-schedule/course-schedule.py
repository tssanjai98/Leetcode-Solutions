class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        state = [0] * numCourses

        for c, p in prerequisites:
            adj[p].append(c)        

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1
            for n in adj[course]:
                if not dfs(n):
                    return False
            state[course] = 2
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False

        return True

