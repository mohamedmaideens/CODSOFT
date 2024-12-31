def chatbot():
    print("Chatbot: Hello! I am your assistant. How can I help you today?")
    print("Type 'exit' to end the conversation.")

    while True:#converting user response to lowercase in order to overcome case problem 
        user_input = input("You: ").strip().lower()
        
        # Exit condition
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Rule-based responses
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you?")
        elif "your name" in user_input:
            print("Chatbot: I am a simple rule-based chatbot.")
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")#displaying time in terms of hours minute seconds 
        elif "weather" in user_input:
            print("Chatbot: I cannot check the weather yet, but you can use a weather app!")
        elif "help" in user_input:
            print("Chatbot: Sure! I can answer questions about time, weather, or general inquiries.")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you please rephrase?")
chatbot()
#calling chatbot method
