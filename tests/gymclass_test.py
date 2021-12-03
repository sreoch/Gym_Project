import unittest

from models.gymclass import GymClass

class TestGymClass(unittest.TestCase):
    def setUp(self):
        self.gymclass_1 = GymClass("Yoga", "12:00", 30, "Yoga Class!")

    def test_gymclass_has_name(self):
        self.assertEqual("Yoga", self.gymclass_1.activity_name)
    
    def test_gymclass_has_start_time(self):
        self.assertEqual("12:00", self.gymclass_1.start_time)

    def test_gymclass_has_duration(self):
        self.assertEqual(30, self.gymclass_1.duration)

    def test_gymclass_has_description(self):
        self.assertEqual("Yoga Class!", self.gymclass_1.description)