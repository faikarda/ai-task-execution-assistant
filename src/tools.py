def calendar_check(date_range):

    return f"""
Available time slots for {date_range}:

- Tuesday 18:00
- Wednesday 19:00
- Friday 17:30
"""


def search_service(query):

    query_lower = query.lower()

    if "coworking" in query_lower and "warsaw" in query_lower:

        return [
            "Brain Embassy - $15/day",
            "HubHub Warsaw - $18/day",
            "Cowork Central - $20/day"
        ]

    if "dentist" in query_lower:

        return [
            "Smile Dental Clinic",
            "Warsaw Dental Center",
            "Happy Teeth Clinic"
        ]

    return []


def booking_service(option):

    return f"Successfully booked: {option}"


def reminder_create(details):

    return f"Reminder created: {details}"