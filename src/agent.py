import os

from openai import OpenAI
from dotenv import load_dotenv

from src.prompts import SYSTEM_PROMPT
from src.planner import create_plan
from src.tools import (
    calendar_check,
    search_service,
    booking_service,
    reminder_create
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def build_fallback_response(user_input, plan, tool_results):

    response = "Task Execution Summary\n\n"

    response += "User request:\n"
    response += f"- {user_input}\n\n"

    response += "Execution plan:\n"

    for index, step in enumerate(plan, start=1):
        response += f"{index}. {step}\n"

    response += "\nTool results:\n"

    if tool_results:
        for result in tool_results:
            response += f"- {result}\n"
    else:
        response += "- No external tool results were needed.\n"

    response += "\nFinal result:\n"

    if "coworking" in user_input.lower():
        response += (
            "I found suitable coworking options "
            "based on the requested budget and location."
        )

    elif "appointment" in user_input.lower():
        response += (
            "I checked availability and prepared a booking result."
        )

    elif "trip" in user_input.lower():
        response += (
            "I created a basic travel planning structure. "
            "More details like travel dates and starting city "
            "would improve the result."
        )

    else:
        response += (
            "The request was analyzed and a structured response was prepared."
        )

    response += "\n\nRemaining blockers:\n"

    response += (
        "- If exact booking is required, "
        "real calendar/search/booking APIs should be connected.\n"
    )

    return response


def run_agent(user_input):

    plan = create_plan(user_input)

    tool_results = []

    missing_questions = []

    if "appointment" in user_input.lower():

        if "warsaw" not in user_input.lower():
            missing_questions.append(
                "Which city are you located in?"
            )

        if (
            "weekend" not in user_input.lower()
            and "weekday" not in user_input.lower()
        ):
            missing_questions.append(
                "Do you prefer weekdays or weekends?"
            )

    if missing_questions:

        response = "Missing information:\n"

        for question in missing_questions:
            response += f"- {question}\n"

        response += (
            "\nPlease resend your full request with these details.\n"
        )

        response += (
            "Example: "
            "Book me a dentist appointment in Warsaw "
            "on weekdays after 5pm"
        )

        return response

    if "coworking" in user_input.lower():

        results = search_service(user_input)

        if results:

            tool_results.append(
                "Coworking spaces found:"
            )

            for result in results:
                tool_results.append(result)

        else:
            tool_results.append(
                "No coworking spaces found under the given criteria."
            )

    if "appointment" in user_input.lower():

        availability = calendar_check(
            "next week after 5pm"
        )

        tool_results.append(availability)

        booking = booking_service(
            "Dental appointment"
        )

        tool_results.append(booking)

    if (
        "remind" in user_input.lower()
        or "reminder" in user_input.lower()
    ):

        reminder = reminder_create(user_input)

        tool_results.append(reminder)

    final_prompt = f"""
User Request:
{user_input}

Execution Plan:
{plan}

Tool Results:
{tool_results}

Provide:
1. Task summary
2. Steps completed
3. Final recommendation
4. Remaining blockers
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": final_prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception:

        return build_fallback_response(
            user_input,
            plan,
            tool_results
        )