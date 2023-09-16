from src.main.models.ride import Ride


class RideService:
    @classmethod
    def add_ride_service(cls, ride_id, driver_id, rider_id, source_x, source_y):
        ride = Ride(ride_id, driver_id, rider_id, source_x, source_y)
        return ride

    @classmethod
    def parse_start_ride_argument(cls, arguments):
        return arguments[0], int(arguments[1]), arguments[2]

    @classmethod
    def start_ride_service(cls, riders, rides, arguments):
        ride_id, driver_seq, rider_id = cls.parse_start_ride_argument(arguments)

        rider = riders[rider_id]
        matched_drivers = rider.matched_drivers
        if driver_seq not in matched_drivers.keys() or ride_id in rides or matched_drivers[driver_seq].status is False:
            print("INVALID_RIDE")
            return
        driver = matched_drivers[driver_seq]
        ride = cls.add_ride_service(ride_id, driver.id, rider_id, rider.x_coord, rider.y_coord)
        driver.status = False
        if ride:
            rides[ride_id] = ride
            cls.print_start_ride(ride_id)

    @classmethod
    def print_start_ride(cls, ride_id):
        print("RIDE_STARTED {}".format(ride_id))

    @classmethod
    def parse_stop_ride_argument(cls, arguments):
        return arguments[0], arguments[1], arguments[2], arguments[3]

    @classmethod
    def stop_ride_service(cls, rides, drivers, arguments):
        ride_id, dest_x_coord, dest_y_coord, time_taken = cls.parse_stop_ride_argument(arguments)

        if ride_id not in rides.keys() or rides[ride_id].status == 1:
            print("INVALID_RIDE")
            return
        ride = rides[ride_id]
        ride.stop_ride(dest_x_coord, dest_y_coord, time_taken)
        drivers[ride.driver_id].status = True
        cls.print_stop_ride(ride_id)

    @classmethod
    def print_stop_ride(cls, ride_id):
        print("RIDE_STOPPED {}".format(ride_id))

    @classmethod
    def get_bill_service(cls, rides, arguments):
        ride_id = arguments[0]
        try:
            ride = rides[ride_id]
        except KeyError:
            print("INVALID_RIDE")
            return
        ride_status = ride.status
        if ride_status != 1:
            print("RIDE_NOT_COMPLETED")
            return
        cls.print_bill_service(ride_id, ride.get_bill(), ride.driver_id)

    @classmethod
    def print_bill_service(cls, ride_id, bill, driver_id):
        if bill:
            print("BILL {} {} {}".format(ride_id, driver_id, bill))
