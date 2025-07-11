class NonAcademic:
    def __init__(self,cleaningStaff,securityStaff,maintenanceStaff,officeStaff):
        self.cleaningStaff = cleaningStaff
        self.securityStaff = securityStaff
        self.maintenanceStaff = maintenanceStaff
        self.officeStaff = officeStaff

staff1 = NonAcademic("Sunil", "Alice Smith", "Mike Johnson", "David Wilson")
staff2 = NonAcademic("Raj", "Bob Brown", "Sara White", "Laura Lee")
staff3 = NonAcademic("Priya", "Tom Green", "Emma Black", "James Brown")

staffs = [staff1, staff2, staff3]
for staff in staffs:
    print("Cleaning Staff: {}\n Security Staff: {}\n Maintenance Staff: {}\n Office Staff: {} \n"
          .format(staff.cleaningStaff, staff.securityStaff, staff.maintenanceStaff, staff.officeStaff))



