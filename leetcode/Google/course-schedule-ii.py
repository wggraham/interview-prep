from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i for i in range(0, numCourses)}
        dependencies = defaultdict(set)
        children = defaultdict(set)
        for child, parent in prerequisites:
            if child in courses:
                courses.remove(child)
            dependencies[child].add(parent)
            children[parent].add(child)

        # do bfs from roots
        courses = deque(courses)
        schedule = []
        while courses:
            course = courses.popleft()
            schedule.append(course)
            for child in children[course]:
                dependencies[child].remove(course)
                if not dependencies[child]:
                    courses.append(child)

        return schedule if len(schedule) == numCourses else []


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
numCourses = 3
prerequisites = [[1, 0], [1, 2], [0, 1]]
test = Solution()
print(test.findOrder(numCourses, prerequisites))
