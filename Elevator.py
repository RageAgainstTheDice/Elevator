class Elevator:
    def __init__(self, name, number, current_floor):
        self.name = name
        self.number = number
        self.current_floor = current_floor

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_current_floor(self):
        return self.current_floor

    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

    def set_current_floor(self, current_floor):
        self.current_floor = current_floor
