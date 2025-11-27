class Father:
    def __init__(self):
        pass
    def fatherProperty(self):
        print("Father's Property")

class mother:
    def __init__(self):
        pass
        
    def motherproperty(self):
        print("Mother's Property")

class child(Father, mother):
    def __init__(self):
        pass
    
    def Property(self):
        print("Child will inherit of Property")
        super().fatherProperty()
        super().motherproperty()
        
chuuty= child()
chuuty.Property()