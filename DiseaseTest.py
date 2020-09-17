#!/usr/bin/env python
# coding: UTF-8
#
##  @package WorldTest
#   @author Jefferson Peralva Machiqueira
#   @date 31/08/2020

import unittest
from World import World
from Disease import Disease

##
 # Class for testing Disease.Disease class
 # @author Jefferson Peralva Machiqueira
class ActorTest(unittest.TestCase):
    ##
    # Generate World and disease for testing purposes
    def setUp(self):
        self.world_one = World(10, 15)
        self.disease_one = Disease()
        self.world_one.addObject(self.disease_one, 5, 10)

    def test_constructor(self):
        self.assertEqual(self.disease_one.getGrowthCondition(), (0, 0, 0))

    def test_getStrenght(self):
        self.assertEqual(self.disease_one.getStrength(), 1)

    def test_getQuadrant(self):
        self.assertEqual(self.disease_one.getQuadrant(), 3)

    def test_setStrength(self):
        self.disease_one.setStrength(2)
        self.assertEqual(self.disease_one.getStrength(), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)