import unittest

from models.gymclass import GymClass

class TestGymClass(unittest.TestCase):
    def setUp(self):
        self.gymclass_1 = GymClass("Yoga", "12:00", 30, "Yoga Class!")