from asyncio.windows_events import NULL


class Analysys:
    def __init__(self, dic, drticle):
        self.myDic = dic
        self.myArticle = drticle

        self.resultDic = dict()  # 儲存注音符號出現的次數

        # print(self.myDic) #測試
        # print(self.myArticle)#測試

    def Count(self):
        for word in self.myArticle:
            #print(word) 
            try:            
                #在myDic中找到這個key
                注音S=self.myDic[word]               
                #print(word+":"+注音)
                for 注音 in 注音S:
                    # 找resultDic,若這個注音不在其中,就新增這個注音,次數為1
                    # 若resultDic有這個注音,則把次數+1
                    
                    if 注音 in self.resultDic :                        
                        self.resultDic[注音]=self.resultDic[注音]+1
                    else:
                        self.resultDic[注音]=1






            except:
                #字典中沒有這個字
                print("except:"+word)     
        
        print(self.resultDic)
