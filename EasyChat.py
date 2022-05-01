import socket, os
from threading import Thread
from database import DATABASE
from server import SERVER
from screens import SCREENS
            
class APP(SERVER,SCREENS,DATABASE):
    def __init__(self):
        self.checkData()
        self.screen = 'selectAcount'
        self.lookingAtContact = 'none'
        self.nickName = ''
        self.objetos = []
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        self.PORT = 3001
        self.HOST = s.getsockname()[0]
        self.running = True
        self.generateWindow()
        while True:
            if self.portIsGood(self.HOST,self.PORT): break
            else: self.PORT += 1
        Thread(target=self.runServer).start()
        self.selectAcountScreen()
        self.window.mainloop()

    def addAcount(self,entry):
        acount = entry.get()
        data = self.getData()
        if acount not in data: data[acount] = {}
        self.saveData(data)
        self.enterAcount(acount=entry.get())

    def enterAcount(self,acount):
        self.nickName = acount
        self.contactsScreen()

    def addMessage(self,message):
        try:
            data = self.getData()
            messageData = message.split('<>')
            print(f'Message: {message}\n\nMessageData: {messageData}')
            if messageData[0] in data[self.nickName]:
                data[self.nickName][messageData[0]]['messages'].append(messageData[1])
            else:
                data[self.nickName][messageData[0]] = {'messages':[messageData[1]],'contact':messageData[2]}
            self.saveData(data)
        except:
            os.system('cls')
            print(f'erro ao adicionar mensagem {message}')

APP()