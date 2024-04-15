class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list of prerequisites
        prereq = defaultdict(list)
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has 3 possible states:
        # visited -> crs has been added to res
        # visiting -> crs not added to res, but added to cycle
        # unvisited -> crs not added to res or cycle

        res = []
        added, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in added:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            res.append(crs)
            added.add(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res

# Time: O(v+e)
# spACE: o(n) because of the dict and set