from chatterbot import ChatBot

bot = ChatBot("Math", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("=========Math ChatBot=========")

while True:
    user_text = input("type the math equation that you want to solve: ")
    print("Chatbot: "+ str.get_response(user_text))
    