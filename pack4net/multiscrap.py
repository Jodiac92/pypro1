# 웹 스크래핑
import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool
def get_links():
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    print(html) # <class 'str'>
    soup = bs(html, 'html.parser')
    my_titles = soup.select('h3 > a')
    data = []
    for title in my_titles:
        data.append(title.get('href'))
    return data

def get_content(link):
    abs_link = 'https://beomi.github.io' + link
    req = requests.get(abs_link)
    html = req.text
    soup = bs(html, 'html.parser')
    print(soup.select('h1')[0].text)

if __name__ == '__main__':
    startTime = time.time()
    
#     for link in get_links():
#         get_content(link) # 6 ~ 8초
    
    # 병렬 처리(multi processing)
    pool = Pool(processes = 4)
    pool.map(get_content, get_links()) # 2 ~ 3초 
    
    
    print('-- %s 초 --'%(time.time() - startTime))