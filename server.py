import socket
import sys

class SERVER:
    def runServer(self):      
        while self.running:       
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
                s.bind((self.HOST,self.PORT))
                s.listen(5)
                conn,addr = s.accept()
                with conn:
                    while True:
                        dataRaw = conn.recv(1024)
                        data = repr(dataRaw)[2:-1]
                        self.addMessage(data)
                        if not dataRaw: break
                self.contactsScreen()

    def sendMessage(self,name):
        if name == 'newMessage': HOST = self.entradaHost.get().split(':')
        else: HOST = self.getData()[self.nickName][name]['contact'].split(':')
        message = f'{self.nickName}<>{self.NovaMensagem.get()}<>{self.HOST}:{self.PORT}' 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST[0],int(HOST[1])))
            s.sendall(message.encode('utf-8')) 

    def closeServer(self):
        self.running = False
        self.window.destroy()
        sys.exit()

    def portIsGood(self,host,port):
        try:      
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host,port))
                s.close()
            return True
        except: return False