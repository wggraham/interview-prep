# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cleaned = set()

        def dfs(robot, x, y, direction):
            if (x, y) in cleaned:
                return
            robot.clean()
            cleaned.add((x, y))
            for i, (dx, dy) in enumerate(directions[direction:] + directions[:direction]):
                nx = x + dx
                ny = y + dy
                if robot.move():
                    dfs(robot, nx, ny, (direction + i) % 4)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                else:
                    robot.turnRight()

        dfs(robot, 0, 0, 0)

    def cleanRoom2(self, robot):
        def dfs(robot, x, y, dx, dy):
            robot.clean()
            visited.add((x, y))

            for _ in range(4):
                if (x + dx, y + dy) not in visited and robot.move():
                    dfs(robot, x + dx, y + dy, dx, dy)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                robot.turnLeft()
                dx, dy = -dy, dx
        visited = set()
        dfs(robot, 0, 0, 0, 1)


