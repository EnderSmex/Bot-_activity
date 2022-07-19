
class EventControler():

    def __init__(self,handlers,api_bot):
        self.handlers = handlers
        self.api_bot = api_bot

    def processing(self,event):
        for handler in self.handlers:
            handler = handler(self.api_bot)
            if self.__check_event_type(handler,event) and handler.check_event(event) :
                handler.handle_event(event)
                return
        
    def __check_event_type(self, handler, event):
        list_events = handler.get_event_types()

        for a in list_events:
            if event.get(a, False):
                return True
        return False
