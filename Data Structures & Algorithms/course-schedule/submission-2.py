class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses

        adj_list = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj_list[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                finish += 1
                for nei in adj_list[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)

        return finish == numCourses

                




        


        