#Task 1

def command_parser(user_input):
    commands = ["help", "issue", "contact support"]
    
    for command in commands:
        if command in user_input.lower():
            if command == "help":
                print("Here are some available commands: help, issue, contact support.")
            elif command == "issue":
                print("Please describe the issue you're experiencing.")
            elif command == "contact support":
                print("You can contact support via email at support@example.com or by phone at 1-800-123-4567.")
            return

    print("Sorry, I couldn't understand your query. Please try again or type 'help' for assistance.")

user_input = input("How can I assist you today? ")
command_parser(user_input)

#Task 2
def issue_categorizer(user_input):
    keywords = {
        "login": ["login", "authentication", "password"],
        "performance": ["slow", "lagging", "performance"],
        "error": ["error", "bug", "crash"]
    }

    for category, words in keywords.items():
        for word in words:
            if word in user_input.lower():
                return category

    return None

def command_parser(user_input):
    commands = ["help", "issue", "contact support"]
    
    for command in commands:
        if command in user_input.lower():
            if command == "help":
                print("Here are some available commands: help, issue, contact support.")
            elif command == "issue":
                issue_category = issue_categorizer(user_input)
                if issue_category:
                    print(f"Your issue seems to be related to {issue_category}. Our support team will assist you accordingly.")
                else:
                    print("Please describe the issue you're experiencing.")
            elif command == "contact support":
                print("You can contact support via email at support@example.com or by phone at 1-800-123-4567.")
            return

    print("Sorry, I couldn't understand your query. Please try again or type 'help' for assistance.")

user_input = input("How can I assist you today? ")
command_parser(user_input)
