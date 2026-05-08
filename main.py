from src.agent import run_agent


def main():
    print("\nAI Task Execution Assistant Started")
    print("Type 'exit' to quit.\n")

    pending_request = None

    while True:
        user_input = input("What can I help you with?\n> ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if pending_request:
            combined_input = pending_request + " " + user_input
            response = run_agent(combined_input)
            pending_request = None
        else:
            response = run_agent(user_input)

        if "Missing information:" in response:
            pending_request = user_input

        print("\n==============================")
        print(response)
        print("==============================\n")


if __name__ == "__main__":
    main()