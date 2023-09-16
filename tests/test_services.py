import io
import unittest

from src.main.models.driver import Driver
from src.main.models.ride import Ride
from src.main.models.rider import Rider
from src.main.service.driver_service import DriverService
from src.main.service.ride_service import RideService
from src.main.service.rider_service import RiderService


class TestServices(unittest.TestCase):
    def setUp(self) -> None:
        self.driver_0 = Driver("D1", 2, 3)
        self.driver_1 = Driver("D2", 4, 3)
        self.driver_2 = Driver("D3", -1, 3)
        self.drivers = [self.driver_0, self.driver_1, self.driver_2]
        self.driver_map = {"D1": self.driver_0, "D2": self.driver_1, "D3": self.driver_2}

        self.rider_1 = Rider("R1", 4, 3)
        self.rider_2 = Rider("R2", 8, 1)
        self.rider_3 = Rider("R3", 0, 2)
        self.rider_map = {"R1": self.rider_1, "R2": self.rider_2, "R3": self.rider_3}

        self.ride_1 = Ride("R-001", "D2", "R1", 4, 3)
        self.rides = {"R-001": self.ride_1}
        self.driver_service = DriverService()
        self.rider_service = RiderService()
        self.ride_service = RideService()

    def test_add_driver_service(self):
        driver = self.driver_service.add_driver_service(["D4", 5, 1])
        self.assertEqual(driver.id, "D4")
        self.assertEqual(driver.status, True)
        self.assertEqual(driver.x_coord, 5)
        self.assertEqual(driver.y_coord, 1)

    def test_add_rider_service(self):
        rider = self.rider_service.add_rider_service(["R4", 4, 1])
        self.assertEqual(rider.x_coord, 4)
        self.assertEqual(rider.y_coord, 1)
        self.assertEqual(len(rider.matched_drivers), 0)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_match_service(self, mock_stdout):
        self.rider_service.match_service(self.rider_1, self.drivers)
        expected_output = "DRIVERS_MATCHED D2 D1 D3\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_add_ride_service(self):
        ride = self.ride_service.add_ride_service("R-002", "D2", "R1", 4, 3)
        self.assertEqual(ride.status, 0)
        self.assertEqual(ride.driver_id, "D2")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_ride_id_already_exists(self, mock_stdout):
        self.ride_service.start_ride_service(self.rider_map, self.rides, ["R-001", 2, "R1"])
        expected_output = "INVALID_RIDE\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_driver_seq_does_not_exist(self, mock_stdout):
        self.rider_service.match_service(self.rider_2, self.drivers)
        self.ride_service.start_ride_service(self.rider_map, self.rides, ["R-002", 4, "R2"])
        expected_output = "INVALID_RIDE\n"
        self.assertTrue(expected_output in mock_stdout.getvalue())

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_start_ride_service(self, mock_stdout):
        self.rider_service.match_service(self.rider_3, self.drivers)
        self.ride_service.start_ride_service(self.rider_map, self.rides, ["R-002", 1, "R3"])
        expected_output = "RIDE_STARTED R-002\n"
        self.assertTrue(expected_output in mock_stdout.getvalue())

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_stop_ride_service_when_ride_id_does_not_exist(self, mock_stdout):
        self.ride_service.stop_ride_service(self.rider_map, self.driver_map, ["R-004", 1, 5, 32])
        expected_output = "INVALID_RIDE\n"
        self.assertTrue(expected_output in mock_stdout.getvalue())

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_stop_ride_service_when_ride_already_stopped(self, mock_stdout):
        self.ride_service.stop_ride_service(self.rider_map, self.driver_map, ["R-001", 1, 5, 32])
        self.ride_service.stop_ride_service(self.rider_map, self.driver_map, ["R-001", 1, 5, 32])
        expected_output = "INVALID_RIDE\n"
        self.assertTrue(expected_output in mock_stdout.getvalue())

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_successful_stop_ride_service(self, mock_stdout):
        self.ride_service.stop_ride_service(self.rides, self.driver_map, ["R-001", 1, 5, 32])
        expected_output = "RIDE_STOPPED R-001\n"
        self.assertTrue(expected_output in mock_stdout.getvalue())

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_get_bill_service(self, mock_stdout):
        self.ride_service.stop_ride_service(self.rides, self.driver_map, ["R-001", 1, 5, 32])
        self.ride_service.get_bill_service(self.rides, ["R-001"])
        expected_output = "BILL R-001 D2 164.96\n"
        self.assertTrue(expected_output in mock_stdout.getvalue())
