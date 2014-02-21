# 6.00x Problem Set 7: Simulating robots

import math
import random

import ps7_visualize
import pylab

# For Python 2.7:
from ps7_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, comment out what's above and
# uncomment this line (for Python 2.6):
# from ps7_verify_movement26 import testRobotMovement

# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(Position):
    width = 0
    height = 0
    numTiles = 0
    tiles = {}
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.numTiles = width * height
        print "width, height, numTiles for rectangular floor"
        print width
        print height
        print self.numTiles

        for w in range(0,width):
            for h in range(0,height):
                #NOTE--float width,height as tuple keys don't work?!
                #so could not use Position(), since those x,y's can be floats
                #tuples of ints (w,h) could be used
                self.tiles[(w,h)] = 0 # value of key tuple (w,h) = 0 = dirty (or vice versa, 1 = clean)
        #self.printTiles()
        #raise NotImplementedError
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        #Return the floor of x as a float, the largest integer value less than
        #or equal to x
        posx = pos.getX()
        posy = pos.getY()
        posx = math.floor(posx)
        posy = math.floor(posy)
        print "cleaning at tile position posx = " + str(posx) + " pos y = " + str(posy)
        #print "pos x " + str(posx) + " pos y " + str(posy)
        self.tiles[(posx, posy)] = 1 # using 0 as dirty value, 1 as clean value, of key tuple pos(x,y)
        #self.printTiles()
        #raise NotImplementedError

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (x, y) is cleaned, False otherwise
        """
        posx = math.floor(m)
        posy = math.floor(n)

        print "m (width value of tile = " + str(m)
        print "n (height value of tile = " + str(n)
        cleanOrDirty = 0 #dirty value
        if (posx,posy) in self.tiles.keys():
            cleanOrDirty = self.tiles[(posx, posy)]
            print "pos key found - clean or dirty value = " + str(cleanOrDirty)
            if (cleanOrDirty == 1):
                return True
            else:
                return False
        else:
            print "pos key NOT found!"
            return False

        #raise NotImplementedError
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.numTiles
        #raise NotImplementedError

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        tilesCopy = {}
        tilesCopy = self.tiles.copy()
        numCleanTiles = 0
        
        for posTupleKey, posVal in tilesCopy.items():
            if posVal == 1:
                numCleanTiles += 1
        return numCleanTiles
        #raise NotImplementedError

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        posx = random.randrange(0, self.width)
        posy= random.randrange(0, self.height)
        randPos = Position(posx, posy)
        return randPos

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        #if key tuple position(x,y) is in dictionary tiles return True else return False
        posx = pos.getX()
        posy = pos.getY()
        posx = math.floor(posx)
        posy = math.floor(posy)
        if (posx >= self.width) or (posy >= self.height):
            return False

        if (posx,posy) in self.tiles.keys():
            return True
        else:
            return False

    def printTiles(self): #prints random order!
        tilesCopy = self.tiles.copy()
        for posKey, posVal in tilesCopy.items():
            print posKey
            print posVal

class Robot(RectangularRoom):
    room = 0
    speed = 0.0
    direction = 0.0
    position = 0.0
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randrange(0,359)
        #raise NotImplementedError

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
        #raise NotImplementedError
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction
        #raise NotImplementedError

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        posx = position.getX()
        posy = position.getY()
        self.position = Position(posx, posy)
        #raise NotImplementedError

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction
        #raise NotImplementedError

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.

        NOTE: Subclasses that inherit the Robot class will implement the
        updatePositionAndClean() function.
        """
        raise NotImplementedError # don't change this!

#test RectangularRoom() with Positiion()
print "creating a 5 wide by 5 tall rectangular tiled room"
recRoom5by5 = RectangularRoom(5,5)

print "creating a tile position at (4,4), really the (5,5) tile, with indices 0-4"
posToClean4by4 = Position(4,4) #recall 5by5 rectangle has indices 0-4,0-4, so 5th tile cleaned
print "telling tile at (4,4) to get cleaned, really the (5,5), but indices 0-4"
recRoom5by5.cleanTileAtPosition(posToClean4by4)
print "Now find out whether tile at (4,4), 5th tile, is clean (should be!)"
print recRoom5by5.isTileCleaned(4,4)
print "Now find out whether tile at (0,0), 1st tile, is clean, should not be yet"
print recRoom5by5.isTileCleaned(0,0)
print "How many tiles total do we have here?"
print recRoom5by5.getNumTiles()
print "How many cleaned tiles do we have?"
print recRoom5by5.getNumCleanedTiles()
#everything above works at this point
randPos = recRoom5by5.getRandomPosition()
print "Is the position we created that we cleaned, (4,4), 5th tile, in room?"
print recRoom5by5.isPositionInRoom(posToClean4by4)
print "Is the random position we just created in room?"
print recRoom5by5.isPositionInRoom(randPos)
posNotCleanYet6by6 = Position(6,6)
print "Is the (6,6) tile in this room (should not be for this particular test)"
print recRoom5by5.isPositionInRoom(posNotCleanYet6by6)

#now test with Robot class
print "initializing a robot class to room 5by5, speed 100.0"
robotTest = Robot(recRoom5by5, 100.0)
print "what position is the robot at?"
print robotTest.getRobotPosition()
print "in what direction is the robot going right now?"
print robotTest.getRobotDirection()
print "give robot Position at 5th tile, (4,4):"
robotTest.setRobotPosition(posToClean4by4)
print "give robot new direction:"
robotTest.setRobotDirection(150.0)
print robotTest.getRobotPosition()
print robotTest.getRobotDirection()
