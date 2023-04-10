from abc import abstractmethod
from datetime import datetime

# engine
class Engine:
    @abstractmethod
    def engine_should_be_serviced():
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage) -> None:
        super().__init__()
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage) -> None:
        super().__init__()
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        super().__init__()
        self.warning_light_is_on = warning_light_is_on
    def engine_should_be_serviced(self):
        return self.warning_light_is_on


# battery
class Battery:
    @abstractmethod
    def battery_should_be_serviced():
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
    def battery_should_be_serviced(self):
        return self.last_service_date.year + 2 < self.current_date

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
    def battery_should_be_serviced(self):
        return self.last_service_date.year + 4 < self.current_date


# car
class Serviceable():
    @abstractmethod
    def needs_service():
        pass

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery) -> None:
        super().__init__()
        self.engine = engine
        self.battery = battery
    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced()

class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(last_service_mileage, current_mileage),
                   SpindlerBattery(last_service_date, current_date))
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage),
                   SpindlerBattery(last_service_date, current_date))
    def create_palindrome(self, current_date, last_service_date, warning_light_is_on):
        return Car(SternmanEngine(warning_light_is_on),
                   SpindlerBattery(last_service_date, current_date))
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage),
                   NubbinBattery(last_service_date, current_date))
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(last_service_mileage, current_mileage),
                   NubbinBattery(last_service_date, current_date))



