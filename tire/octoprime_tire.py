from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tires) -> None:
        self.tires = tires

    def tire_needs_service(self):
        sum = 0
        for i in self.tires:
            sum += i
        if sum >= 3:
            return True
        else:
            return False