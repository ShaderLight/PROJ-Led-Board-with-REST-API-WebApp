import requests
from typing import List
from util import hexColorToLedziak, depolonizator3000
from wulgFilter import PRZEKLENSTWA

class LoadBalancer:
    def __init__(self, ipAdresses: List[str]) -> None:
        self.ipAdresses: List[str] = ipAdresses
        self.loadSpread: List[int] = [0]  * len(ipAdresses)
        self.TEXTENDPOINT = '/api/text'
    
    def sendText(self, colorHTML:str, text:str) -> bool:
        colorLedziak = hexColorToLedziak(colorHTML)

        if len(text) > 255:
            return False
        
        text = depolonizator3000(text)
        text = text.replace(" ", "_")
        allowedChars:str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

        for s in text:
            if s not in allowedChars:
                return False
        
        for p in PRZEKLENSTWA:
            if p in text:
                return False
            
        picoNum = self.loadSpread.index(min(self.loadSpread))
        params = {
            't':text,
            'color':colorLedziak
        }
        text_response = requests.put(self.ipAdresses[picoNum] + self.TEXTENDPOINT, params=params, timeout=100)
        
        print(text_response.status_code)

        if text_response.status_code == 201:
            self.loadSpread[picoNum] += len(text)
            self.stripLoad()
            return True
        return False
    
    def stripLoad(self):
        m = min(self.loadSpread)
        for i in range(len(self.loadSpread)):
            self.loadSpread[i] -= m