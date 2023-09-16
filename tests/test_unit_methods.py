import unittest

from src.main.models.driver import Driver
from src.main.models.ride import Ride
from src.main.models.rider import Rider


class TestUnitMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.driver_0 = Driver("D1", 2, 3)
        self.driver_1 = Driver("D2", 4, 3)
        self.driver_2 = Driver("D3", -1, 3)
        self.drivers = [self.driver_0, self.driver_1, self.driver_2]

        self.rider_1 = Rider("R1", 4, 3)
        self.rider_2 = Rider("R2", 8, 1)
        self.rider_3 = Rider("R3", 0, 2)

        self.ride_1 = Ride("R-001", "D1", "R1", 4, 3)

    def test_get_driver_id_0(self):
        driver_id = self.driver_0.id
        self.assertTrue(driver_id == "D1")

    def test_get_driver_status(self):
        driver_status = self.driver_1.status
        self.assertTrue(driver_status)

    def test_driver_status_setter_and_getter(self):
        driver_status = self.driver_1.status
        self.assertTrue(driver_status)
        self.driver_1.status = False
        driver_status = self.driver_1.status
        self.assertFalse(driver_status)

    def test_get_driver_x_coord(self):
        x_coord = self.driver_1.x_coord
        self.assertEqual(x_coord, 4)

    def test_get_driver_y_coord(self):
        y_coord = self.driver_2.y_coord
        self.assertEqual(y_coord, 3)

    def test_get_rider_x_coord(self):
        x_coord = self.rider_1.x_coord
        self.assertEqual(x_coord, 4)

    def test_get_rider_y_coord(self):
        y_coord = self.rider_1.y_coord
        self.assertEqual(y_coord, 3)

    def test_match_drivers(self):
        self.rider_1.match_drivers(self.drivers)
        matches = self.rider_1.matched_drivers
        self.assertEqual(len(matches.keys()), 3)

    def test_get_ride_status(self):
        status = self.ride_1.status
        self.assertEqual(status, 0)

    def test_get_ride_driver_id(self):
        driver_id = self.ride_1.driver_id
        self.assertEqual(driver_id, "D1")

    def test_get_bill(self):
        self.ride_1.stop_ride(9, 5, 23)
        bill = self.ride_1.get_bill()
        self.assertEqual(bill, "157.25")
