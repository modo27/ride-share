import math


class Ride:

    BASE_FARE = 50
    FARE_PER_KM = 6.5
    FARE_PER_MIN = 2
    SERVICE_TAX = 0.2

    def __init__(self, ride_id, driver_id, rider_id, source_x_coord, source_y_coord):
        self.__ride_id = ride_id
        self.__driver_id = driver_id
        self.__rider_id = rider_id
        self.__source_x_coord = int(source_x_coord)
        self.__source_y_coord = int(source_y_coord)
        self.__dest_x_coord = None
        self.__dest_y_coord = None
        self.__time_taken = None
        self.__status = 0  # 0 denotes started, 1 denotes ended

    def stop_ride(self, dest_x_coord, dest_y_coord, time_taken):
        self.__dest_x_coord = int(dest_x_coord)
        self.__dest_y_coord = int(dest_y_coord)
        self.__time_taken = int(time_taken)
        self.__status = 1

    def get_bill(self):
        dist_travelled = round(
            math.sqrt(
                (self.__dest_x_coord - self.__source_x_coord) ** 2 + (self.__dest_y_coord - self.__source_y_coord) ** 2
            ),
            2,
        )
        net_bill = self.BASE_FARE + (dist_travelled * self.FARE_PER_KM) + (self.__time_taken * self.FARE_PER_MIN)
        total_bill = net_bill + round(self.SERVICE_TAX * net_bill, 2)
        return format(total_bill, ".2f")

    @property
    def status(self):
        return self.__status

    @property
    def driver_id(self):
        return self.__driver_id
