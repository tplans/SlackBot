from slackclient import SlackClient

class Bot:

    def __init__(self, token):
        self.token = token
        sc = SlackClient(token)

    def read_msg(self):
        if sc.rtm_connect():
            print("Connection Established")


    def hello(self):
        sc.api_call("chat.postMessage", channel="#general", text="Hello World")
    