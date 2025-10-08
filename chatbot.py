def simple_chatbot():
    """
    Basic chatbot using if-elif-else structure
    """
    print("🤖 ChatBot: Hi! I'm a simple bot. Say 'hello', 'how are you', or 'bye'")

    while True:
        message = input("You: ").lower()

        if message == "hello":
            print("🤖 ChatBot: Hi!")

        elif message == "how are you":
            print("🤖 ChatBot: I'm fine, thanks!")

        elif message == "what is your name":
            print("🤖 ChatBot: I'm BasicBot!")

        elif message == "bye":
            print("🤖 ChatBot: Goodbye!")
            break

        else:
            print("🤖 ChatBot: I don't understand. Try: hello, how are you, bye")


# Run the chatbot
simple_chatbot()
