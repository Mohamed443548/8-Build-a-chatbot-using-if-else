
print("🤖 ChatBot: Hello! I'm ChatBot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["hi", "hello"]:
        print("🤖 ChatBot: Hello there! How can I help you today?")
    
    elif "your name" in user_input:
        print("🤖 ChatBot: I'm just a simple rule-based chatbot created by Mohamed Idrish!")

    elif "how are you" in user_input:
        print("🤖 ChatBot: I'm doing great, thanks for asking! What about you?")
    
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"🤖 ChatBot: The current time is {current_time}")

    elif "bye" in user_input:
        print("🤖 ChatBot: Goodbye! Have a great day! 👋")
        break

    elif "help" in user_input:
        print("🤖 ChatBot: I can answer greetings, tell the time, and talk about myself. Try saying 'hello', 'time', or ask 'what's your name'.")

    else:
        print("🤖 ChatBot: Sorry, I don't understand that. Can you ask something else?"