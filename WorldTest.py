#!/usr/bin/env python
# coding: UTF-8
#
##  @package WorldTest
#   @author Jefferson Peralva Machiqueira
#   @date 31/08/2020

import unittest
from World import World
from Actor import Actor


##
 # Class for testing World.World class
 # @author Jefferson Peralva Machiqueira
class WorldTest(unittest.TestCase):
    ##
     # Generate Worlds for testing purposes
     # This method is used before execution of any other method
    def setUp(self):
        if not self.test_setGrid() or not self.test_largeWorld():
            self.world_one = World(7, 9)
            self.world_two = World(10, 15)

    ##
     # Test initial height and width.
    def test_getWidthandHeight(self):
        self.assertEqual(self.world_one.getWidth(), 7)
        self.assertEqual(self.world_one.getHeight(), 9)
        self.assertEqual(self.world_two.getWidth(), 10)
        self.assertEqual(self.world_two.getHeight(), 15)

    ##
     # Test to see if added object to correct cell.
    def test_addObj(self):
        self.world_one.addObject(Actor(), 6, 5)
        self.assertIsInstance(self.world_one.getGrid()[5][6][0], Actor)
        self.world_one.addObject(Actor(), 6, 5)
        self.assertIsInstance(self.world_one.getGrid()[5][6][1], Actor)
        self.assertIsNone(self.world_one.getGrid()[5][6][2])

    ##
     # Tests to see if the grid is completely initialized as null.
    def test_nullBeginning(self):
        for height in range(len(self.world_one.getGrid())):
            for width in range(len(self.world_one.getGrid()[height])):
                for depth in range(len(self.world_one.getGrid()[height][width])):
                    self.assertIsNone(self.world_one.getGrid()[height][width][depth])

    ##
     # Tests the thrown exceptions of addObject()
    def test_exceptions(self):
        with self.assertRaises(NameError):
            self.world_one.addObject(None, 6, 5)
        with self.assertRaises(ValueError):
            self.world_one.addObject(Actor(), 10, 5)
        with self.assertRaises(ValueError):
            self.world_one.addObject(Actor(), -1, 5)
        with self.assertRaises(ValueError):
            self.world_one.addObject(Actor(), 6, 10)
        with self.assertRaises(ValueError):
            self.world_one.addObject(Actor(), 10, -1)
        with self.assertRaises(SyntaxError):
            for ind in range(6):
                self.world_one.addObject(Actor(), 6, 5)

    ##
     # todo implement
    def test_setGrid(self):
        pass

    ##
     # Sets the world to an illegal size.
    def test_largeWorld(self):
        # Tuple with invalid values
        values = (-1, 1001)
        for value in values:
            world_one = World(value, 5)
            self.assertEqual(1000, world_one.getWidth())
        for value in values:
            world_one = World(5, value)
            self.assertEqual(1000, world_one.getHeight())


if __name__ == '__main__':
    unittest.main(verbosity=2)
