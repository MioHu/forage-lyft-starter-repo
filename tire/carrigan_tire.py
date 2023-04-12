from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tires) -> None:
        self.tires = tires
    
    def tire_needs_service(self):
        for i in self.tires:
            if i >= 0.9:
                return True
        return False