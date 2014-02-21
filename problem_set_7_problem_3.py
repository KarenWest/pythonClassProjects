# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    anim = False
    steps = 0
    for _ in range(num_trials):
        robots = []
        room = RectangularRoom(width, height)
        for _ in range(num_robots):
            robots.append(robot_type(room, speed))
        total_tiles = float(room.getNumTiles())
        if anim:
            anim = ps7_visualize.RobotVisualization(num_robots, width, height)
        while room.getNumCleanedTiles() / total_tiles < min_coverage:
            steps += 1
            for r in robots:
                if anim:
                    anim.update(room, robots)
                r.updatePositionAndClean()
        if anim:
            anim.done()
    return steps / float(num_trials)