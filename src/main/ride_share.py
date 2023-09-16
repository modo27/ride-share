from src.main.constants import ADD_DRIVER, ADD_RIDER, BILL, MATCH, START_RIDE, STOP_RIDE
from src.main.service.driver_service import DriverService
from src.main.service.ride_service import RideService
from src.main.service.rider_service import RiderService


class RideShare:
    def __init__(self):
        self.__drivers = {}
        self.__riders = {}
        self.__rides = {}

    def parse_and_execute_command(self, command, arguments):
        if command == ADD_DRIVER:
            self.__drivers[arguments[0]] = DriverService.add_driver_service(arguments)
        elif command == ADD_RIDER:
            self.__riders[arguments[0]] = RiderService.add_rider_service(arguments)
        elif command == MATCH:
            RiderService.match_service(self.__riders[arguments[0]], self.__drivers.values())
        elif command == START_RIDE:
            RideService.start_ride_service(self.__riders, self.__rides, arguments)
        elif command == STOP_RIDE:
            RideService.stop_ride_service(self.__rides, self.__drivers, arguments)
        elif command == BILL:
            RideService.get_bill_service(self.__rides, arguments)
