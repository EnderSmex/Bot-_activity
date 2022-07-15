from hardcore.message_handler import MessageHandler

class FuckOff(MessageHandler):

    def check_message(self,message):
        '''This method chek message?'''
        if message['message']['text'] == 'Привет':
            return True
        return False

    def handle_message(self,message):
        self.api_bot.method('sendMessage',{'chat_id':message['message']['chat']['id'],'text':f"huy tebe, {message['message']['from']['first_name']}"})
