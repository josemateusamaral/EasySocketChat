import tkinter as tk
from functools import partial

class SCREENS:
    def generateWindow(self):
        self.window = tk.Tk()
        self.window.config(bg='white')
        tamanho = int(self.window.winfo_screenheight()/2)
        px = int(self.window.winfo_screenwidth()/2 - tamanho / 2)
        py = int(self.window.winfo_screenheight()/2 - tamanho / 2)
        self.window.geometry('{}x{}+{}+{}'.format(tamanho,tamanho,px,py))
        self.window.title('EASY CHAT - Messages')
        
    def zeroWindow(self):
        for i in self.window.winfo_children(): i.destroy()

    def defaultWidgets(self):
        tk.Label(text=f'Servindo em {self.HOST}:{self.PORT} as {self.nickName}',bg='green').pack()

    def selectAcountScreen(self):
        self.zeroWindow()
        tk.Label(text='choose acount',master=self.window).pack(side='top')
        tk.Button(text='add acount',master=self.window,command=self.addAcountScreen).pack(side='top')
        for nickname in self.getData(): tk.Button(text=nickname,command=partial(self.enterAcount,nickname)).pack(expand=True)

    def addAcountScreen(self):
        self.zeroWindow()
        tk.Label(text='new acount',master=self.window).pack(side='top')
        entrada = tk.Entry(master=self.window)
        entrada.pack()
        tk.Button(text='add acount',master=self.window,command=partial(self.addAcount,entrada)).pack(side='top')

    def contactsScreen(self):
        self.zeroWindow()
        self.window.title('EASY CHAT - Messages')
        self.defaultWidgets()
        done = []
        tk.Button(text='NEW MESSAGE',command=partial(self.messageScreen,'newMessage'),bg='yellow',fg='black').pack(pady=15)
        for name in self.getData()[self.nickName]:
            buttonText = name
            botao = tk.Button(text=buttonText,master=self.window,command=partial(self.messageScreen,name))
            botao.pack()
        tk.Button(text='exit',command=self.closeServer,bg='red').pack(side='bottom')
        tk.Button(text='change acount',command=self.selectAcountScreen,bg='blue').pack(side='bottom')

    def messageScreen(self,name):
        self.zeroWindow()
        self.window.title('EASY CHAT - Messages from ' + name)
        frame = tk.Frame()
        frame.config(bg='white')
        tk.Button(text='<',command=self.contactsScreen,master=frame,bg='red').pack(side='left')    
        self.defaultWidgets() 
        frame.pack(fill='x',pady=4)  

        frame = tk.Frame()
        frame.config(bg='white')
        tk.Label(text='to: ',master=frame,bg='white',fg='black').pack(side='left')
        self.entradaHost = tk.Entry(master=frame)
        self.entradaHost.insert(0,'192.168.0.11:3001')
        self.entradaHost.pack(side='left',fill='x')
        frame.pack(fill='x',pady=4)

        frame = tk.Frame()
        frame.config(bg='white')
        tk.Label(text='your nickname: ',master=frame,bg='white',fg='black').pack(side='left')
        self.entradaName = tk.Entry(master=frame)
        self.entradaName.pack(fill='x',side='left')
        frame.pack(fill='x',pady=4)

        frame = tk.Frame()
        frame.config(bg='white')
        tk.Label(text='message: ',master=frame,bg='white',fg='black').pack(side='left')
        self.NovaMensagem = tk.Entry(master=frame)
        self.NovaMensagem.pack(fill='x',side='left')
        frame.pack(fill='x',pady=4)

        sendButton = tk.Button(text='SEND',command=self.sendMessage,bg='green')
        sendButton.pack(side='bottom')

        if name == 'newMessage': return
        texto = ''
        messagesLabel = tk.Label()
        messagesLabel.pack(expand=True,fill='both')
        for message in self.getData()[self.nickName][name]['messages']: texto += message + '\n\n'
        messagesLabel['text'] = texto
        self.entradaHost.insert(0,self.getData()[self.nickName][name]['contact'])