# Task 1: Simple Rule-Based Chatbot

class SimpleChatBot:
    def __init__(self):
        # Predefined rules and responses
        self.rules = {
            # Greetings
            'greeting': {
                'patterns': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good evening', 'good afternoon'],
                'responses': [
                    "Hello! How can I help you today?",
                    "Hi there! What can I do for you?",
                    "Hey! How are you doing?",
                    "Greetings! How may I assist you?"
                ]
            },
            
            # How are you
            'how_are_you': {
                'patterns': ['how are you', 'how do you do', 'what\'s up', 'how\'s it going'],
                'responses': [
                    "I'm doing great, thank you for asking!",
                    "I'm fine! How about you?",
                    "All good here! How can I help you?",
                    "I'm doing well! What's on your mind?"
                ]
            },
            
            # Name questions
            'name': {
                'patterns': ['what is your name', 'what\'s your name', 'who are you', 'your name'],
                'responses': [
                    "I'm a simple chatbot created to help you!",
                    "You can call me ChatBot! What's your name?",
                    "I'm your friendly AI assistant!",
                    "My name is ChatBot, nice to meet you!"
                ]
            },
            
            # Weather
            'weather': {
                'patterns': ['weather', 'temperature', 'climate', 'forecast', 'raining', 'sunny'],
                'responses': [
                    "I don't have real-time weather data, but you can check your local weather app!",
                    "For current weather information, I'd recommend checking a weather website or app.",
                    "Sorry, I can't provide weather updates. Try checking online for your area!",
                    "I wish I could tell you about the weather, but I don't have that capability yet!"
                ]
            },
            
            # Time
            'time': {
                'patterns': ['what time', 'current time', 'time now', 'what\'s the time'],
                'responses': [
                    "I don't have access to real-time data. Please check your device's clock!",
                    "Sorry, I can't tell the current time. Check your phone or computer!",
                    "I don't have time information. Your device should show the current time!"
                ]
            },
            
            # Help
            'help': {
                'patterns': ['help', 'assist', 'support', 'what can you do', 'commands'],
                'responses': [
                    "I can chat with you about various topics! Try asking me about myself, saying hello, or asking general questions.",
                    "I'm here to help! You can greet me, ask about my name, or just have a conversation.",
                    "I can respond to greetings, questions about myself, and general chat. What would you like to talk about?",
                    "I'm a simple chatbot. I can answer basic questions and have conversations with you!"
                ]
            },
            
            # Technology/Programming
            'technology': {
                'patterns': ['programming', 'coding', 'python', 'technology', 'computer', 'software'],
                'responses': [
                    "Technology is fascinating! Are you interested in programming?",
                    "I love talking about tech! What specific area interests you?",
                    "Programming and technology are great fields to explore!",
                    "Technology keeps evolving! What aspect would you like to discuss?"
                ]
            },
            
            # Goodbye
            'goodbye': {
                'patterns': ['bye', 'goodbye', 'see you', 'farewell', 'take care', 'exit', 'quit'],
                'responses': [
                    "Goodbye! It was nice chatting with you!",
                    "See you later! Have a great day!",
                    "Bye! Feel free to come back anytime!",
                    "Take care! Thanks for the conversation!"
                ]
            },
            
            # Thanks
            'thanks': {
                'patterns': ['thank you', 'thanks', 'appreciate it', 'grateful'],
                'responses': [
                    "You're welcome! Happy to help!",
                    "No problem at all!",
                    "Glad I could help!",
                    "You're very welcome!"
                ]
            }
        }
    
    def find_match(self, user_input):
        """Find matching pattern in user input"""
        user_input = user_input.lower().strip()
        
        for category, data in self.rules.items():
            for pattern in data['patterns']:
                if pattern in user_input:
                    return category
        
        return None
    
    def get_response(self, user_input):
        """Generate response based on user input"""
        import random
        
        # Find matching category
        category = self.find_match(user_input)
        
        if category:
            # Return random response from matched category
            responses = self.rules[category]['responses']
            return random.choice(responses)
        else:
            # Default responses for unmatched input
            default_responses = [
                "I'm not sure how to respond to that. Can you try asking something else?",
                "That's interesting! Can you tell me more or ask something different?",
                "I don't quite understand. Try asking about greetings, help, or general topics!",
                "Hmm, I'm still learning. Can you rephrase that or ask something else?",
                "I'm not sure about that. Feel free to ask me about myself or say hello!"
            ]
            return random.choice(default_responses)
    
    def chat(self):
        """Main chat loop"""
        print("=" * 50)
        print("🤖 Simple Rule-Based Chatbot")
        print("=" * 50)
        print("Hello! I'm a simple chatbot. Type 'quit' or 'bye' to exit.")
        print("Try saying hello, asking for help, or just chat with me!")
        print("-" * 50)
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                print("Bot: Please type something!")
                continue
            
            # Check for exit conditions
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print("Bot: Goodbye! Thanks for chatting with me!")
                break
            
            # Get and display response
            response = self.get_response(user_input)
            print(f"Bot: {response}")

# Create and test the chatbot
print("Creating Simple Rule-Based Chatbot...")
chatbot = SimpleChatBot()

# Test with some sample inputs
test_inputs = [
    "Hello",
    "What's your name?",
    "How are you?",
    "What can you do?",
    "Tell me about programming",
    "What's the weather like?",
    "Thank you",
    "Random text that doesn't match"
]

print("\n" + "="*60)
print("TESTING THE CHATBOT WITH SAMPLE INPUTS:")
print("="*60)

for test_input in test_inputs:
    response = chatbot.get_response(test_input)
    print(f"User: {test_input}")
    print(f"Bot: {response}")
    print("-" * 40)

print("\n" + "="*60)
print("CHATBOT READY! Run chatbot.chat() to start interactive mode")
print("="*60)
chatbot.chat()
