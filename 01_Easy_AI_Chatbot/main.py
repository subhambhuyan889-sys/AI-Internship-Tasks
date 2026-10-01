def get_response(message):
    message = message.strip().lower()

    if message in ("hello", "hi", "hey"):
        return "Hello! How can I help you?"
    if "your name" in message or "who are you" in message:
        return "I am a simple rule-based AI chatbot."
    if "how are you" in message:
        return "I am doing well. Thanks for asking!"
    if message == "help" or "help" in message:
        return "I can answer simple questions about myself."
    if message in ("bye", "exit", "quit"):
        return "Goodbye! Have a great day."

    return "Sorry, I don't understand that yet."


def run_chat():
    print("Simple Rule-Based AI Chatbot")
    print("Type 'bye' to exit.")

    while True:
        user_message = input("You: ")
        response = get_response(user_message)
        print("Bot:", response)

        if user_message.strip().lower() in ("bye", "exit", "quit"):
            break


if __name__ == "__main__":
    run_chat()
