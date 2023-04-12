from my_task2 import Engine, Battery, Serviceable, CapuletEngine
from tire.tire import Tire
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date) -> None:
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def battery_should_be_serviced(self):
        date_which_battery_should_be_serviced_by = self.last_service_date.replace(year=self.last_service_date + 3)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire) -> None:
        self.engine = engine
        self.battery = battery
        self.tire = tire
    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced() or self.tire.tire_needs_service()

class CarFactory():
    # list one car as example, other create methods are similar
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        return Car(CapuletEngine(last_service_mileage, current_mileage),
                   SpindlerBattery(last_service_date, current_date),
                   CarriganTire(tires))