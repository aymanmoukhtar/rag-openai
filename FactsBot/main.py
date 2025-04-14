from dotenv import load_dotenv

from chat.chatbot import Chatbot

load_dotenv()

chatbot = Chatbot()

while True:
    content = input("\n>> ")

    if (content.lower() == "exit"):
        break

    print(chatbot.send_message(content))
