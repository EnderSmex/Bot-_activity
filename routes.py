from app import app
from flask import request
import json
from config import TelegramConfig
from hardcore.message_controler import MessageControler
from services.telegram_api import TelegramApi
from handlers_list import handlers_list


api_bot = TelegramApi(TelegramConfig.TOKEN)

controler= MessageControler(handlers_list,api_bot)

@app.route('/',methods=['POST'])
def huy():
    data=json.loads(request.data.decode('utf-8'))
    if 'message' in data:
        print(data['message']['from']['first_name'])

        try:
            print(data['message']['text'])
        except:
            pass
        controler.processing(data)
    return "ok"

@app.route('/secret',methods=['GET','POST'])
def pack():
    return "Soon we will rule the world. Ave Muslim "