import requests
import re
from fake_useragent import UserAgent
import csv

def catch(url,header):
    re=requests.get(url,headers=header)
    if re.status_code==200:
        return re.text
    return None

url0='https://maoyan.com/board/4?offset='
ua=UserAgent()
header={"User-Agent":ua.google}
exprs=re.compile('<p.*?title="(.*?)".*?主演：(.*?)</p>.*?上映时间：(.*?)</p>.*?<i.*?">(.*?)</i><i.*?">(.*?)</i>',re.S)

with open("out.csv","w",newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['剧名','主演','上映时间','猫眼评分'])
    for i in range(0,10):
        url=url0+str(i*10)
        html=catch(url,header)
        html=re.sub('\n','',html)
        html=re.sub(' ','',html)
        result=re.findall(exprs,html)
        for each in result:
            lst=[]
            for i in range(0,3):
                lst.append(each[i])
            lst[2]=each[i][0:10]
            lst.append(each[3]+each[4])
            writer.writerow(lst)
