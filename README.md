# AI Task Execution Assistant

A simple AI agent project built with Python and uv.

This assistant can:
- Understand user requests
- Break tasks into execution steps
- Ask clarifying questions
- Use mock tools
- Handle API failures gracefully
- Return structured summaries

---

## Features

### Task Planning
The assistant creates execution plans based on user intent.

### Clarifying Questions
If information is missing, the agent asks follow-up questions.

Example:
- "Which city are you located in?"
- "Do you prefer weekdays or weekends?"

### Mock Tools
Implemented tools:
- calendar_check()
- search_service()
- booking_service()
- reminder_create()

### Error Handling
If the OpenAI API is unavailable or quota is exceeded, the assistant automatically switches to fallback mode.

---

## Tech Stack

- Python 3.12
- OpenAI API
- uv
- python-dotenv

---

## Project Structure

```txt
agent-assignment/
│
├── pyproject.toml
├── uv.lock
├── .env.example
├── README.md
├── main.py
│
└── src/
    ├── agent.py
    ├── planner.py
    ├── prompts.py
    └── tools.py
    Setup

Install dependencies:

uv sync

Run the assistant:

uv run python main.py
Environment Variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here
Example Requests
Find me 3 coworking spaces in Warsaw under $20/day
Book me a dentist appointment
Plan a 2-day trip to Prague under €300
Notes

This project uses mock services instead of real external APIs for simplicity and demonstration purposes.