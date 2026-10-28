
# Sequence Diagram (P6)

```mermaid
sequenceDiagram
    actor Patient
    participant System as AppointmentBookingSystem
    participant Slot as TimeSlot
    participant Appointment
    actor Doctor

    Patient->>System: bookAppointment(patient, doctor, slot)
    System->>System: checkAppointmentLimit(patient)

    alt Upcoming appointments >= 3
        System-->>Patient: Reject booking (limit reached)
    else Upcoming appointments < 3
        System->>Slot: checkAvailability()
        alt Slot is unavailable
            Slot-->>System: unavailable
            System-->>Patient: Reject booking (slot unavailable)
        else Slot is available
            System->>Appointment: submitRequest()
            System->>Doctor: Send pending appointment request
            System-->>Patient: Booking request submitted (Pending)

            Doctor->>System: respondToRequest(doctor, appointment, decision)

            alt Doctor accepts
                System->>Appointment: accept()
                System->>Slot: reserve()
                System-->>Patient: Notify status = Accepted
            else Doctor declines
                System->>Appointment: decline()
                System->>Slot: release()
                System-->>Patient: Notify status = Declined
            end
        end
    end
```

## Explanation

1. The patient requests an appointment through the system.
2. The system checks that the patient has fewer than 3 upcoming appointments.
3. The system checks whether the selected time slot is available.
4. If both checks pass, the system creates a pending appointment request and sends it to the doctor.
5. The doctor accepts or declines the request.
6. If accepted, the slot is reserved. If declined, the slot is released and the patient is notified.
