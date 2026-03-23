# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Pattern:
#     Topological sort with graph traversal

# Approach:
#     I have a couple of approaches I can take here. One using DFS and the other using BFS (Kahn's algorithm)
#     For DFS:
#         - I first want to create a mapping from course -> prereq from the input array
#         - I keep track of visited and visiting set. 
#             - Visited will optimize our traversal so we don't revisit a path we've already verified
#             - Visiting will keep track of nodes we are visiting in our current path so we don't enter an infinite loop
#         - When we traverse with DFS, we want to check if the node exists in visited and visiting
#             - If in visited, then we can return True as we've already verified this path
#             - If in visiting, then we return False as there is a circular reference and courses cannot be completed
#         - We want to make sure we traverse all courses and its prereqs
#         - When we finish each course's traversal, we add to the result array
#         - Return the result array if all courses were able to be traversed, else empty array
#     For BFS:
#         - I first want to create a mapping from prereq -> course from the input array
#         - I keep track of number of prereqs left per course in an array
#         - I queue up courses with no prereqs left
#         - I go through the queue and remove the course from courses that depend on them and decrease the number of prereq left count
#         - Every time we dequeue a course, we add to the result array
#         - I continue while keeping track of courses completed
#         - If courses completed == numCourses then we return result array, else empty array

# Time & Space complexity:
#     Time complexity is O(n) time complexity is linear in the number of courses and prerequisites, since we visit each course once and process each dependency once.
#     Space complexity is O(n) space complexity is linear as the size of the queue, courseMap, result grows depending on the number of courses and prerequisites

# DFS
class SolutionDFS:
    def courseSchedule2(self, numCourses: int, prereqs: list[list[int]]) -> list[int]:
        courseMap = {}

        for course, prereq in prereqs:
            courseMap[course] = courseMap.get(course, [])
            courseMap[course].append(prereq)

        visited = set()
        visiting = set()

        result = []

        def dfs(node):
            if node in visited:
                return True
            
            if node in visiting:
                return False
            
            visiting.add(node)

            for neighbor in courseMap.get(node, []):
                if not dfs(neighbor):
                    return False
                
            visiting.remove(node)
            visited.add(node)
            result.append(node)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return result
    
class SolutionBFS:
    def courseSchedule2(self, numCourses: int, prereqs: list[list[int]]) -> list[int]:
        prereqMap = {}
        prereqRequired = [0] * numCourses

        for course, prereq in prereqs:
            prereqMap[prereq] = prereqMap.get(prereq, [])
            prereqMap[prereq].append(course)
            prereqRequired[course] += 1

        queue = []
        queuePointer = 0

        for prereq, count in enumerate(prereqRequired):
            if count == 0:
                queue.append(prereq)

        result = []
        courseCompleted = 0

        while queuePointer < len(queue):
            prereq = queue[queuePointer]
            queuePointer += 1

            result.append(prereq)
            courseCompleted += 1

            for course in prereqMap.get(prereq, []):
                prereqRequired[course] -= 1

                if prereqRequired[course] == 0:
                    queue.append(course)

        return result if courseCompleted == numCourses else []

