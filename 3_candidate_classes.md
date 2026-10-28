# Candidate Classes (P3)

## 1. Patient

**Responsibilities** - View doctors' available time slots. - Request an
appointment. - Keep track of upcoming appointments.

**Candidate attributes** - `patientId` - `name`

**Candidate methods** - `viewAvailability(doctor)` -
`bookAppointment(doctor, slot)` - `getUpcomingAppointments()`

## 2. Doctor

**Responsibilities** - Publish available time slots. - Review
appointment requests. - Accept or decline appointment requests.

**Candidate attributes** - `doctorId` - `name`

**Candidate methods** - `getAvailableSlots()` -
`acceptAppointment(appointment)` - `declineAppointment(appointment)`

## 3. Appointment

**Responsibilities** - Represent an appointment request between a
patient and a doctor. - Store the request status. - Associate the
request with a selected time slot.

**Candidate attributes** - `appointmentId` - `status`

**Candidate methods** - `submitRequest()` - `accept()` - `decline()`

**Possible status values:** `Pending`, `Accepted`, `Declined`.

## 4. TimeSlot

**Responsibilities** - Represent a time when a doctor is available. -
Indicate whether a time slot is available for booking. - Become
available again when a declined request releases the slot.

**Candidate attributes** - `slotId` - `date` - `startTime` - `endTime` -
`isAvailable`

**Candidate methods** - `checkAvailability()` - `reserve()` -
`release()`

## 5. AppointmentBookingSystem

**Responsibilities** - Display a doctor's available time slots. -
Process appointment booking requests. - Enforce the maximum of N = 3
upcoming appointments per patient. - Send appointment requests to
doctors and notify patients of the result.

**Candidate methods** - `viewAvailability(doctor)` -
`bookAppointment(patient, doctor, slot)` -
`checkAppointmentLimit(patient)` -
`respondToRequest(doctor, appointment, decision)` -
`notifyPatient(patient, status)`

## Notes

-   R1--R4 are covered by the candidate classes and their
    responsibilities.
-   R5--R7 are non-functional requirements and are not modelled as
    separate use cases here.
-   The class design is a candidate model and should be checked against
    the final class and sequence diagrams.
