# Class Diagram (P5)

```mermaid
classDiagram
    class Patient {
        +patientId
        +name
        +viewAvailability(doctor)
        +bookAppointment(doctor, slot)
        +getUpcomingAppointments()
    }

    class Doctor {
        +doctorId
        +name
        +getAvailableSlots()
        +acceptAppointment(appointment)
        +declineAppointment(appointment)
    }

    class Appointment {
        +appointmentId
        +status
        +submitRequest()
        +accept()
        +decline()
    }

    class TimeSlot {
        +slotId
        +date
        +startTime
        +endTime
        +isAvailable
        +checkAvailability()
        +reserve()
        +release()
    }

    class AppointmentBookingSystem {
        +viewAvailability(doctor)
        +bookAppointment(patient, doctor, slot)
        +checkAppointmentLimit(patient)
        +respondToRequest(doctor, appointment, decision)
        +notifyPatient(patient, status)
    }

    Patient "1" --> "0..*" Appointment : requests
    Doctor "1" --> "0..*" Appointment : reviews
    Doctor "1" --> "0..*" TimeSlot : publishes
    TimeSlot "1" --> "0..*" Appointment : requested for

    AppointmentBookingSystem ..> Patient : manages booking for
    AppointmentBookingSystem ..> Doctor : coordinates requests with
    AppointmentBookingSystem ..> Appointment : creates and updates
    AppointmentBookingSystem ..> TimeSlot : checks and reserves
```

**Business rule:** A patient may have at most 3 upcoming appointments at
any given time (N = 3).

**Design note:** A time slot can be linked to multiple appointment
requests over time---for example, if a doctor declines a request and the
slot is released. The system must prevent conflicting active bookings
for the same slot.
