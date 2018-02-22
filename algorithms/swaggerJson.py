

class swagggerJson:

    def __init__(self,description,title,schemes,tagName,tagDescription ):
        self. description = description
        self.title = title
        self.schemes = schemes
        self.tagName = tagName
        self.tagDescription = tagDescription
        self.swaggerDict = {
              "swagger": "2.0",
              "info": {
                "description": self. description,
                "version": "1.0.0",
                "title": self.title,
                "contact": {
                  "email": "cpacket@cpacketnetworks.com"
                },
                "license": {
                  "name": "Apache 2.0",
                  "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
                }
              },
              "schemes": [
                self.schemes
              ],
              "host": "localhost",
              "responses": {
                "Unauthorized": {
                  "description": "Unauthorized to perform this action"
                }
              },
              "tags":
                {
                  "name": self.tagName,
                  "description": self.tagDescription
                }

            }

    def setPath(self, url):
        URL = {url:None}
        paths = {}
        paths.append(URL)

    def setParameter(self,username,InDescription,description,Type):
        param = {'name': username,
        'in': InDescription,
        'description': description,
        'required': True,
        'type': Type}

    def setResponse401(self, description):
        resp401 = {'401':{
        "description": description}}

    def setResponse200(self, description):
        resp200 = {'200': {
            "description": description}}
        ########## work to be done##########


    def portBalance(self,to_port_id,from_port_id,number):
        balance = {}
        for num in range(number):
            infoDict = {'to_port_id':to_port_id,'from_port_id':from_port_id }
            balance[num]=infoDict
        return balance

    def multiClusterBalance(self):

        multiCB = {}
        for num in range(number1):
            for num in range(number2):
                infoDict = {}
                for num in range(number3):
                    info = {}
                    info[num] =


test = swagggerJson('description','title','schemes','tagName','tagDescription' )

print test.swaggerDict
