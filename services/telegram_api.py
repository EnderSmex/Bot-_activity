import requests

class TelegramApi():

    
    def __init__(self,token):
        self.TOKEN = token
        self.BASEURL="https://api.telegram.org/bot{TOKEN}/"
        self.http = requests.Session()
        self.auth()

    def auth(self):
        self.BASEURL = self.BASEURL.format(TOKEN=self.TOKEN)

    def method(self,method,data):
        url= self.BASEURL + method + '?'
        query_string= ''
        for key,value in data.items():
            if isinstance(value,list):
                valuest= ','.join(value)
            else:
                valuest= value
            query_string+= key + '=' + str(valuest) + '&'
        url+=query_string
        response=self.http.get(url).json()
        return response
                  

