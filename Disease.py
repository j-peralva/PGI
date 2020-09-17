# coding: UTF-8
#
##  @package Disease
#   @author Jefferson Peralva Machiqueira
#   @date 31/08/2020

from Actor import Actor
from IDisease import IDisease

##
 # This Disease class is a sub-class of the Actor class.
 # 
 # @author Jefferson Peralva Machiqueira
 # @date 31/08/2020
 #
 #
class Disease (Actor, IDisease):

    ##
     # Constructor.
     # - Call its superclass’s default constructor.
     # - Initialize the lower bound and the upper bound temperatures for the
     #   growth rate to 0.
     # - Set the growth rate to 0.
     # - Set the disease strength to 1.
     #          
    def __init__(self):
        super(Disease, self).__init__()
        ### Rate at which the disease grows when subjected to the appropriate temperature range.    
        self.__growthRate = 0.0
        ### Minimum temperature for the disease development.
        self.__lowerTemp = 0.0
        ### Maximum temperature for the disease development.
        self.__higherTemp = 0.0
        ### Disease strength.
        self.__dStrength = 1.0

    ##
     # Sets the disease growth rate, lower temperature and higher temperature.
     #
     # @param float lTemp Lower bound temperature for the disease to grow at this gRate.
     # @param float hTemp Upper bound temperature for the disease to grow at this gRate.
     # @param float gRate The growth rate.
     #
    def setGrowthCondition(self, lTemp: float, hTemp: float, gRate: float):
        self.__growthRate = gRate
        self.__lowerTemp = lTemp
        self.__higherTemp = hTemp

    ##
     # Returns the disease growth rate, lower temperature and higher temperature.
     #
     # @return growth rate, lower temp and higher temp
     #
    def getGrowthCondition(self) -> tuple:
        return self.__growthRate, self.__lowerTemp, self.__higherTemp

    ## Returns the quadrant of this disease.
     # 
     # @return 0, 1, 2 or 3.
     #
    def getQuadrant(self) -> int:
        width = self.getWorld().getWidth()
        height = self.getWorld().getHeight()
        yAxis = width//2 - 1
        xAxis = height//2 - 1
        if self.getX() <= yAxis and self.getY() <= xAxis:
            return 0
        elif self.getX() > yAxis and self.getY() <= xAxis:
            return 1
        elif self.getX() <= yAxis and self.getY() > xAxis:
            return 2
        elif self.getX() > yAxis and self.getY() > xAxis:
            return 3
        
    ##
     # Print on screen in the format "Iteration <ID>: Actor <Actor ID>." 
     # The @f$<ID>@f$ is replaced by the current iteration number. 
     # @f$<Actor ID>@f$ is replaced by the unique ID of the Actor object that performs 
     # the act() method. 
     #
    def act(self):
        print(f'Iteration {Actor.Iteration(self)}: {Actor.getID(self)}')
        conditions = self.getGrowthCondition()
        temp = self.getWorld().getTemp(self.getQuadrant())
        if temp <= conditions[2] and temp >= conditions[1]:
            self.__dStrength *= conditions[0]
        Actor.nextIteration(self)

    
    ##
     # Return the disease strength of this object.
     #
     # @return disease strength of the object.
     #
    def getStrength(self):
        return self.__dStrength

    ##
    # Set Strength
    # @param float strength
    def setStrength(self, strength):
        self.__dStrength = strength

    ##
     # Return a string with the strength, growth and quadrant of this disease.
     #
    def __str__(self):
        st = super(Disease,self).__str__()
        st +='strength = %f\n' % self.getStrength()
        st += 'growth = %f, %f, %f\n' % self.getGrowthCondition()
        st += 'quadrant = %d, temp = %d\n' % (self.getQuadrant(),self.getWorld().getTemp(self.getQuadrant()))
        return st
