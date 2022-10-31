class Car:
    """
    Car modela un coche con reudas y motor
    """
    def __init__(self,engine='motor',tires='estandar'):
        self.engine=engine
        self.tires=tires

    def description(self):
        print(f"Un coche con {self.engine} y {self.tires}")

