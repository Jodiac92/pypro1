# 신문 기사 스크래핑 전용 모듈 설치

from newspaper import Article
import re

url = "https://news.v.daum.net/v/20191106150608183"
aa = Article(url, language='ko')
aa.download()
aa.parse()
print('제목 :',aa.title)
print()
ss = aa.text
print(ss)
print('----------------')
ss2 = re.sub(r'[^가-힣\s]','',ss)
print(ss2)