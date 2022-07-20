from hardcore.event_handler import EventHandler
from models import Users
from app import async_session
from sqlalchemy.future import select
import asyncio

class FuckOff(EventHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event_types = ['message']

    async def check_event(self,event):
        '''This method chek message?'''
        if event['message'].get('text') == '/start':
            return True
        return False

    async def handle_event(self,event):
        id = event['message']['from']['id']
        async with async_session() as session:
            user_be = await session.execute(select(Users).where(Users.user_id == id))
            user_be = user_be.scalars().first()

        if user_be:
            a = self.api_bot.method('sendMessage', {'chat_id':event['message']['chat']['id'],'text': 'Где новые люди?', 'reply_markup': self.get_keyboard()})
            print(a)
        else:
            self.api_bot.method('sendMessage', {'chat_id': event['message']['chat']['id'], 'text': 'Нифига, новичок?'})
            async with async_session() as session:
                user= Users(user_id = id, role = 'Novice', is_admin= False)
                session.add(user)
                await session.commit()
        await asyncio.sleep(60)
        self.api_bot.method('sendMessage', {'chat_id': event['message']['chat']['id'], 'text': 'mmmom'})
    
    def get_keyboard(self):
        return {'inline_keyboard':[[
            {'text': 'huy', 'callback_data': 'sfklhj'}
        ]]}