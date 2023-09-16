class Driver:
    def __init__(self, driver_id, x_coord, y_coord):
        self.__driver_id = driver_id
        self.__x_coord = int(x_coord)
        self.__y_coord = int(y_coord)
        self.__available = True

    def __get_status(self):
        return self.__available

    def __set_status(self, available):
        self.__available = available

    @property
    def id(self):
        return self.__driver_id

    @property
    def x_coord(self):
        return self.__x_coord

    @property
    def y_coord(self):
        return self.__y_coord

    status = property(__get_status, __set_status)
