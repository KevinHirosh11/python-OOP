from abc import ABC, abstractmethod

class Campus(ABC):
    def __init__(self, about, location, contact):
        self.about = about
        self.location = location
        self.contact = contact

    @abstractmethod
    def show_campus_info(self):
        pass

class BCICampus(Campus):
    def __init__(self, about, location, contact):
        super().__init__(about, location, contact)

    def show_campus_info(self):
        print(f"About: {self.about}\nLocation: {self.location}\nCampus Contact: {self.contact}\n")

