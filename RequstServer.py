import json, base64, requests
from requests_negotiate_sspi import HttpNegotiateAuth
from datetime import datetime


class RequestServer(object):
    
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            
        return cls._instance

    def __init__(self):
        # input essential details here
        self.client_id = 'xxx'
        self.client_secret = 'xxxxxx'
        self.token_url = 'https://ids.xxx.com/connect/token'

        self.data = {'grant_type': 'password',
                     'username': 'xxx',
                     'password': "xxxxxx",
                     'scope': 'webapi'}

        if not hasattr(self, 'inited'):
            self.inited = False

        if not self.inited:
            self.inited = True
            self.token = self.get_token()[0]
            self.start_time = self.get_token()[1]

    def get_token(self):
        headers = {'Authorization': 'Basic {}'
            .format(base64.b64encode(bytes('{}:{}'
                                           .format(self.client_id, self.client_secret)
                                           .encode('utf-8'))).decode('utf-8'))}
        try:
            # post the server and get the local time of the server
            response = requests.post(self.token_url, headers=headers, data=self.data, verify=True,
                                     allow_redirects=False)
            access_token = json.loads(response.text)["access_token"]
            # if access_token, record the time
            if response.text is not None:
                retrieve_time = datetime.strptime(response.headers["Date"], "%a, %d %b %Y %H:%M:%S GMT")

            return access_token, retrieve_time

        except:
            return access_token, 'Retrieve access_token failed!'

    # token: eyJhbGciOiJSUzI1NiIsImtpZCI6IjkyNjNCQTAyNEIzMDQ3OEI4Q0ZEQjc5OT...

    def if_refresh_token(self, startTime, Token):
        import datetime
        # if token expires in 3600 seconds
        # can define by yourself or suggest to set as an hour(3600 second)
        if (datetime.datetime.now() - startTime).seconds <= 3600 :
            token = Token
        # if overdue, get new token
        else:
            token = obj.get_token()[0]

        return token

    def request_client(self, url, params, method):
        Token = self.if_refresh_token(start_time, token)
        # get or post for further purpose
        if method == 'get':
            # put the token in headers
            if Token is not None:
                response = requests.get(url, params=params,
                                        headers={'Content-Type': 'application/json',
                                                 "Authorization": "Bearer " + Token})

            # if access_token is None, try windows id to request
            else:
                try:
                    response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                            auth=HttpNegotiateAuth())
                except Exception as e:
                    print(str(e))

        elif method == 'post':
            if Token is not None:
                response = requests.post(url, data=json.dumps(params),
                                         headers={'Content-Type': 'application/json',
                                                  "Authorization": "Bearer " + Token})

            else:
                try:
                    response = requests.post(url, data=json.dumps(params), headers={'Content-Type': 'application/json'},
                                             auth=HttpNegotiateAuth())

                except Exception as e:
                    print(str(e))

        return json.loads(response.text)



