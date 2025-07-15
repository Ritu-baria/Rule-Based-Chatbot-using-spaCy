import spacy
#loada spacy english model
nlp=spacy.load("en_core_web_sm")
# Define simple intents and responses
INTENTS = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "thanks": ["thanks", "thank you", "thx"],
    "name": ["what is your name", "who are you"],
    "weather": ["weather", "rain", "sunny", "forecast"],
    "joke": ["tell me a joke", "make me laugh", "funny"]
}
RESPONSES = {
    "greeting": "Hello! How can I help you today?",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "name": "I’m ChatBot, your virtual assistant.",
    "weather": "I can't check the weather right now, but it's always sunny in the cloud ☁️",
    "joke": "Why did the computer show up at work late? It had a hard drive!"
}
# Function to get intent
def get_intent(user_input):
    doc = nlp(user_input.lower())
    for token in doc:
        for intent, keywords in INTENTS.items():
            if token.lemma_ in keywords or user_input.lower() in keywords:
                return intent
    return "unknown"
# Chat loop
def chat():
    print("ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        intent = get_intent(user_input)
        if intent == "goodbye":
            print(f"ChatBot: {RESPONSES[intent]}")
            break
        elif intent in RESPONSES:
            print(f"ChatBot: {RESPONSES[intent]}")
        else:
            print("ChatBot: I'm not sure how to respond to that.")

# Run the chatbot
chat()