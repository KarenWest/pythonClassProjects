# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        position = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(position):
            self.setRobotPosition(position)
            self.room.cleanTileAtPosition(position)
        else:
            self.setRobotDirection(int(random.random() * 360))