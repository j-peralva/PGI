#!/usr/bin/env python
# coding: UTF-8
#
## @package Actor
#  @author Jefferson Peralva Machiqueira
#  @date 31/08/2020


##
 # Actor class, which is the base class for Disease objects.
 # 
 # @author Jefferson Peralva Machiqueira
 #
class Actor:
    ### Holds the value of the next "free" id.
    __ID = 0

    ##
     # Construct a new Actor object. 
     # - Sets the initial values of its member variables.
     # - Sets the unique ID for the object and initializes the reference to the World 
     #   object to which this Actor object belongs to null. 
     # - The ID of the first Actor object is 0. 
     # - The ID gets incremented by one each time a new Actor object is created. 
     # - Sets the iteration counter to zero and initialize the location of the 
     #   object to cell (0,0). 
     #
    def __init__(self):
        ### X coordinate of this actor.
        self.__locX = 0
        ### Y coordinate of this actor.
        self.__locY = 0
        ### World this actor belongs to.
        self.__world = None
        ### Unique identifier for this actor.
        self.__actorID = Actor.__ID
        Actor.__ID += 1
        ### Iteration counter.
        self.__itCounter = 0
        ### World width
        self.__worldWidth = 0
        ### World height
        self.__worldHeight = 0

    ##
     # Used for testing
     # @return ActorID
     #
    def getID(self) -> int:
        return self.__actorID

    ##
     # Used for testing
     # @return number of iterations
     #
    def Iteration(self) -> int:
        return self.__itCounter

    ##
     # Prints on screen in the format "Iteration <ID>: Actor <Actor ID>".
     #
     # The @f$<ID>@f$ is replaced by the current iteration number. @f$<Actor ID>@f$ is
     # replaced by the unique ID of the Actor object that performs the act(self)
     # method. 
     #
     # For instance, the actor with ID 1 shows the following result on
     # the output screen after its act(self) method has been called twice.
     # <PRE>
     # Iteration 0: Actor 1
     # Iteration 1: Actor 1
     # </PRE>
     #  
    def act(self):
        print(f'Iteration {self.Iteration()}: {self.getID()}')
        self.nextIteration()

    ##
     # Sets the cell coordinates of this object.
     # 
     # @param x the column.
     # @param y the row.
     # 
     # @throws 
     #  ValueError when x < 0 or x >= world width,
     # @throws 
     #  ValueError when y < 0 or y >= world height,
     # @throws 
     #  RuntimeError when the world is null.
     #
    def setLocation(self, x: int, y: int):
        if self.__world is None:
            raise RuntimeError('The World is NULL')
        if x < 0 or x >= self.__worldWidth or y < 0 or y >= self.__worldHeight:
            raise ValueError('x or y is not in the valid range')
        self.__locX = x
        self.__locY = y

    ##
     # Sets the world this actor is into.
     # 
     # @param world Reference to the World object this Actor object is added.
     # @throws
     #  RuntimeError when world is null.
     #
    def addedToWorld(self, world: object):
        if world is None:
            raise RuntimeError('The world is NULL')
        self.__world = world
        self.__worldWidth = world.getWidth()
        self.__worldHeight = world.getHeight()

    ##
     # Gets the world this object in into.
     #
     # @return the world this object belongs to
     #
    def getWorld(self) -> object:
        return self.__world

    ##
     # Gets the X coordinate of the cell this actor object is into.
     # 
     # @return the x coordinate of this Actor object.
     #
    def getX(self) -> int:
        return self.__locX
    

    ##
     # Gets the Y coordinate of the cell this actor object is into.
     #
     # @return the y coordinate of this Actor object.
     #
    def getY(self) -> int:
        return self.__locY

    ##
    # Jumps for next iteration
    def nextIteration(self):
        self.__itCounter += 1

    ##
     #  Return a string with this actor ID and position. 
     #
    def __str__(self) -> str:
        try:
           st = "ID = %d "u'\u2192 '.encode('utf-8') % self.getID()
           st += 'position = (%d, %d)\n' % (self.getX(), self.getY())
        except TypeError:
           st = "ID = %d "u'\u2192 ' % self.getID()
           st += 'position = (%d, %d)\n' % (self.getX(), self.getY())
        return st
