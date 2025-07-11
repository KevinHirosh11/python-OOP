class Building:
    def __init__(self, buildingName, buildingCode, buildingLocation):
        self.BuildingName = buildingName
        self.BuildingCode = buildingCode
        self.BuildingLocation = buildingLocation

building1 = Building("CRK", "B001", "west Campus")
building2 = Building("JBD", "B002", "south Campus")
building3 = Building("LIB", "B003", "central Campus")

buildings = [building1, building2, building3]
for building in buildings:
    print("Building Name: {}\n Building Code: {}\n Building Location: {} \n"
          .format(building.BuildingName, building.BuildingCode, building.BuildingLocation))