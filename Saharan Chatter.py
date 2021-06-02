from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

echo = ChatBot('SaharanChatter')
echo2 = ChatBot('SaharanChatter2')


# Create a new trainer for the chatbot
trainecho = ChatterBotCorpusTrainer(echo)
trainecho2 = ChatterBotCorpusTrainer(echo2)

echo.storage.drop()
echo2.storage.drop()

trainecho.train("chatterbot.corpus.english")
trainecho2.train("chatterbot.corpus.english")

echos = input("Starting string?")
while True:
    print(echo2.get_response(echos))
    echos2 = echo2.get_response(echos)
    print(echo.get_response(echos2))
    echos = echo.get_response(echos2)
