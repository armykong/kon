from read_dic import read_dic # 注音字典
from read_article import read_article
from Analysys import Analysys


Dic=read_dic()
myDict=Dic.myDict
Article=read_article("GigaWord_text_lm") # giga.txt GigaWord_text_lm
myArticle=Article.text
#分析
myAnaly=Analysys(myDict,myArticle)
myAnaly.Count()