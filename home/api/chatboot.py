from chatterbot import ChatBot
chatbot = ChatBot("Skfweb")
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


def get_response_data(input_data):
    try:
        response = chatbot.get_response(input_data)
        return response
    except Exception as e:
        return False

def bot_traner(training_data):
    try:
        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train(
            "chatterbot.corpus.english"
        )
        return "Bot tran successfully"
    except Exception as e:
        return False
    
def self_traner(training_data):
    try:
        conversation = []
        for k, v in training_data.items():
	        conversation.append(v)
        trainer = ListTrainer(chatbot)
        trainer.train(conversation)
        return "Bot tran successfully"
    except Exception as e:
        print(e)
        return False

