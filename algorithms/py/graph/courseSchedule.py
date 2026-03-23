# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Pattern:
    # Topological sort with graph traversal

# Approach:
    # I create a mapping of courses and prerequisites. I can go two ways:
    #     - course -> prerequisites we keep hashsets to see if there's any circular reference
    #     - prereq -> courses (Kahn's algorithm) where I will find a prereq course without any prereqs 
    #                          then move to courses to reduce their prereq count by 1, continue to see if we can exhaust all courses

# Time & Space complexity:
#     Time complexity of both approaches are O(n) where n is the size of the numCourses
#     Space complexity of both appraoches are O(n) as well

# Standard DFS
class SolutionDFS:
    def courseSchedule(self, numCourses: int, prereqs: list[list[int]]) -> bool:
        courseMap = {}

        for course, prereq in prereqs:
            courseMap[course] = courseMap.get(course, [])
            courseMap[course].append(prereq)

        visited = set()
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True

            visiting.add(course)

            if course in courseMap:
                for neighbor in courseMap[course]:
                    if not dfs(neighbor):
                        return False

            visiting.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return False
        
        return True
            
# Kahn's Algorithm (BFS)
class SolutionBFS:
    def courseSchedule(self, numCourses: int, prereqs: list[list[int]]) -> bool:
        prereqMap = {}
        prereqFreqBucket = [0] * numCourses

        for course, prereq in prereqs:
            prereqMap[prereq] = prereqMap.get(prereq, [])
            prereqMap[prereq].append(course)

        for prereq, courses in prereqMap.items():
            for course in courses:
                prereqFreqBucket[course] += 1

        queue = []
        queueIndex = 0

        for i in range(len(prereqFreqBucket)):
            if prereqFreqBucket[i] == 0:
                queue.append(i)

        completed = 0

        while queueIndex < len(queue):
            course = queue[queueIndex]
            queueIndex += 1

            courses = prereqMap.get(course, [])
            for course in courses:
                prereqFreqBucket[course] -= 1

                if prereqFreqBucket[course] == 0:
                    queue.append(course)
            
            completed += 1

        return completed == numCourses