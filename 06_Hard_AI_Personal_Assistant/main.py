from datetime import datetime
import platform
import urllib.parse
import webbrowser


def process_command(command):
    command = command.strip().lower()

    if command in ("hello", "hi", "hey"):
        return "Hello! How can I help you?", False

    if command == "time":
        return f"The current time is {datetime.now().strftime('%I:%M:%S %p')}.", False

    if command == "date":
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}.", False

    if command == "open youtube":
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube.", False

    if command == "open google":
        webbrowser.open("https://www.google.com")
        return "Opening Google.", False

    if command.startswith("search "):
        query = command[7:].strip()
        if query:
            url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
            webbrowser.open(url)
            return f"Searching Google for {query}.", False

    if command == "system":
        return f"Operating system: {platform.system()}\nMachine: {platform.machine()}", False

    if command == "help":
        return (
            "Commands: hello, time, date, open youtube, open google, "
            "search <topic>, system, help, bye"
        ), False

    if command in ("bye", "exit", "quit"):
        return "Goodbye! Have a great day.", True

    return "Sorry, I don't understand that command yet.", False


def run_assistant():
    print("AI Personal Assistant")
    print("Type 'help' to see available commands.")

    while True:
        command = input("You: ")
        response, should_exit = process_command(command)
        print("Assistant:", response)

        if should_exit:
            break


if __name__ == "__main__":
    run_assistant()
