
class EventHandler():

    __slots__ = ('event_types')

    def __init__(self, api_bot):
        self.api_bot= api_bot
        self.event_types=[]

    async def check_event(self,event):
        '''This method chek event?'''
        pass

    async def handle_event(self,event):
        pass

    def get_event_types(self):
        return self.event_types

