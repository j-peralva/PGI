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
 # Class for testing Actor.Actor class
 # @author Jefferson Peralva Machiqueira
class ActorTest(unittest.TestCase):

    ##
     # Generate Worlds for testing purposes
     # This method is used before execution of any other method
     # We are using setUpClass(cls) instead of setUp(self) because
     # in this case, because of Actor ID, we want to setUp only once
     # not everytime a method is called by unittest.main()
    @classmethod
    def setUpClass(cls):
        cls.world_one = World(7, 9)
        cls.world_two = World(10, 15)
        cls.actor_one = Actor()
        cls.actor_two = Actor()
        cls.actor_three = Actor()
        cls.world_two.addObject(cls.actor_two, 5, 10)

    # Test the constructor
    def test_constructor(self):
        self.assertEqual(self.actor_one.getX(), 0)
        self.assertEqual(self.actor_one.getY(), 0)
        self.assertIsNone(self.actor_one.getWorld())
        self.assertEqual(self.actor_one.getID(), 0)
        self.assertEqual(self.actor_two.getID(), 1)
        self.assertEqual(self.actor_one.Iteration(), 0)
        self.assertEqual(self.actor_two.Iteration(), 0)

    # Test the Actor.setLocation method
    def test_setLocation(self):
        self.assertEqual(self.actor_two.getX(), 5)
        self.assertEqual(self.actor_two.getY(), 10)
        with self.assertRaises(RuntimeError):
            self.actor_one.setLocation(6, 5)
        with self.assertRaises(ValueError):
            self.actor_two.setLocation(10, 5)
        with self.assertRaises(ValueError):
            self.actor_two.setLocation(6, 15)
        with self.assertRaises(ValueError):
            self.actor_two.setLocation(0, -1)
        with self.assertRaises(ValueError):
            self.actor_two.setLocation(-1, 5)
        self.actor_two.setLocation(0, 0)
        self.assertEqual(self.actor_two.getX(), 0)
        self.assertEqual(self.actor_two.getY(), 0)

    # Test the Actor.getWorld method
    def test_getWorld(self):
        self.assertIsNotNone(self.actor_two.getWorld())
        self.assertIsNone(self.actor_one.getWorld())

    # Test the Actor.addedtoWorld method
    def test_addedtoWorld(self):
        self.assertIsNone(self.actor_three.getWorld())
        self.actor_three.addedToWorld(self.world_one)
        self.assertIsNotNone(self.actor_three.getWorld())
        self.assertEqual(self.actor_three.getX(), 0)
        self.assertEqual(self.actor_three.getX(), 0)
        self.actor_three.setLocation(1, 1)
        self.assertEqual(self.actor_three.getX(), 1)
        self.assertEqual(self.actor_three.getX(), 1)
        with self.assertRaises(ValueError):
            self.actor_three.setLocation(7, 5)
        with self.assertRaises(ValueError):
            self.actor_three.setLocation(6, 9)
        with self.assertRaises(ValueError):
            self.actor_three.setLocation(0, -1)
        with self.assertRaises(ValueError):
            self.actor_three.setLocation(-1, 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)