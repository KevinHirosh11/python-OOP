class GrandParents:

    def __init__(self):
        pass

    def LandProperty(slef):
        print("Poperty inherit of Grand Perent.")

class Perent(GrandParents):

    def __init__(self):
        pass

    def HouseProperty(self):
        print("House Property inherit of Perent.")

class Child(Perent):
    def __init__(self):
        pass

    def VehicleProperty(self):
        print("Vehicle Buy form Child.")

    def LandProperty(slef):
        print("Land property convert to the commecial bulding")
    
clare = Child()
clare.LandProperty()
clare.HouseProperty()
clare.VehicleProperty()