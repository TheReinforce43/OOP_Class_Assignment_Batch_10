class Hospital :


    def __init__(self,name,address):

        self.name = name
        self.address = address
        self.doctors = dict()
        self.patients = set()


    # Here write main methods for Hospital class

    def add_doctor(self,doctor_id):

        if self.is_doctor_available(doctor_id):
            raise ValueError("Doctor is already added to the hospital")

        self.doctors.append(doctor_id)

    def add_patient(self,patient_id,assigned_doctor_id ):

        if self.is_patient_registered(patient_id):
            raise ValueError("Patient is already registered in the hospital")

        if not self.is_doctor_available(assigned_doctor_id):
            raise ValueError("Assigned doctor is not available in the hospital")

      

    # Here write helper methods for Hospital class

    def is_doctor_available(self,doctor_id):

        if doctor_id in self.doctors:
            return True
        return False
    
    
    def is_patient_registered(self,patient):

        if patient.patient_id in self.patients:
            return True
        return False



class Doctor :


    def __init__(self,name,specialization,years_of_experience):

        self.name = name
        self.specialization = specialization
        self.patients = set()
        self.scheduling_appointments = dict()
        self.patients_treatments= dict()


    # Here write main methods for Doctor class

    def add_patient(self,patient_id):
        pass 

    # Here write helper methods for Doctor class

    


class Patient :


    def __init__(self,patient_id,name,age,facing_disease):

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.facing_disease = facing_disease
       
        self.appointments = list()
        self.treatments = list()

      