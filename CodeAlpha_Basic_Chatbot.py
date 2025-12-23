import datetime

chat_history = []

def save_history():
    with open("chat_history.txt", "w") as file:
        for line in chat_history:
            file.write(line + "\n")

def get_time():
    now = datetime.datetime.now()
    return now.strftime("Current time is %I:%M %p")

def get_date():
    today = datetime.date.today()
    return today.strftime("Today's date is %B %d, %Y")

def tell_joke():
    jokes = [
        "Why don’t programmers like nature? It has too many bugs!",
        "I told my computer I needed a break, and it said: 'No problem, I'll go to sleep.'",
        "Why was the JavaScript developer sad? Because he didn’t Node how to Express himself!"
    ]
    import random
    return random.choice(jokes)

def chatbot_response(user_input, user_name):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return f"Hi {user_name}! How can I help you today?"
    
    elif user_input in ["how are you", "how are you?", "how r u"]:
        return "I'm doing great! Thanks for asking 😊"
    
    elif "time" in user_input:
        return get_time()

    elif "date" in user_input:
        return get_date()

    elif "joke" in user_input:
        return tell_joke()

    elif "weather" in user_input:
        return "The weather is nice and sunny! (Just a fixed response 😉)"

    elif user_input in ["bye", "goodbye", "exit"]:
        return f"Goodbye {user_name}! Have a wonderful day 😊"
    
    else:
        return "Sorry, I didn’t understand that. Try asking for time, date, joke, or say hello."

# Starting the chatbot
print("🤖 Welcome to the Advanced Python Chatbot!")
user_name = input("Before we start, what is your name? ")

print(f"Nice to meet you, {user_name}! Type 'bye' to exit.\n")

while True:
    user_message = input("You: ")
    reply = chatbot_response(user_message, user_name)

    print("Bot:", reply)

    # Save chat messages
    chat_history.append(f"You: {user_message}")
    chat_history.append(f"Bot: {reply}")

    if user_message.lower() in ["bye", "goodbye", "exit"]:
        save_history()
        print("📁 Chat history saved to 'chat_history.txt'")
        break
