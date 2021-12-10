from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
import re

def msg(message):
    news = re.sub('[^A-Za-z0-9]+',' ', message)
    bot_token = 'YOUR BOT TOKEN'
    bot_chatID = 'YOUR BOT ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='+ bot_chatID + '&parse_mode=MarkdownV2&text=' + news

    response = requests.get(send_text)
    print(send_text)
    return response.json()

def sendTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    bot_token = 'YOUR BOT TOKEN'
    bot_chatID = 'YOUR BOT ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='+ bot_chatID + '&parse_mode=MarkdownV2&text=' + current_time

    response = requests.get(send_text)
    print(send_text)
    return response.json()

lst = []
c = 0
k = 0
itr = 3
try:
    while k != itr:
        print(k)
        url = 'https://news.google.com/news/rss'
        r = requests.get(url)
        web_c = BeautifulSoup(r.text,'xml')
        web_c = web_c.find_all('item')
        # return web_c  
        lstNews = []

        for i in web_c:
            if(i.title.text not in lstNews):         
                lstNews.append(i.title.text)

        print(lstNews)
        k = k + 1
        time.sleep(3)      #30 sec delay
        if k == (itr-1):
            sendTime()
            for i in range(len(lstNews)):
                news = lstNews[i]
                msg(lstNews[i])
                print(lstNews[i])
                time.sleep(3)
            k = 0
except KeyboardInterrupt:
    pass



