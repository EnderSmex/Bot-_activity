from app import app, api_bot
from flask import request
import json
from hardcore.event_controler import EventControler
from handlers_list import handlers_list
from models import Users
import asyncio


controler= EventControler(handlers_list,api_bot)
loop = asyncio.get_event_loop() 

@app.route('/',methods=['POST'])
def huy():
    
    data=json.loads(request.data.decode('utf-8'))

    print(data)

    try:
        print(data['message']['text'])
    except:
        pass
    asyncio.ensure_future(controler.processing(data), loop=loop)
    return "ok"

@app.route('/secret',methods=['GET','POST'])
def pack():
    return "Soon we will rule the world. Ave Muslim "
