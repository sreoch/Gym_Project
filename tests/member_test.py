import unittest

from models.member import Member



class TestMember(unittest.TestCase):
    def setUp(self):
        self.member_1 = Member("Scott", "Reoch", 20, "standard")

    def test_member_has_first_name(self):
        self.assertEqual("Scott", self.member_1.first_name)

    def test_member_has_last_name(self):
        self.assertEqual("Reoch", self.member_1.last_name)

    def test_member_has_age(self):
        self.assertEqual(20, self.member_1.age)

    def test_member_has_membership(self):
        self.assertEqual("standard", self.member_1.membership_type)

    def test_member_can_get_full_name(self):
        self.assertEqual("Scott Reoch", self.member_1.full_name())
