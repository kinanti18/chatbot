from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time 

time.clock = time.time

bot = ChatBot("chatbot", read_only=False, 
logic_adapters=[
    { 
        "import_path": "chatterbot.logic.BestMatch", 
        "default_response": "Sorry I don't have an answer", 
        "maximum_similarity_threshold":0.9
    }
    ])

list_to_train = [
    "hi",
    "hi there",
    "what's your name",
    "I'm a chatbot",
    "how old are you?",
    "I'm ageless",
    "why are you so mad?",
    "I'm not",
    "Do you have Iphone",
    "I've everything",
    "What's your favorite food",
    "I don't eat",
    "What's your job?",
    "I'm here to answers your questions",
    "I don't know what you're talking about"
]

list_trainer = ListTrainer(bot)

list_trainer.train(list_to_train)

while True:
    user_response = input("User: ")
    print("Chatbot: ", str(bot.get_response(user_response)))
