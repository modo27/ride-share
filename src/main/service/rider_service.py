from src.main.models.rider import Rider


class RiderService:
    @classmethod
    def add_rider_service(cls, arguments):
        rider = Rider(arguments[0], arguments[1], arguments[2])
        return rider

    @classmethod
    def match_service(cls, rider, drivers):
        rider.match_drivers(drivers)
        matched_drivers = rider.matched_drivers
        if len(matched_drivers) > 0:
            output = "DRIVERS_MATCHED"
            for val in matched_drivers.values():
                output += " {}".format(val.id)
            print(output)
        else:
            print("NO_DRIVERS_AVAILABLE")
