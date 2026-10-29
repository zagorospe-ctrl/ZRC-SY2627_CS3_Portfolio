class Patient():
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount

    def display_patient_info(self):
        print("Hospital Billing System")
        print("-------------------")
        print(f"Patient Name: {self.name}")
        print(f"Original Bill: {self.bill_amount}")
        print(f"Final Bill: {self.calculate_bill()}")


class SeniorPatient(Patient):
    def __init__(self, name, bill_amount, senior_discount):
        super().__init__(name, bill_amount)
        self.senior_discount = 0.20

    def calculate_bill(self):
        discounted_amount = self.bill_amount * (1 - self.senior_discount)
        return discounted_amount

    def display_patient_info(self):
            super().display_patient_info()

class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount, philhealth_discount):
        super().__init__(name, bill_amount)
        self.philhealth_discount = 0.15

    def calculate_bill(self):
        discounted_amount = self.bill_amount * (1 - self.philhealth_discount)
        return discounted_amount

    def display_patient_info(self):
        super().display_patient_info()

    

regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000, 0.20)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000, 0.15)

patients = [regular_patient, senior_patient, philhealth_patient]

for patient in patients:
    patient.display_patient_info()

