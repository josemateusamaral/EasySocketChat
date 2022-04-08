import json
import os

class DATABASE:
    def getData(self):
        with open('APLICATION_DATA','r') as file: return json.load(file)

    def saveData(self,data):
        with open('APLICATION_DATA','w') as file: json.dump(data,file)

    def checkData(self):
        #if 'APLICATION_DATA' in os.listdir(): os.remove('APLICATION_DATA')
        if 'APLICATION_DATA' not in os.listdir():
            with open('APLICATION_DATA','w') as file: json.dump({},file)