# Requirements (P1)

| ID | Requirement | Type | Category |
|---|---|---|---|
| R1 | A patient can view the days and times when a doctor is available. | Functional | Availability |
| R2 | A patient can book an appointment during an available time slot. | Functional | Booking |
| R3 | A doctor can accept or decline an appointment request. | Functional | Request handling |
| R4 | A patient can have at most **N** upcoming appointments at any given time. | Functional | Booking rule |
| R5 | Patient medical data shall be accessible only to authorized staff. | Non-functional | Security |
| R6 | Available appointment times shall be displayed within 2 seconds. | Non-functional | Performance |
| R7 | The application shall be usable on mobile phone screens. | Non-functional | Usability |

**N = 3** (our choice: enough for a checkup plus follow-ups, still limits slot hoarding).

R4 is a business rule about the number of appointments, so we treat it as functional.