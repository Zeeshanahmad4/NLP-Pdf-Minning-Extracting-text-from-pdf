# ahmadzee26-gmail.com
NLP Pdf Minning Extracting text from pdf
'''
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
res = requests.get("https://coronavirus.1point3acres.com/en")
soup = BeautifulSoup(res.content,'lxml')
#print(soup)
list1=[]
contentTable  = soup.find_all('div',{ "class" : "jsx-3748010317 stat row"})
dic={'location':None,'confirmed':None,'New':None,'Deaths':None,'source':None}
for i in range(len(contentTable)):
#print(contentTable)
#print(contentTable[0].get_text())
    c1=contentTable[i].find_all('span')
    dic['location']=c1[0].get_text()
    dic['confirmed']=c1[1].get_text()
    dic['New']=c1[2].get_text()
    dic['Deaths']=c1[3].get_text()
    try:
        dic['source']=c1[4].find('a').get('href')
    except:
        ()
    list1.append(dic)
print(list1)
'''
