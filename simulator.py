# coding: UTF-8
#
##  @package simulator
#   @author Jefferson Peralva Machiqueira
#   @date 31/08/2020

from sys import argv
from MyWorld import MyWorld
from World import World
from Actor import Actor

##
# This is the main method that sets up a virtual world
# and simulates the gowth of the diseases in the world
# if the number of iterations is given in the comand line
# argument, run the simulation for that number of iterations
# Otherwise, use the deafault number of iterations: 5.
# @author Jefferson Peralva Machiqueira
# @date 31/08/2020
def main(args = None):
    numItr = 5
    if len(args) > 1:
        numItr = args[1]
    print('Simulation of MyWorld')
    world = MyWorld()
    for i in range(numItr):
        world.act()
        objects = world.getObjects()
        for each in objects:
            each.act()
    print('Simulation of World')
    world = World(100, 100)
    world.addObject(Actor(), 10, 10)
    world.addObject(Actor(), 90, 90)
    for i in range(numItr):
        world.act()
        objects = world.getObjects()
        for each in objects:
            each.act()


if __name__ == '__main__':
    main(argv)
