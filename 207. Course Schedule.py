class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list with a hasp map
        # Iterates through all courses. For each course,
        # it checks if a cycle exists using the dfs function.
        # If it finds a cycle for any course, it returns False,
        # (indicating it is impossible to finish all courses. )
        # If no cycles are found for any course, it returns True,
        # (indicating it is possible to finish all courses.)
        # Remember to backtrack

        # Map each course to its prerequisite list
        preMap = defaultdict(list)
        for course, pre in prerequisites:
            preMap[course].append(pre)

        # Set to track all courses along the current DFS path
        visitSet = set()

        # check if it's possible to finish all courses without running into a cycle
        def dfs(course):
            # this means we saw this course before and run into a cycle
            if course in visitSet:
                return False
            # this means no prereq for this course
            if preMap[course] == []:
                return True

            visitSet.add(course)
            # When exploring the prereq of a course,
            # the function recursively calls dfs on each prereq.
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            # After processing all prereq, it removes the course from the visitSet to backtrack.
            # So that we don't falsely detect a cycle due to a course
            # that might be visited again in a different path.
            visitSet.remove(course)
            # Avoid redundant exploration of already processed courses and their prereq
            preMap[course] = []
            return True

        # Check if it is possible to finish all courses without running into a cycle
        # You have to take courses labeled from 0 to numCourses - 1
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

    # Time: O(e+n) edges + nodes
    # Soace: O(N), due to preMap and visitSet and recursive calls 