from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
from flask import Flask, render_template, request


app = Flask(__name__)

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

corpus_path='E:/Hackathon/chatbot/chatterbot_corpus/data/english/'

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)

"""while True:
    message = input('You:')
    print(message)
    if message.strip() == 'Bye':
        print('ChatBot: Bye')
        break
    else:
        reply = bot.get_response(message)
        print('ChatBot:', reply)"""
        
  
"""model_json = trainer.to_json()
with open("chatbot_train.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
trainer.save_weights("chatbot_train.h5")
print("Saved model to disk")"""

app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))
    
if __name__ == "__main__":
    app.run()


