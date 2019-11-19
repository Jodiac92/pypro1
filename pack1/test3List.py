# 자료형 : string (순서O, 수정X)
s = "sequence"
print(len(s))
print(s.count('e'))
print(s.find('e',3))
print(s.startswith('s'))

ss = 'mbc'
print(ss, 'mbc', id(ss))
ss = 'abc'
print(ss,id(ss))

print('슬라이싱------------')
print(s[0], s[:3], s[2:4], s[3:])
print(s[-1], s[-4:-1], s[-4:], s[::2])
print(id(s))
s = 'fre' + s[2:]
print(s)
print(id(s))

a= 'Life is too short'
print(a)
b = a.replace("Life", "My Leg")
print(b)

# 자료형 : list (순서O, 수정O) - 배열과 비슷하다
#a=[1,2,3] # 비권장
a = [1, 2, 3] # 권장
b = [10, a, 20.5, True, '문자열']
print(b)
print(b[0], b[1], b[1][0])
b.remove(10) # 값에 의한 삭제
print(b)
del b[1] # 순서에 의한 삭제
print(b)

print()
fa = ['엄마', '아빠', '나']
fa.append('동생') # 추가
fa.extend(['삼촌', '조카']) # 여러개 추가
fa += ['고모', '이모'] # 여러개 추가
fa.insert(0, '할머니') # 특정 위치에 추가
print(fa, len(fa))
print(fa.index("나"))
print('엄마' in fa)
