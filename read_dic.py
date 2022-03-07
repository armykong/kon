class read_dic:
    def __init__(self):
        self.path = "單字詞_13053(注音_無聲調).dic"
        self.myDict = dict()
        #讀入字典,在在myDict
        with open(self.path,mode="r",encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                #取(key,value)
                line=line.strip()

                if(line==""): #空行則忽略
                    continue 

                

                temp_dic=line.split(",")
                
                if len(temp_dic)>1:
                    key=temp_dic[0]
                    value=temp_dic[1]
                    
                    #檢查value是否還有",",若有則取第0個切片
                    ary =value.split(",")
                    #存(key,value)
                    if(len(ary)>1):
                        self.myDict[key] = ary[0]
                    else:
                        self.myDict[key] = value

    