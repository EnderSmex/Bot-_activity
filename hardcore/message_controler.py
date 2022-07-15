
class MessageControler():

    def __init__(self,handlers,api_bot):
        self.handlers = handlers
        self.api_bot = api_bot

    def processing(self,message):
        for handler in self.handlers:
            handler = handler(self.api_bot)
            if handler.check_message(message):
                handler.handle_message(message)
                return
        
    
