#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import spacy

#python -m spacy link en_core_web_lg en

spacy.load("en")
app = Flask(__name__)

#create chatbot
englishBot = ChatBot("mqbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")


trainer = ListTrainer(englishBot)

training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

#trainer = ListTrainer(chatbot)
trainer.train(training_data) 

trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english") #train the chatter bot for english


#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))

if __name__ == "__main__":
    app.run()
