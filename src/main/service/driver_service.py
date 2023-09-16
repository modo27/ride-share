from src.main.models.driver import Driver


class DriverService:
    @classmethod
    def add_driver_service(cls, arguments):
        driver = Driver(arguments[0], arguments[1], arguments[2])
        return driver
