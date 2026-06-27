def chatbot():
    print("Simple Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()
        greetings=["hello","hii","hi","hey"]

        if any(word in user for word in greetings):
               print("Bot: Hi,how can i help you?!")
        
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        
        elif "name" in user:
            print("Bot: My name is ChatBot.")
        
        elif "bye" in user:
            print("Bot: Goodbye!")
            break
        
        else:
            print("Bot: Sorry,I don't understand that.")


# Run the chatbot
chatbot()
