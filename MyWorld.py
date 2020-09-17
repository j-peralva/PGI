# coding: UTF-8
#
##  @package MyWorld
#   @author Jefferson Peralva Machiqueira
#   @date 31/08/2020

from World import World
from IWorld import IWorld
from Disease import Disease
from sys import exit
from typing import List

## Type definition for use in Python Type Hinting for ArrayDisease/list-of-disease-instances
ArrayDisease = List[Disease]

##
 # SubClass of World and IWorld classes
 # @author Jefferson Peralva Machiqueira
class MyWorld(World, IWorld):

    __quadID = (0, 1, 2, 3)

    ##
     # Call the constructor of the World with the width and height
    def __init__(self, w: int = 720, h: int = 640):
        super().__init__(w, h)
        self.__temperature = None
        self.__itCounter = 0
        self.prepare()

    ##
     # Prepare the world. Open a text file named
     # "simulation.config" in the current path
     # Parse the configuration for the number of
     # disease objects, the cell locations of these objects,
     # the gowth rates, and the temperature ranges associates
     # with individual gowth rates
     #
    def prepare(self):
        lines = []
        try:
            arq = open("simulation.config", "r")
            lines = arq.readlines()
        except FileNotFoundError:
            print('Terminating the program.')
            exit(-1)
        else:
            arq.close()
        lines = [line.rstrip('\n').split('=').pop(1) for line in lines]
        disArray = self.initDiseases(int(lines[0]))
        aux = self.initGrowthConditions(lines[2], disArray)
        if aux == -1:
            print('Terminating the program.')
            exit(-1)
        aux = self.initTemps(lines[3])
        if aux == -1:
            print('Terminating the program.')
            exit(-1)
        aux = self.initLocations(lines[1], disArray)
        if aux == -1:
            print('Terminating the program.')
            exit(-1)
        self.setTemp(self.__quadID, self.__temperature)

    ##
    # Create Disease objects
    # @param int numDisStr
    # @return array of diseases
    def initDiseases(self, numDisStr: int) -> ArrayDisease:
        return [Disease() for _ in range(numDisStr)]

    ##
    # Create gowth conditions
    # @param str growthStr
    # @param ArrayDiseases diseaseArr
    # @return int
    def initGrowthConditions(self, growthStr: str, diseaseArr: ArrayDisease) -> int:
        growthStr = growthStr.strip()
        if growthStr == '' or not isinstance(growthStr, str):
            print('Check the DiseasesGrowth line in simulation.config')
            return -1
        growthStr = growthStr.split(';')
        growthStr = [value.split(',') for value in growthStr]
        if len(growthStr) != len(diseaseArr):
            print('Check the DiseasesGrowth line in simulation.config')
            return -1
        for value in growthStr:
            if len(value) != 3:
                print('Check the DiseasesGrowth line in simulation.config')
                return -1
        for ind in range(len(diseaseArr)):
            diseaseArr[ind].setGrowthCondition(float(growthStr[ind][0]), float(growthStr[ind][1]), float(growthStr[ind][2]))
        return 0

    ##
    # Create Temperatures
    # @param str tempStr
    # @return int
    def initTemps(self, tempStr: str) -> int:
        tempStr = tempStr.split(';')
        tempStr = [float(value) for value in tempStr]
        if len(tempStr) != 4:
            print('Check the Temperature line in simulation.config')
            return -1
        self.__temperature = {key: value for key, value in enumerate(tempStr)}
        return 0

    ##
    # setup all diseases in MyWorld
    # @param str locationsStr
    # @param diseaseArr
    def initLocations(self, locationsStr: str, diseaseArr: ArrayDisease) -> int:
        locationsStr = locationsStr.split(';')
        if len(locationsStr) != len(diseaseArr):
            print('Check the Locations line in simulation.config')
            return -1
        locationsStr = [value.split(',') for value in locationsStr]
        for coordinate in locationsStr:
            if len(coordinate) != 2:
                print('Check the Locations line in simulation.config')
                return -1
        for ind in range(len(diseaseArr)):
            self.addObject(diseaseArr[ind], int(locationsStr[ind][0]), int(locationsStr[ind][1]))
        return 0

    ##
    # Return the total disease strenght of all diseases
    # @return float
    def getSumStrength(self) -> float:
        objects = self.getObjects()
        value = 0
        for obj in objects:
            value += obj.getStrength()
        return value

    ##
    # Return the temperature of the region with the ID of quadID
    # @param int quadID
    # @return float with the temperature of ID
    def getTemp(self, quadID: int) -> float:
        return self.__temperature[quadID]

    ##
    # Set temperature of quadID quadrant
    # @param int quadID
    # @param dict temp
    def setTemp(self, quadID: tuple, temp: float):
        self.__temperature[quadID] = temp

    ##
    # Overrides the method act in the world class
    def act(self):
        print(f'Iteration {self.__itCounter}: World disease strenght is {self.getSumStrength()}')
        self.__itCounter += 1


if __name__ == '__main__':
    valor = MyWorld(720, 640)
    valor.act()
    print(valor.getTemp(0), valor.getTemp(1), valor.getTemp(2), valor.getTemp(3))
    objetos = valor.getObjects()
    for objeto in objetos:
        print(objeto.getX(), objeto.getY(), objeto.getGrowthCondition(), objeto.getQuadrant())
        objeto.act()
