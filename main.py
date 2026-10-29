class TimeSlot:
    def __init__(self, slotId, date, startTime, endTime, isAvailable=True):
        self.slotId = slotId
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.isAvailable = isAvailable

    def checkAvailability(self):
        return self.isAvailable

    def reserve(self):
        self.isAvailable = False

    def release(self):
        self.isAvailable = True


class Appointment:
    def __init__(self, appointmentId, patient, doctor, slot):
        self.appointmentId = appointmentId
        self.patient = patient
        self.doctor = doctor
        self.slot = slot
        self.status = "Pending"

    def submitRequest(self):
        self.status = "Pending"

    def accept(self):
        self.status = "Accepted"

    def decline(self):
        self.status = "Declined"


class Patient:
    def __init__(self, patientId, name, system):
        self.patientId = patientId
        self.name = name
        self.system = system

    def viewAvailability(self, doctor):
        return self.system.viewAvailability(doctor)

    def bookAppointment(self, doctor, slot):
        return self.system.bookAppointment(self, doctor, slot)

    def getUpcomingAppointments(self):
        return [
            appt for appt in self.system.appointments
            if appt.patient == self and appt.status in ["Pending", "Accepted"]
        ]


class Doctor:
    def __init__(self, doctorId, name, system):
        self.doctorId = doctorId
        self.name = name
        self.system = system
        self.available_slots = []

    def addSlot(self, slot):
        self.available_slots.append(slot)

    def getAvailableSlots(self):
        return [slot for slot in self.available_slots if slot.checkAvailability()]

    def acceptAppointment(self, appointment):
        return self.system.respondToRequest(self, appointment, "Accept")

    def declineAppointment(self, appointment):
        return self.system.respondToRequest(self, appointment, "Decline")


class AppointmentBookingSystem:
    def __init__(self, max_upcoming=3):
        self.appointments = []
        self.doctors = []
        self.patients = []
        self.N = max_upcoming

    def viewAvailability(self, doctor):
        return doctor.getAvailableSlots()

    def checkAppointmentLimit(self, patient):
        upcoming_count = len(patient.getUpcomingAppointments())
        return upcoming_count < self.N

    def bookAppointment(self, patient, doctor, slot):
        if not self.checkAppointmentLimit(patient):
            return {"success": False, "message": "Booking failed: Maximum upcoming appointments limit (3) reached."}
        
        if not slot.checkAvailability():
            return {"success": False, "message": "Booking failed: Time slot is unavailable."}

        # Create appointment request
        appointmentId = len(self.appointments) + 1
        appointment = Appointment(appointmentId, patient, doctor, slot)
        appointment.submitRequest()
        self.appointments.append(appointment)
        
        return {"success": True, "message": "Booking request submitted (Pending)", "appointment": appointment}

    def respondToRequest(self, doctor, appointment, decision):
        if appointment.doctor != doctor:
            return {"success": False, "message": "Unauthorized doctor response."}

        if decision.lower() == "accept":
            appointment.accept()
            appointment.slot.reserve()
            self.notifyPatient(appointment.patient, "Accepted")
            return {"success": True, "status": "Accepted"}
        elif decision.lower() == "decline":
            appointment.decline()
            appointment.slot.release()
            self.notifyPatient(appointment.patient, "Declined")
            return {"success": True, "status": "Declined"}
        
        return {"success": False, "message": "Invalid decision."}

    def notifyPatient(self, patient, status):
        # Simulation of notification dispatch
        print(f"Notification to {patient.name}: Your appointment status is now {status}.")


if __name__ == "__main__":
    system = AppointmentBookingSystem()
    doc = Doctor(1, "Dr. House", system)
    pat = Patient(1, "John Doe", system)

    slot1 = TimeSlot(101, "2026-11-01", "10:00", "11:00")
    doc.addSlot(slot1)

    print("Available slots:", len(pat.viewAvailability(doc)))
    result = pat.bookAppointment(doc, slot1)
    print(result["message"])