import unittest
from main import AppointmentBookingSystem, Doctor, Patient, TimeSlot

class TestClinicAppointments(unittest.TestCase):
    def setUp(self):
        self.system = AppointmentBookingSystem(max_upcoming=3)
        self.doctor = Doctor(1, "Dr. Smith", self.system)
        self.patient = Patient(1, "Alice", self.system)

    def test_view_availability(self):
        slot = TimeSlot(1, "2026-11-05", "09:00", "10:00")
        self.doctor.addSlot(slot)
        available = self.patient.viewAvailability(self.doctor)
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].slotId, 1)

    def test_successful_booking(self):
        slot = TimeSlot(2, "2026-11-05", "10:00", "11:00")
        self.doctor.addSlot(slot)
        
        result = self.patient.bookAppointment(self.doctor, slot)
        self.assertTrue(result["success"])
        self.assertEqual(result["appointment"].status, "Pending")

    def test_appointment_limit_rule_r4(self):
        # Patient books 3 appointments (N=3 limit)[cite: 1, 2]
        slots = [
            TimeSlot(10, "2026-11-06", "09:00", "10:00"),
            TimeSlot(11, "2026-11-06", "10:00", "11:00"),
            TimeSlot(12, "2026-11-06", "11:00", "12:00")
        ]
        for s in slots:
            self.doctor.addSlot(s)
            res = self.patient.bookAppointment(self.doctor, s)
            self.assertTrue(res["success"])

        # Try booking a 4th slot, should fail per R4
        extra_slot = TimeSlot(13, "2026-11-06", "12:00", "13:00")
        self.doctor.addSlot(extra_slot)
        fail_res = self.patient.bookAppointment(self.doctor, extra_slot)
        self.assertFalse(fail_res["success"])
        self.assertIn("limit (3) reached", fail_res["message"])

    def test_doctor_accept_appointment(self):
        slot = TimeSlot(3, "2026-11-07", "14:00", "15:00")
        self.doctor.addSlot(slot)
        
        booking = self.patient.bookAppointment(self.doctor, slot)
        appt = booking["appointment"]
        
        res = self.doctor.acceptAppointment(appt)
        self.assertTrue(res["success"])
        self.assertEqual(appt.status, "Accepted")
        self.assertFalse(slot.isAvailable)

    def test_doctor_decline_appointment(self):
        slot = TimeSlot(4, "2026-11-07", "15:00", "16:00")
        self.doctor.addSlot(slot)
        
        booking = self.patient.bookAppointment(self.doctor, slot)
        appt = booking["appointment"]
        
        res = self.doctor.declineAppointment(appt)
        self.assertTrue(res["success"])
        self.assertEqual(appt.status, "Declined")
        self.assertTrue(slot.isAvailable)  # Slot released back

if __name__ == "__main__":
    unittest.main()