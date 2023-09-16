import math


class Rider:
    def __init__(self, rider_id, x_coord, y_coord):
        self.__rider_id = rider_id
        self.__x_coord = int(x_coord)
        self.__y_coord = int(y_coord)
        self.__matches = {}

    def match_drivers(self, drivers):
        available_drivers = filter(lambda item: item.status, drivers)
        distance_vs_drivers = dict(
            filter(
                lambda item: item[1] <= 5,
                {
                    driver: math.sqrt((self.__x_coord - driver.x_coord) ** 2 + (self.__y_coord - driver.y_coord) ** 2)
                    for driver in available_drivers
                }.items(),
            )
        )
        sorted_drivers_by_dist = sorted(distance_vs_drivers.items(), key=lambda x: (x[1], x[0].id))
        for i in range(min(len(sorted_drivers_by_dist), 5)):
            self.__matches[i + 1] = sorted_drivers_by_dist[i][0]

    @property
    def x_coord(self):
        return self.__x_coord

    @property
    def y_coord(self):
        return self.__y_coord

    @property
    def matched_drivers(self):
        return self.__matches
