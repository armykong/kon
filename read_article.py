import os
from pathlib import Path
class read_article:
    def __init__(self,article):
        
        self.path = article
        self.text="" 
        if article=="" :
            self.path = "giga.txt"
        # get file length
        statinfo = os.stat(self.path)
        size=statinfo.st_size
        print(size)
        #讀入文章,存在text
        with open(self.path,mode="r",encoding="utf-8") as f:
            #char=f.read(1)
            lines = f.readlines()
            for line in lines:
                line=line.strip() #去除換符行
                if(line==""): #空行則忽略
                    continue 

                self.text+=line.replace(" ","")       

    