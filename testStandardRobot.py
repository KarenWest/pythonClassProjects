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
        #print "new x = " + str(new_x) + " new y " + str(new_y)
        #print "floor of x = " + str(math.floor(new_x)) + " floor of y = " + str(math.floor(new_y))
    
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

        cleanOrDirty = 0 #dirty value
        if (posx,posy) in self.tiles.keys():
            cleanOrDirty = self.tiles[(posx, posy)]
            #print "pos key found - clean or dirty value = " + str(cleanOrDirty)
            if (cleanOrDirty == 1):
                return True
            else:
                return False
        else:
            #print "pos key NOT found!"
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
        #then clean this first tile!
        self.room.cleanTileAtPosition(self.position)
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
        #X direction (num. rows) wall limit is the width of rectangular room
        #Y direction (num. cols) wall limit is the height of rectangular room
        #So (0,0) is in bottom LEFT corner--since rows start at zero at BOTTOM, not top
        #direction works as you would think, with east at 0 or 360 degrees, 90 degrees at north,
        #180 degrees at west, and 270 degrees at south direction

        #so each time unit, getNewPosition in SAME direction if you don't hit the wall
        #if you hit the wall, then get a new RANDOM direction and then recalculate new position,
        #making sure it is a valid position on grid, has not already been cleaned (tile visited)

        #So it makes no difference which direction you are moving in--the getNewPosition() function
        #figures out mathematically what the next position is, based on grid, and you just have to
        #determine whether you have hit the wall in that same direction--don't have to look at the
        #number the degrees or radians in that particular direction--just moving in same direction,
        #get next position, do you hit the wall, if so get new random direction, move that way, if you
        #won't hit a wall that way.

        #If you don't hit a wall when you calculate a new direction, but the tile is clean already, then
        #just go through the tiles and find one that is not clean yet, and move in the same direction.
        
        robotPos = self.getRobotPosition()
        posx = robotPos.getX()
        posy = robotPos.getY()
        posx = math.floor(posx)
        posy = math.floor(posy)
        #First check if this position is clean:
        #if (self.room.isTileCleaned(posx,posy) == False):
            #then clean this tile!
            #self.room.cleanTileAtPosition(robotPos)
        #Now see where to move robot next on floor and clean that tile if it is not clean
        #So first try moving in same direction--will you hit a wall?
        newPos = self.position.getNewPosition(self.direction,self.speed)
        newPosx = newPos.getX()
        newPosy = newPos.getY()
        newPosx = math.floor(newPosx)
        newPosy = math.floor(newPosy)
        if (self.room.isPositionInRoom(newPos)) and (self.room.isTileCleaned(newPosx,newPosy) == False):
            #position is in room AND the tile has NOT been visited yet--since it's still DIRTY
            #Should NOT have to check whether you hit a wall, since new position is in room
            #so NO NEW DIRECTION needed yet--move in SAME direction
            self.setRobotPosition(newPos)
            self.room.cleanTileAtPosition(newPos)
            #print "Moved in SAME DIRECTION I was moving in last time, direction = " + str(self.direction)
        else: # (self.room.isPositionInRoom(newPos) == False) or (self.room.isTileCleaned(newPosx, newPosy) == True):
            # either HIT WALL -- OR -- tile already cleaned -- so calculate new RANDOM direction

            #NOTE: this works until you are surrounded by tiles that have no next step tile that has not already been
            #cleaned?
            #?? think a problem is that if all surrounding tiles are already clean, then, in that case,
            #you can get stuck in situation where you keep recalculating a new random direction, but when you take a step,
            #all the next tiles have already been cleaned, and you get stuck in a loop, so in this case, you must
            #not recalculate a new direction, but rather keep going in same direction until you find a tile not clean,
            #and jump to that tile instead, and go from there.
            #So find this case--see if that corrects this issue!
            
            keepTryingNewDirection = True
            while (keepTryingNewDirection == True):
                self.direction = random.randrange(0,359) #get new random direction
                newPos = self.position.getNewPosition(self.direction,self.speed) #get new next position step with new direc.
                newPosx = newPos.getX()
                newPosy = newPos.getY()
                newPosx = math.floor(newPosx)
                newPosy = math.floor(newPosy)
                if (self.room.isPositionInRoom(newPos)) and (self.room.isTileCleaned(newPosx,newPosy) == False):
                    #new position in new direction is in room, and the tile has not been cleaned yet
                    #so new direction and new tile to clean found!
                    self.setRobotPosition(newPos)
                    self.room.cleanTileAtPosition(newPos)
                    #print "Moved in NEW DIRECTION I was moving in last time, direction = " + str(self.direction)
                    keepTryingNewDirection = False
                elif (self.room.isPositionInRoom(newPos) == False):
                    #new position in new direction NOT in room -- try again!
                    #print "new direction found a new position not in room --hit wall--try again! direction = " + str(self.direction)
                    continue
                else:
                    #print "new direction produced new position in room but tile already clean--try again?! direction = " + str(self.direction)
                    #print "first check to see if all tiles have already been cleaned."
                    #?? Any other checks needed here? list of tiles visited? is this really needed??
                    #calculate list of cells not clean yet
                    tilesCleaned = []
                    allSurroundingTilesClean = False
                    foundTileUnclean = False
                    saveWidth = 0
                    saveHeight = 0
                    for i in range(0,self.room.width):
                        for j in range(0,self.room.height):
                            if (self.room.isTileCleaned(i,j) == False):
                                saveWidth = i
                                saveHeight = j
                                foundTileUnclean = True
                            else:
                                #print "appending to tiles cleaned: tile: i = " + str(i) + " j = " + str(j)
                                tilesCleaned.append((i,j)) #make list of tiles cleaned
                    if (foundTileUnclean == True):
                        #print "not all tiles are clean!--start here rather than getting new direc. i = " + str(saveWidth) + " j = " + str(saveHeight)
                        newPos = Position(saveWidth,saveHeight)
                        self.setRobotPosition(newPos)
                        self.room.cleanTileAtPosition(newPos)
                        #print "Found new tile that was not clean! current direc. " + str(self.direction)
                        #print "tile location x = " + str(saveWidth) + " y = " + str(saveHeight)
                        keepTryingNewDirection = False
                    else:
                        keepTryingNewDirection = False
                        #print "all tiles clean! stop cleaning!-- do not look for new direction! should be done."

                    #for tile in tilesCleaned:
                        #print tile

'''
The rest here is commented out--not needed for StandardRobot()!  Correct Test Results are at bottom.
Not deleting yet though since there is more code to write, and who knows whether or not it will be useful or not yet!

                           
                        #Here in this case--found a tile NOT clean--but are it's surrounding tiles all clean?
                        #check surrounding tiles of this unclean tile and see if they are all clean!
                        #the reason being--if all surrounding tiles are clean, but this one is not, no matter which
                        #direction you move in, you will see that in your next step, all tiles are already clean,
                        #and you must choose your next tile to clean not based on a new direction, but on what tiles
                        #have not been cleaned yet--and jump there

                        #First--determine if all surrounding tiles are clean already--in which case a JUMP is needed, not new direc.
                        #Note: rows and cols are numbered such that lower left corner of grid is (0,0)
                        allSurroundingTilesClean = True
                        newX = i
                        newY = j
                        if (i < (self.room.width - 1)): #go up in width dimension
                            if (self.room.isTileCleaned(i+1,j) == False):
                                allSurroundingTilesClean = False
                                newX = i + 1
                                newY = j
                        if (i > 0) and (allSurroundingTilesClean == True): #go down in width dimension
                            if (self.room.isTileCleaned(i-1,j) == False):
                                allSurroundingTilesClean = False
                                newX = i - 1
                                newY = j
                        if (j < (self.room.height - 1)) and (allSurroundingTilesClean == True): #go up in height dimension
                            if (self.room.isTileCleaned(i,j+1) == False):
                                allSurroundingTilesClean = False
                                newX = i
                                newY = j + 1
                        if (j > 0) and (allSurroundingTilesClean == True): #go down in height dimension
                            if (self.room.isTileCleaned(i,j-1) == False):
                                allSurroundingTilesClean = False
                                newX = i
                                newY = j - 1
                        if (i < (self.room.width - 1)) and (j > 0) and (allSurroundingTilesClean == True): #go on diagonal to upper left
                            if (self.room.isTileCleaned(i+1, j-1) == False):
                                allSurroundingTilesClean = False
                                newX = i + 1
                                newY = j - 1
                        if (i < (self.room.width - 1)) and (j < (self.room.height - 1)) and (allSurroundingTilesClean == True): #go on diagonal to upper right
                            if (self.room.isTileCleaned(i+1, j+1) == False):
                                allSurroundingTilesClean = False
                                newX = i + 1
                                newY = j + 1
                        if (i > 0) and (j > 0) and (allSurroundingTilesClean == True): #go on diagonal to lower left
                            if (self.room.isTileCleaned(i-1, j-1) == False):
                                allSurroundingTilesClean = False
                                newX = i - 1
                                newY = j - 1
                        if (i > 0) and (j < (self.room.height - 1)) and (allSurroundingTilesClean == True): #go on diagonal to lower right
                            if (self.room.isTileCleaned(i-1, j+1) == False):
                                allSurroundingTilesClean = False
                                newX = i - 1
                                newY = j + 1
                        
                        if (allSurroundingTilesClean == True): #all surrounding tiles clean --must JUMP
                            noUncleanTileFound = True
                            while (noUncleanTileFound == True):
                                if (i < (self.room.width - 1)): #check next tile UP in width dimension
                                    tryPosx = i + 1
                                    tryPosy = j
                                    i += 1
                                elif (i > 0): #check next tile DOWN in width dimension
                                    tryPosx = i - 1
                                    tryPosy = j
                                    i -= 1
                                elif (j < (self.room.height - 1)): #check next tile UP in height dimension
                                    tryPosx = i
                                    tryPosy = j + 1
                                    j += 1
                                elif (j > 0): #check next tile DOWN in height direction
                                    tryPosx = i
                                    tryPosy = j - 1
                                    j -= 1
                                elif (i < (self.room.width - 1)) and (j > 0): #check diagonal tile in upper left
                                    tryPosx = i + 1
                                    tryPosy = j - 1
                                    i += 1
                                    j -= 1
                                elif (i < (self.room.width - 1)) and (j < (self.room.height - 1)): #check diagonal tile in upper right
                                    tryPosx = i + 1
                                    tryPosy = j + 1
                                    i += 1
                                    j += 1
                                elif (i > 0) and (j > 0): #check diagonal tile in lower left
                                    tryPosx = i - 1
                                    tryPosy = j - 1
                                    i -= 1
                                    j -= 1
                                elif (i > 0) and (j < (self.room.height - 1)): #check diagonal tile in lower right
                                    tryPosx = i - 1
                                    tryPosy = j + 1
                                    i -= 1
                                    j += 1
                                else:
                                    print "uh-oh -- all tiles must be clean??  thought I checked that already!"
                                if (self.room.isTileCleaned(tryPosx,tryPosy) == False): #found unclean tile--take it!
                                    newPos = Position(tryPosx,tryPosy)
                                    self.setRobotPosition(newPos)
                                    self.room.cleanTileAtPosition(newPos)
                                    print "Had to JUMP to a new tile that was not clean! current direc. " + str(self.direction)
                                    print "tile location x = " + str(tryPosx) + " y = " + str(tryPosy)
                                    noUncleanTileFound = False
                                    keepTryingNewDirection = False
                                else:
                                    print "this tile clean too! try again. x = " + str(tryPosx) + " y = " + str(tryPosy)
                            else: #a surrounding tile was found unclean --take that
                                newPos = Position(newX,newY)
                                self.setRobotPosition(newPos)
                                self.room.cleanTileAtPosition(newPos)
                                print "Found new tile next to this one that was not clean! current direc. " + str(self.direction)
                                print "tile location x = " + str(newX) + " y = " + str(newY)
                                noUncleanTileFound = False
                                keepTryingNewDirection = False

        


#another goof!
        if (self.direction >= 0) and (self.direction < 90):
            #
            #moving in positive x, positive y direction, x being rows, y cols
            #so (posx + 1) takes you toward BOTTOM of rectangle, since adding to ROWS brings you downward in rectangle??
            #and (posy + 1)
            if ((posx + 1) >= self.room.width) or ((posy + 1) >= self.room.height):
                needNewDirection = True
                self.direction = random.randrange(90,179)
        else: #continue in same direction--have not hit wall yet in positive x dir or positive y dir
            print "continuing in direction " + str(self.direction)
        if (self.direction >= 90) and (self.direction < 180): #moving in negative x, positive y direction
            if ((posx - 1) < 0) or ((posy + 1) >= self.room.height):
                needNewDirection = True
                self.direction = random.randrange(180,269)
        else: #continue in same direction--have not hit wall yet in negative x dir or positive y dir
            posx -= 1
            posy += 1
        if (self.direction >= 180) and (self.direction < 270): #moving in negative x, negative y direction
            if ((posx - 1) < 0) or ((posy - 1) < self.room.height):
                needNewDirection = True
                self.direction = random.randrange(180,269)
        else: #continue in same direction--have not hit wall yet in negative x dir or positive y dir
            posx -= 1
            posy += 1

        if (needNewDirection == False):
            newPos = Position(posx,posy)
            self.setRobotPosition(newPos)
            self.room.cleanTileAtPosition(newPos)
            newPosx = newPos.getX()
            newPosy = newPos.getY()
            newPosx = math.floor(newPosx)
            newPosy = math.floor(newPosy)
            self.tilesVisited.append((newPosx,newPosy))
            print "Taking another step in the same direction"
        else: calculate new direction  -- hit a wall!
            newPos = self.position.getNewPosition(self.direction,self.speed)
            newPos = self.position.getNewPosition(self.direction,self.speed)
            newPosx = newPos.getX()
            newPosy = newPos.getY()
            newPosx = math.floor(newPosx)
            newPosy = math.floor(newPosy)
            if (self.room.isPositionInRoom(newPos)) and (self.room.isTileCleaned(newPosx,newPosy) == False):
                #position is in room AND the tile has NOT been visited yet--since it's still DIRTY
                #Should NOT have to check whether you hit a wall, since new position is in room            
                self.setRobotPosition(newPos)
                self.room.cleanTileAtPosition(newPos)
                self.tilesVisited.append((newPosx,newPosy)) #do you still need this??? we will see.
                newDirecNotFound = False
                print "Found new direction"

            
#and another goof!
        robotPos = self.getRobotPosition()
        posx = robotPos.getX()
        posy = robotPos.getY()
        posx = math.floor(posx)
        posy = math.floor(posy)
        if (self.tilesVisited == []):
            self.tilesVisited.append((posx,posy))
        print "at START of updatePositionAndClean:"
        for tile in self.tilesVisited:
            print tile
        newPos = self.position.getNewPosition(self.direction, self.speed)
        newPosx = newPos.getX()
        newPosy = newPos.getY()
        newPosx = math.floor(newPosx)
        newPosy = math.floor(newPosy)
        if (self.room.isPositionInRoom(newPos) and (self.room.isTileCleaned(newPosx,newPosy) == False) and (self.room.width > newPosx) and (self.room.height > newPosy)):
            self.setRobotPosition(newPos)
            self.room.cleanTileAtPosition(newPos)
            if ((newPosx,newPosy) not in self.tilesVisited):
                self.tilesVisited.append((newPosx,newPosy))
            print "found new direction first try"
        else: # either x or y direction hit the wall
            # calculate new direction at random
            newDirecNotFound = True
            range0to89 = False
            range90to179 = False
            range180to269 = False
            range270to359 = False
            new_x = 0.0
            new_y = 0.0
            while (newDirecNotFound == True):
                if (self.direction >= 0) and (self.direction < 90) and (range0to89 == False):
                    self.direction = random.randrange(90,179)
                    range0to89 = True
                elif (self.direction >= 90) and (self.direction < 180) and (range90to179 == False):
                    self.direction = random.randrange(180, 269)
                    range90to179 = True
                elif (self.direction >= 180) and (self.direction < 270) and (range180to269 == False):
                    self.direction = random.randrange(270, 359)
                    range180to269 = True
                elif (self.direction >= 270) and (self.direction < 359) and (range270to359 == False):
                    self.direction = random.randrange(0,89)
                    range270to359 = True
                newPos = self.position.getNewPosition(self.direction,self.speed)
                newPosx = newPos.getX()
                newPosy = newPos.getY()
                newPosx = math.floor(newPosx)
                newPosy = math.floor(newPosy)
                if (math.floor(newPosx) != math.floor(new_x)) and (math.floor(newPosy) != math.floor(new_y)) and ((newPosx, newPosy) not in self.tilesVisited):
                    if (self.room.isPositionInRoom(newPos) and (self.room.isTileCleaned(newPosx,newPosy) == False) and (self.room.width > newPosx) and (self.room.height > newPosy)):
                        self.setRobotPosition(newPos)
                        self.room.cleanTileAtPosition(newPos)
                        self.tilesVisited.append((newPosx,newPosy))
                        newDirecNotFound = False
                        print "Found new direction"
                    elif (self.room.isPositionInRoom(newPos) and (self.room.isTileCleaned(newPosx, newPosy) == True)):
                        #calculate list of cells not clean yet
                        uncleanTileXY = (0,0)
                        for i in range(0,self.room.width):
                            for j in range(0,self.room.height):
                                if (self.room.isTileCleaned(i,j) == False):
                                    uncleanTileXY = (i,j)
                                    break
                        if (uncleanTileXY == (0,0)):
                            if (self.room.isTileCleaned(0,0) == True):
                                newDirecNotFound = False
                                print "all tiles clean! -- so no new direction found"
                            else:
                                print "not all tiles are clean!--must find new direction"
                    elif (self.room.width > newPosx) and (self.room.height > newPosy):
                        print "what should I do now? which way do we go from here?"
                    else:
                        range0to89 = False
                        range90to179 = False
                        range180to269 = False
                        range270to359 = False
                else: #new direction same as previous direction calculation of x and y - try another one
                    if (self.direction >= 0) and (self.direction < 90):
                        self.direction = random.randrange(180,269)
                        range0to89 = True
                    elif (self.direction >= 90) and (self.direction < 180):
                        self.direction = random.randrange(270, 359)
                        range90to179 = True
                    elif (self.direction >= 180) and (self.direction < 270):
                        self.direction = random.randrange(0, 89)
                        range180to269 = True
                    elif (self.direction >= 270) and (self.direction < 359):
                        self.direction = random.randrange(90,179)
                        range270to359 = True
                    newPos = self.position.getNewPosition(self.direction,self.speed)
                    newPosx = newPos.getX()
                    newPosy = newPos.getY()
                    newPosx = math.floor(newPosx)
                    newPosy = math.floor(newPosy)

                    if (math.floor(newPosx) != math.floor(new_x)) and (math.floor(newPosy) != math.floor(new_y)) and ((newPosx, newPosy) not in self.tilesVisited):
                        if (self.room.isPositionInRoom(newPos) and (self.room.isTileCleaned(newPosx,newPosy) == False) and (self.room.width > newPosx) and (self.room.height > newPosy)):
                            self.setRobotPosition(newPos)
                            self.room.cleanTileAtPosition(newPos)
                            self.tilesVisited.append((newPosx,newPosy))
                            newDirecNotFound = False
                            print "found new direction after previous direction was same"
                        else:
                            print "did NOT find new direc after previous direc was same"
                            range0to89 = False
                            range90to179 = False
                            range180to269 = False
                            range270to359 = False
                new_x = newPosx
                new_y = newPosy
        print "at END of updatePositionAndClean:"
        for tile in self.tilesVisited:
            print tile
'''                   
        #raise NotImplementedError

'''
Test cases for Standard Robot class
 CORRECT 
Test: 1 class creation

robot = StandardRobot(RectangularRoom(1,2), 1.0)

Output:

Test: 2 test setRobotPosition

robot = StandardRobot(RectangularRoom(5,8), 1.0)
robot.getRobotPosition()
loop 10 times:
* Generate random x, y values
* Check if Position(x,y) is in the room
* If so, robot.setRobotPosition(Position(x, y))
* robot.getRobotPosition()

Output:

    Random position 0: (3.00, 9.00)
    Random position 1: (6.00, 2.00)
    Random position 2: (1.00, 5.00)
       In room; setting position. Position is now: (1.00, 5.00)
    Random position 3: (4.00, 8.00)
    Random position 4: (3.00, 6.00)
       In room; setting position. Position is now: (3.00, 6.00)
    Random position 5: (6.00, 9.00)
    Random position 6: (3.00, 6.00)
       In room; setting position. Position is now: (3.00, 6.00)
    Random position 7: (0.00, 4.00)
       In room; setting position. Position is now: (0.00, 4.00)
    Random position 8: (5.00, 5.00)
    Random position 9: (2.00, 1.00)
       In room; setting position. Position is now: (2.00, 1.00)

Test: 3 test setRobotDirection

robot = StandardRobot(RectangularRoom(5,8), 1.0)
robot.getRobotDirection()
loop 10 times:
* Generate random direction value
* robot.setRobotDirection(randDirection)
* robot.getRobotDirection()

Output:

    Random direction: 245
      Setting direction. Direction is now: 245
    Random direction: 187
      Setting direction. Direction is now: 187
    Random direction: 68
      Setting direction. Direction is now: 68
    Random direction: 123
      Setting direction. Direction is now: 123
    Random direction: 263
      Setting direction. Direction is now: 263
    Random direction: 189
      Setting direction. Direction is now: 189
    Random direction: 66
      Setting direction. Direction is now: 66
    Random direction: 73
      Setting direction. Direction is now: 73
    Random direction: 304
      Setting direction. Direction is now: 304
    Random direction: 162
      Setting direction. Direction is now: 162

Test: 4 test updatePositionAndClean

Test StandardRobot.updatePositionAndClean()

Output:

    Creating room and robot...
    Setting position and direction to Position(1.5, 2.5) and 90...
    Calling updatePositionAndClean(); robot speed is 1.0
    Passed; now calling updatePositionAndClean() 20 times
    Passed test.

Test: 5 test updatePositionAndClean

Test StandardRobot.updatePositionAndClean()

Output:

    Creating randomly sized room: 8x7 - and robot at speed 0.85...
    Robot initalized at random position
    Was initial position cleaned? True
    Robot initalized at random direction:
    Number of cleaned tiles: 1

    Calling updatePositionAndClean() 30 times...
    Cleaned the minimum number of tiles; test passed.
'''
robot = StandardRobot(RectangularRoom(5,8), 1.0)
print "starting Standard Robot Test"
for i in range(0,50):
    #print "updatePositionAndClean() - iteration " + str(i)
    robot.updatePositionAndClean()
print "finished Standard Robot Test"
