from abc import ABC, abstractmethod

class Faculties(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def Show_Faculty(self):
        pass

class BCIFaculty(Faculties):
    def __init__(self, name):
        super().__init__(name)

    def Show_Faculty(self):
        print(f"Faculty Name: {self.name}\n")

