from hardcore.event_handler import EventHandler
from models import Users
from app import db
from timer import timeout

class FuckOff(EventHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event_types = ['message']

    def check_event(self,event):
        '''This method chek message?'''
        if event['message'].get('text') == '/start':
            return True
        return False

    def handle_event(self,event):
        id = event['message']['from']['id']
        user_be = Users.query.filter(id== Users.user_id).first()
        
        self.send_me_not_know(event['message']['chat']['id'])

        if user_be:
            a = self.api_bot.method('sendMessage', {'chat_id':event['message']['chat']['id'],'text': 'Где новые люди?', 'reply_markup': self.get_keyboard()})
            print(a)
        else:
            self.api_bot.method('sendMessage', {'chat_id': event['message']['chat']['id'], 'text': 'Нифига, новичок?'})

            user= Users(user_id = id, role = 'Novice', is_admin= False)
            db.session.add(user)
            db.session.commit()
    
    def get_keyboard(self):
        return {'inline_keyboard':[[
            {'text': 'huy', 'callback_data': 'sfklhj'}
        ]]}

    @timeout(20)
    def send_me_not_know(self, chat_id):
        self.api_bot.method('sendMessage', {'chat_id': chat_id, 'text': '20?'})

