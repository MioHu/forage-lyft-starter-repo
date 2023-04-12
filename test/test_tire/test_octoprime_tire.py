import unittest
from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tires = [0.9, 0.8, 0.9, 0.7]
        tire = OctoprimeTire(tires)
        self.assertTrue(tire.tire_needs_service())

    def test_needs_service_false(self):
        tires = [0.2, 0.2, 0.2, 0.2]
        tire = OctoprimeTire(tires)
        self.assertFalse(tire.tire_needs_service())