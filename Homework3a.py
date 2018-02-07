class patient:
    def __init__(self, name):
        #this is how you reference the patient name
        self.name = name

    def discharge(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class EmergencyPatient(patient):
    def __init__(self, name):
        patient.__init__(self,name)
        self.expectedcost = 1000

    def discharge(self):
        print(self.name, "Emergency Patient")

class HospitalizedPatient(patient):
    def __init__(self, name):
        patient.__init__(self,name)
        self.expectedcost = 2000

    def discharge(self):
        print(self.name, "Hospitalized Patient")

class Hospital(patient):
    def __init__(self):
        self.cost = 0
        self.patient = []

    def admit(self, patient):
        #allows us to add patients one at a time, over and over again
        #self.patient is the total list of patients
        self.patient.append(patient)

    def discharge_all(self):
        for patient in self.patient:
            patient.discharge()
            self.cost += patient.expectedcost

    def get_total_cost(self):
        return self.cost

P1 = HospitalizedPatient('P1')
P2 = HospitalizedPatient('P2')
P3 = EmergencyPatient('P3')
P4 = EmergencyPatient('P4')
P5 = EmergencyPatient('P5')

YNHH = Hospital()
YNHH.admit(P1)
YNHH.admit(P2)
YNHH.admit(P3)
YNHH.admit(P4)
YNHH.admit(P5)
YNHH.discharge_all()
print(YNHH.get_total_cost())
