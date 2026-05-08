def create_plan(user_input):

    user_input = user_input.lower()

    if "trip" in user_input:
        return [
            "Find transportation",
            "Find accommodation",
            "Calculate budget",
            "Create itinerary"
        ]

    elif "coworking" in user_input:
        return [
            "Search coworking spaces",
            "Filter by budget",
            "Prepare recommendations"
        ]

    elif "appointment" in user_input:
        return [
            "Check availability",
            "Search providers",
            "Book appointment"
        ]

    else:
        return [
            "Analyze request",
            "Prepare response"
        ]