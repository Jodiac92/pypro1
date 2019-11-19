# 정규표현식
import re

ss = '1234 abc가나다ABC_555_6_78_mbc하하78'
print(re.findall(r'123', ss))
print(re.findall(r'[0-9]', ss))
print(re.findall(r'[0-9]+', ss))
print(re.findall(r'[0-9]{2, 3}', ss))
print(re.findall(r'\d+', ss))
print(re.findall(r'\d{2}', ss))
print()
print(re.findall(r'.bc',ss))
print(re.findall(r'a..',ss)) # a로 시작하는 3글자
print(re.findall(r'^1+',ss)) # 1로 시작
print(re.findall(r'[^1]+',ss)) # 1로 시작하는 것을 빼고
print(re.findall(r'78$',ss))
print(re.findall(r'[_a-zA-Z가-힣]',ss))


