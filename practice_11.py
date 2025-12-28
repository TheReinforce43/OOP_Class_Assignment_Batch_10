from datetime import date 

class carLicenceManagement:

    def __init__(self,car_model,owner_name,owner_age,manufacturer,manufacture_year):
        self.car_model = car_model
        self.owner_name = owner_name
        self.owner_age = owner_age
        self.manufacturer = manufacturer
        self.manufacture_year = manufacture_year

        self.licence = None 


    


       

class carLicence:

    def __init__(self,plate_number,registration_date,expiry_date,car_object):

        if not self.is_valid__initial_date(registration_date,expiry_date):
            raise ValueError("Invalid registration or expiry date")
        
        if car_object.licence is not None:
            raise ValueError("This car already has a licence assigned")
        
        self.plate_number = plate_number
        self.registration_date = registration_date
        self.expiry_date = expiry_date
        self.car = car_object 

        self.car.licence = self

     
    def renew_licence(self,new_expiry_date):

        if not self.is_valid_date(new_expiry_date):
            raise ValueError("Invalid expiry date")

        if not self.is_eligible_for_renewal():
            raise ValueError("Licence is not eligible for renewal")
        self.expiry_date = new_expiry_date


    # Helpter method to check if the registration and expiry dates are valid

    def is_valid__initial_date(self,registration_date,expiry_date):

        todays_date = date.today()


        if registration_date <= todays_date <= expiry_date:
            return True
        return False 
    
    def is_valid_date(self,new_expiry_date):
        todays_date = date.today()

        if todays_date < new_expiry_date:
            return True
        return False
    
    def is_eligible_for_renewal(self):
        
        todays_date = date.today()

        registration_date = self.registration_date

        year_interval = todays_date.year - registration_date.year

        return year_interval<=20 
    

if __name__ == "__main__":

    car1 = carLicenceManagement("Model S", "Md.Rahim Uddin", 30, "Tesla", 2020)


    # Valid licence creation
    try:
        licence = carLicence(
            "XYZ789",
            date(2025,10,10,),
            date(2027, 1, 1),
            car1
        )
        print("Licence created successfully")
        print("Expiry Date:", licence.expiry_date)

    except ValueError as e:
        print("Licence creation failed:", e)


    # Invalid licence creation (expiry date before registration date)
    try:
        licence1 = carLicence(
            "ABC123",
            date(2022, 1, 1),
            date(2023, 1, 1),
            car1
        )
        print("Licence created successfully")
        print("Expiry Date:", licence1.expiry_date)

    except ValueError as e:
        print(" Licence creation failed:", e)

    # Licence renewal
    try:
        licence.renew_licence(date(2029, 12, 31))
        print("Licence renewed successfully")
        print("New Expiry Date:", licence.expiry_date)
    except ValueError as e:
        print("Licence renewal failed:", e)

    # Checking eligibility for renewal after 20 years
    try:   
        old_car = carLicenceManagement("Old Model", "Jane Doe", 55, "OldManufacturer", 2000)
        old_licence = carLicence(
            "OLD123",
            date(2000, 1, 1),
            date(2026, 1, 1),
            old_car
        )
        old_licence.renew_licence(date(2045, 12, 31))
        print("Old licence renewed successfully")
        print("New Expiry Date:", old_licence.expiry_date)  
    except ValueError as e:
        print("Old licence renewal failed:", e)

    # Attempting to assign a second licence to the same car
    try:    
        second_licence = carLicence(
            "SECOND123",
            date(2023, 1, 1),
            date(2025, 1, 1),
            car1
        )
        print("Second licence created successfully")    
    except ValueError as e:
        print("Second licence creation failed:", e)