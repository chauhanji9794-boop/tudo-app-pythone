# TECH GOD - Intelligent Tech Assistant

# Function to display welcome message
def greet():
    print("⚡ Welcome to TECH GOD ⚡")
    print("Type your tech question or 'exit' to quit.\n")


# Function to process user input and return response
def get_response(user_input):
    # Convert input to lowercase for easy matching
    user_input = user_input.lower()

    # Conditions to check keywords
    if "python" in user_input:
        return "Python is used for AI, web development, automation, and more."

    elif "java" in user_input:
        return "Java is a powerful object-oriented programming language."

    elif "ai" in user_input:
        return "AI means Artificial Intelligence — machines that think like humans."

    elif "html" in user_input:
        return "HTML is used to create web pages."

    elif "git" in user_input:
        return "Git tracks changes in your code."

    elif "github" in user_input:
        return "GitHub is a cloud platform to store your Git projects."

    elif "exit" in user_input:
        return "exit"

    else:
        return "I am still learning... ask another tech question!"


# Main function to run the app
def main():
    greet()  # Call greeting function

    # Infinite loop to keep program running
    while True:
        # Take input from user
        user_input = input("You: ")

        # Get response from function
        response = get_response(user_input)

        # Check if user wants to exit
        if response == "exit":
            print("Tech God: Goodbye 👋")
            break

        # Print response
        print("Tech God:", response)


# Entry point of program
if __name__ == "__main__":
    main()