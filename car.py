# class Car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year

#     def descriptive_name(self):
#         description=self.make + ' ' + self.model + ' ' + str(self.year)
#         return description
    
# cars=Car("Altroz","XM PLUS",2019)
# print(cars.descriptive_name())

'''
Setting a Default Value for an Attribute:Odometer Reading

'''

class Car:

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading= 0

    def descriptive_name(self):
        description=self.make + ' ' + self.model + ' ' + str(self.year)
        return description
    
    def odometer_read(self):
        print(f"The odometer reading for the above car is {str(self.odometer_reading)} miles/hour")
    
cars=Car("Mahindra","XM PLUS",2019)
cars=Car("Hyundai","Exter",2023)
print(cars.descriptive_name())
cars.odometer_read()
