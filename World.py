#!/usr/bin/env python
# coding: UTF-8
#
##  @package World
#   @author Jefferson Peralva Machiqueira
#   @date 31/08/2020

from sys import exit
from Actor import Actor
from typing import List
from Constants import MAXIMUM_HEIGHT, MAXIMUM_WIDTH, DEPTH

## Type definition for use in Python Type Hinting for Grid/3D-list
Grid = List[List[List[int or None or Actor]]]
## Type definition for use in Python Type Hinting for ArrayActor/list-of-actor-instances
ArrayActor = List[Actor]


##
 # Class for holding Actor objects in cells of a grid in the world.
 # The world is represented by a 2 dimensional array of cells,
 # with the specified width and height. One cell
 # can keep at most 5 Actor objects.
 # @author Jefferson Peralva Machiqueira
class World:
    ##
    # Constructor.
    # Creates a world with the given width and height.
    # @param int world_width Width in number of cells
    # @param int world_height Height in number of cells
    #
    def __init__(self, worldWidth: int, worldHeight: int):
        if worldWidth <= 0 or worldWidth > MAXIMUM_WIDTH:
            worldWidth = MAXIMUM_WIDTH
        if worldHeight <= 0 or worldHeight > MAXIMUM_HEIGHT:
            worldHeight = MAXIMUM_HEIGHT
        ## Private instance attribute width
        self.__width = worldWidth
        ## Private instance attribute height
        self.__height = worldHeight
        ## Private instance attribute depth
        self.__depth = DEPTH
        ## Private instance attribute grid
        self.__grid = self.createGrid(self.__height, self.__width, self.__depth)
        ## Private instance attribute objCounter
        self.__objCounter = 0

    ## Initializes each object of the array as None.
     #
     # @param h grid height.
     # @param w grid width.
     # @param d grid depth.
     # @return grid.
     # PS.: This method could be static, but I was oriented to keep the
     # professor proposed skeleton
    def createGrid(self, h: int, w: int, d: int) -> Grid:
        return [[[None]*d for _ in range(w)] for _ in range(h)]

    ## Return a string representation of the grid.
     # List by width. Each slice is height x depth.
     #
     # @return str string with the grid.
     #
    def __str__(self) -> str:
        gstr = f'Grid is {self.__height} x {self.__width} x {self.__depth}\n\n'
        for i, x in enumerate(self.__grid):
            gstr += f'width {i}\n'
            gstr += '\n'.join([' '.join([' '.join(str('*' if z is None else z.getID())) for z in y]) for y in x]) + '\n\n'
        return gstr

    ## Return a string representation of the grid.
     # List by depth. Each slice is height x width.
     #
     # @return str string with the grid.
     #
    def __repr__(self):
        g = self.__grid
        h = self.__height
        w = self.__width
        d = self.__depth
        gstr = f'Grid is {h} x {w} x {d}\n\n'
        for z in range(d):
            gstr += f'depth {z}\n'
            for y in range(h):
                for x in range(w):
                    o = g[y][x][z]
                    gstr += str('*' if o is None else o.getID()) + ' '
                gstr += '\n'
            gstr += '\n'
        return gstr

    ##
     # Blank method body.
     # Overriden in subclasses as appropriate
     #
    def act(self):
        pass

    ##
     # Adds a new actor to this world at a given position.
     # @param Actor obj
     # @param int x width
     # @param int y height
     # @return int Number of objects in that cell
     # @throws SyntaxError when already max number of objects are in that cell
     # @throws ValueError if x or y is not in the valid range
     # @throws NameError if the object is null
     #
    def addObject(self, obj: Actor, x: int, y: int) -> int:
        if obj is None:
            raise NameError('The object is null')
        if x < 0 or x >= self.__width or y < 0 or y >= self.__height:
            raise ValueError('x or y is not in the valid range')
        if not any(value is None for value in self.__grid[y][x]):
            raise SyntaxError(f'Max number of objects are already in cell [{x}, {y}]')
        index = self.__grid[y][x].index(None)
        self.__grid[y][x][index] = obj
        self.__objCounter += 1
        obj.addedToWorld(self)
        obj.setLocation(x, y)
        return index + 1

    ##
     # Height getter
     # @return int Returns the world height.
     #
    def getHeight(self) -> int:
        return len(self.__grid)

    ##
     # Width getter
     # @return int Returns the world width.
     #
    def getWidth(self) -> int:
        return len(self.__grid[0])

    ##
     # Depth getter
     # @return int Returns the world depth.
     #
    def getDepth(self) -> int:
        return len(self.__grid[0][0])

    ##
     # Grid getter
     # @return Grid Returns the grid.
     #
    def getGrid(self) -> Grid:
        return self.__grid

    ##
     # Returns the total number of objects in this world.
     # @return int Total number of objects in this world.
     #
    def numberOfObjects(self) -> int:
        return self.__objCounter

    ##
     # Returns an array with all Actor objects in this world.
     # @return ArrayActor List[Actor]
     #
    def getObjects(self) -> ArrayActor:
        objects = []
        for h in range(self.__height):
            for w in range(self.__width):
                for instance in self.__grid[h][w]:
                    if isinstance(instance, Actor):
                        objects.append(instance)
        return objects

    ## todo implement set_grid()
     #
     #  It checks if aGrid is a 3D array with the same positive length in each dimension.
     #  If so, it sets the grid to aGrid and the other private fields of class World to 
     #  the dimension lengths of aGrid and numObjs.
     #
     #  Note that some checks are omitted. For example, no check is performed to make sure
     #  that numObjs is consistent with the number of Actor objects in aGrid.
     #
     #  Each Actor object in aGrid has to be set to this World object.
     #
     #  @param aGrid reference to a 3D array of Actor objects.
     #
     #  @param numObjs the number of Actor objects in aGrid.
     #
     #  @throws ValueError if the length of each dimension is out of range
     #         or 2nd/3rd dimension has different lengths.
     #
    def setGrid(self, aGrid, numObjs):
        pass


def main():
    world = World(7,9)
    print ("Number of objects in cell(4,4) = %d" % world.addObject(Actor(),4,4))
    print ("Number of objects in cell(2,3) = %d" % world.addObject(Actor(),2,3))
    print ("Number of objects in cell(4,4) = %d" % world.addObject(Actor(),4,4))
    print ("Number of objects in cell(4,4) = %d" % world.addObject(Actor(),4,4))
    print(world)
    print("%r" % world)

if __name__ == "__main__":
    exit(main())
