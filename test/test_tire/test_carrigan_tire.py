import unittest
from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tires = [0.1, 0.5, 0.9, 0.98]
        tire = CarriganTire(tires)
        self.assertTrue(tire.tire_needs_service())


    def test_needs_service_false(self):
        tires = [0.25, 0.2, 0.3, 0.28]
        tire = CarriganTire(tires)
        self.assertFalse(tire.tire_needs_service())