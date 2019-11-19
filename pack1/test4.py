# tuple : list와 유사, 읽기 전용(속도가 빠르다)'
t = ('a', 'b', 'c', 'a')
t = 'a', 'b', 'c', 'a'
print(t,len(t))

#t[1] = 'kbs' # 'tuple' object does not support item assignment
li = list(t) # list로 형변화
li[1] = 'kbs'
t = tuple(li)
print(t)

# set : 순서, 중복X
a = {1, 2, 3, 3, 1}
print(a, type(a))

b = {3, 4}
print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a - b, a | b, a & b) # 차집합 합집합 교집합

#print(b[0]) # set은 슬라이싱 불가
b.add(5)
print(b)
b.update({6, 7}) # 셋 추가가능
b.update([8, 9]) # 리스트 추가가능
b.update((10, 11)) # 튜플 추가가능
print(b)

b.discard(10) #  값 삭제 - 있으면 삭제 없으면 생략
b.remove(11) # 값 삭제 - 있으면 삭제 없으면 에러
print(b)

c = set()
c = b # 주소 치환 (얕은 복사)
c.clear()
print(c)

li = [1, 2, 2, 3, 4, 2, 2]
print(li)
s = set(li) # 중복 제거
li = list(s)
print(li)

# dict : {'key' : 'value'} - json처리에 좋음
mydic = dict(k1 = 1, k2 = 2, k3 = 3.4)
print(mydic)
dic = {'파이썬':'뱀', '자바':'커피', '스프링':'용수철'}
print(dic, len(dic))
print(dic['자바'])
#print(dic[0]) # 인덱싱 불가

dic['오라클'] = '예언자' # 추가
print(dic)
del dic['오라클'] # 삭제
print(dic)
#dic.clear() # 모두 삭제
print(dic.pop('자바')) # 추출

print(dic.keys())
print(dic.values())
print(dic.get('파이썬')) # 참조
print(dic)
print('자바' in dic, '파이썬' in dic) # 있는지 확인