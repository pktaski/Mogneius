import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://pktaski: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@github.com/pktaski/Filters-Bot okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
