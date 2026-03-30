from __future__ import annotations

# Dependency Finish
#
# There are numCourses labeled from 0 to numCourses - 1.
# Each pair [a, b] means b must be completed before a.
# Return True if it is possible to finish all courses.
#
# Input: numCourses = 2, prerequisites = [[1, 0]]
# Output: True
# Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
# Output: False

class SolutionDFS:
    def solve(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        courseMap = {}

        for course, prereq in prerequisites:
            courseMap[course] = courseMap.get(course, [])
            courseMap[course].append(prereq)

        visited = set()
        visiting = set()

        def dfs(course):
            if course in visited:
                return True
            
            if course in visiting:
                return False
            
            visiting.add(course)

            for prereq in courseMap[course]:
                if dfs(prereq) == False:
                    return False
                
            visiting.remove(course)
            visited.add(course)

            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
            
        return True

class SolutionBFS:
    def solve(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        courseMap = {}
        prereqFreqBucket = [0] * numCourses

        for course, prereq in prerequisites:
            courseMap[prereq] = courseMap.get(prereq, [])
            courseMap[prereq].append(course)
            prereqFreqBucket[course] += 1

        queue = []
        queuePointer = 0

        for prereq in range(len(prereqFreqBucket)):
            if prereqFreqBucket[prereq] == 0:
                queue.append(prereq)

        courseCompleted = 0

        while queuePointer < len(queue):
            prereq = queue[queuePointer]
            queuePointer += 1

            courseCompleted += 1

            for course in courseMap.get(prereq, []):
                prereqFreqBucket[course] -= 1

                if prereqFreqBucket[course] == 0:
                    queue.append(course)
        
        return courseCompleted == numCourses
            
