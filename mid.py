from abc import ABC, abstractmethod
#abstractmethod
class Gravity(ABC):
    def __init__(self, name):
        self.Name = name

    @abstractmethod
    def planet_details(self):
        pass

    @abstractmethod
    def star_details(self):
        pass
    
    @abstractmethod
    def calculate_gravity(self):
        pass

class PlanetAndStar(Gravity):
    def __init__(self, name):
        self.Name = name

    def planet_details(self):
        pass

    def star_details(self):
        pass
    
    def calculate_gravity(self):
        pass

class Planet(PlanetAndStar):
    def __init__(self, name, mass, radius):
        super().__init__(name)
        #Encapsulation
        self.__Mass = mass
        self.__Radius = radius

    def planet_details(self):
        print(f"Planet {self.Name} has mass {self.__Mass} kg and radius {self.__Radius} km")

    def calculate_gravity(self):
        super().calculate_gravity()
        G = 6.67430e-11
        gravity = G * self.__Mass / (self.__Radius ** 2)
        return gravity

class Star(PlanetAndStar):
    def __init__(self, name, temperature, luminosity):
        super().__init__(name)
        self.__Temperature = temperature
        self.__Luminosity = luminosity

    def star_details(self):
        print(f"Star {self.Name} has temperature {self.__Temperature} K and luminosity {self.__Luminosity} W")

if __name__ == "__main__":
    #polymorphism
    Planet1 = Planet("Earth", 5.97e24, 6371)
    Planet1.planet_details()
    print("Gravity on Earth:", Planet1.calculate_gravity(), "m/s^2")

    Star1 = Star("Sun", 5778, 3.828e26)
    Star1.star_details()


    