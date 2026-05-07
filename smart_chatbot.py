import datetime

print("🤖 Smart AI ChatBot")
print("Type 'bye' to exit\n")

while True:

    user_input = input("You: ").lower()

    # Greetings
    if user_input == "hello":
        print("Bot: Hello! 👋")

    elif user_input == "hi":
        print("Bot: Hi there! 😊")

    # How are you
    elif user_input == "how are you" or user_input == "how r u":
        print("Bot: I am doing great! 😄")

    # Name
    elif user_input == "your name" or user_input == "ur name":
        print("Bot: I am Smart AI ChatBot 🤖")

    # Time
    elif user_input == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    # Joke
    elif user_input == "joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs 😂")

    # Calculator
    elif user_input == "calculator":

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        operation = input("Choose operation (+, -, *, /): ")

        if operation == "+":
            print("Result:", num1 + num2)

        elif operation == "-":
            print("Result:", num1 - num2)

        elif operation == "*":
            print("Result:", num1 * num2)

        elif operation == "/":

            if num2 != 0:
                print("Result:", num1 / num2)

            else:
                print("Cannot divide by zero")

        else:
            print("Invalid operation")

    # Exit chatbot
    elif user_input == "bye":
        print("Bot: Goodbye 👋")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that.")