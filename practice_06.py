
"""
Docstring for practice_06

 We have assume that , car rental company has multiple car models. Each car model can be in one of the following states:
 - available
 -rented
- maintenanceMode
"""





class CarRentalSystem:


    def __init__(self,company_name):

        self.company_name = company_name 
        self.cars = {}

    def is_available_this_model(self,car_model):
        return car_model in self.cars 
    
    def is_maintenance_period(self,car_model):


        if not self.is_available_this_model(car_model):
            raise Exception('please ensure that this model is available in this company')
        
        car_info = self.cars[car_model]

        return  car_info['status']=='maintenanceMode'

    def is_rented(self,car_model):

        if not self.is_available_this_model(car_model):
            raise Exception('please ensure that this model is available in this company')
        
        car_info = self.cars[car_model]

        return  car_info['status']=='rented'

    def add_car(self,car_model):

        if self.is_available_this_model(car_model):
            raise Exception("this car model is already exist to this rent store")
        
        self.cars[car_model] = {
            'status': 'available',
            'service_start_date': None,
            'service_end_date': None,
            'customer_name': None,
            'rent_price':None 

        }


    def rent_car(self,car_model,customer_name,rent_price,service_start_date,service_end_date):

        

        if not self.is_available_this_model(car_model):
            raise Exception('please ensure that this model is available in this company')
        
        if self.is_maintenance_period(car_model):
            raise Exception('this car is in maintenance period')
        
        car_info = self.cars[car_model]

        car_info['status'] = 'rented'
        car_info['customer_name'] = customer_name
        car_info['rent_price'] = rent_price
        car_info['service_start_date'] = service_start_date
        car_info['service_end_date'] = service_end_date


    def maintenance_car(self,car_model):

        if not self.is_available_this_model(car_model):
            raise Exception('please ensure that this model is available in this company')
        
        if self.is_rented(car_model):
            raise Exception('During renting period this car can not go to maintenance')
        
        car_info = self.cars[car_model]

        car_info['status'] = 'maintenanceMode'
        car_info['customer_name'] = None
        car_info['rent_price'] = None
        car_info['service_start_date'] = None
        car_info['service_end_date'] = None
    
    def return_car(self,car_model):

        if not self.is_available_this_model(car_model):
            raise Exception('please ensure that this model is available in this company')
        
        if not self.is_rented(car_model):
            raise Exception('this car is not rented currently')
        
        car_info = self.cars[car_model]

        if car_info['status']=='available':
            raise Exception('this car is already available in the rent store')

        car_info['status'] = 'available'
        car_info['customer_name'] = None
        car_info['rent_price'] = None
        car_info['service_start_date'] = None
        car_info['service_end_date'] = None

if __name__ == "__main__":
    UttaraCarMart = CarRentalSystem("UttaraCarMart") 
    UttaraCarMart.add_car("Toyota Corolla")
    UttaraCarMart.rent_car("Toyota Corolla","Rahim Uddin",100, "2024-06-01", "2024-06-10")
    print(UttaraCarMart.is_rented("Toyota Corolla"))  # Output: True

    UttaraCarMart.return_car("Toyota Corolla")
    print(UttaraCarMart.is_rented("Toyota Corolla"))  # Output: False

    UttaraCarMart.maintenance_car("Toyota Corolla")
    print(UttaraCarMart.is_maintenance_period("Toyota Corolla"))  # Output: True    
    UttaraCarMart.return_car("Toyota Corolla")
    print(UttaraCarMart.is_rented("Toyota Corolla"))  # Output: False 
    UttaraCarMart.return_car("Toyota Corolla") 
    UttaraCarMart.rent_car("Toyota Corolla","Farhan Kabir",120, "2024-06-11", "2024-06-20")
    print(UttaraCarMart.is_rented("Toyota Corolla"))  # Output: True
    UttaraCarMart.return_car("Toyota Corolla")
    print(UttaraCarMart.is_rented("Toyota Corolla"))  # Output: False
