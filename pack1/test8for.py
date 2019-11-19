# for
from bottleneck.reduce import ss
for i in [1, 2, 3, 4, 5]:
    print(i, end=' ')
else:
    print('수행완료')
    
colors = ['r','g','b'] # list
for v in colors:
    print(v, end=' ')
print()
colors = {'r','g','b','b'} # set
for v in colors:
    print(v, end=' ')
print()
colors = ('r','g','b') # tuple
for v in colors:
    print(v, end=' ')
    
print()
soft = {'java':'웹용언어', 'python':'만능언어', 'scala':'자바친구'}
for i in soft.items():
    print(i)
    
print()
for k, v in soft.items():
    print(k)
    print(v)
    
print()

for k in soft.keys():
    print(k,end=' ')
print()
for v in soft.values():
    print(v,end=' ')

print()
print(list(range(5)))
i = iter(range(10))
print(next(i))
print(next(i))

print()
for i in [2, 3]:
    print('--{}단--'.format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print('{0} * {1} = {2}'.format(i,j,i*j))
        
print()
li = ['a', 'b', 'c']
for k, d in enumerate(li):
    print(k, ' ', d)
    
print()
datas = [1,2,3,4,5]
for i in datas:
    if i == 3:
        #continue
        break
    print(i, end = ' ')
else:
    print('for 정상 반복')
    
print()
jum = [95, 70, 60, 50, 100]
number = 0
for j in jum:
    number += 1
    if j < 70:
        continue
    print('%d번째 합격'%number)
    
print()
li1 = [3,4,5]
li2 = [0.5,1,2]

for a in li1:
    for b in li2:
        print(a + b, end = ', ')
        
print()
datas = [a + b for a in li1 for b in li2]
print(datas)

print('--------------------------------')
import re
ss = '''
이태호 외교부 2차관은 5일 오전 국회 예산결산위원회에서 전날 문재인 대통령과 아베 신조 일본 총리가 11분 동안 가진 단독 환담에 대해 "양국 최고위층의 소통이란 점에서 아주 의미가 크다"고 말했다. 13개월 만에 성사된 두 정상의 대화를 한일관계 정상화의 긍정적 신호로 볼 수 있느냐는 물음에 대한 답변이었다. 이 차관은 "소통 지속의 필요성에 (양국이) 공감하는 상황"이라며 "입장을 좁히기 위한 여러 협의를 진행하고 있다"고 했다.
일본 정부 대변인인 스가 요시히데 일본 관방장관은 비슷한 시간 열린 이날 정례브리핑에서 "아베 총리가 문 대통령에게 일본의 원칙적인 입장을 제대로 전달했다"며 "한국 측에 현명한 대응을 요구해 갈 생각에 변함이 없다"고 했다. 환담의 의미와 한일관계에 미칠 영향을 묻는 질문엔 "예단을 갖고 말하는 것은 자제하겠다"라고 즉답을 피했고, 문 대통령이 제안한 고위급 협의에 응할지 여부에 대해서도 함구했다.
교도통신 등 일본 언론에 따르면, 모테기 도시미쓰 외무상은 이날 기자회견에서 "(한일 정상이) 10분 간 말을 주고받은 것을 갖고 커다란 평가를 하는 것은 어렵다"며 평가를 보류했다고 한다. 두 정상의 대화를 한일 관계를 풀 중대 모멘텀으로 인식한 우리 정부와 달리 일본 정부는 의미를 애써 축소하고 있는 셈이다.
일본 언론들의 보도 행태도 다르지 않았다. 일본 주요 언론들은 문 대통령이 아세안+3 정상회의 대기장에서 아베 총리를 이끌어 환담을 성사시킨 데 대해 한일 군사정보보호협정(GSOMIA·지소미아) 종료 결정 철회와 한미일 안보협력을 강조하는 미국에 한일 관계 개선 노력을 보여주기 위한 것이라고 분석했다.
정상 차원의 최고위급 대화에 대한 일본 정부와 언론의 부정적 인식은 한일 갈등의 핵심 쟁점인 일제 강제징용 배상 판결에 대한 해법이 여전히 요원한 현실과 무관하지 않다. 모테키 외무상은 회견에서 문 대통령의 고위급 협의 제안과 관련해 "레벨의 문제라기 보다는 내용이 중요하다"고 주장했다. 이낙연 국무총리의 최근 방일과 두 정상의 단독 환담에도 한국 정부가 강제징용 문제의 해법을 마련하지 않으면 한일 관계가 풀리기 어렵다는 점을 강조한 발언으로 읽힌다.
'''
print(type(ss))

ss2 = re.sub(r'[^가-힣\s]', '', ss)

print(ss2)

ss3 = ss2.split(' ')
print(ss3)
cou = {}
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1
print(cou)

print()
from time import localtime
print()

print(localtime().tm_year)

act = {6:'잠', 9:'아침먹고 출근', 18:'일하기', 20:'야근', 24:'휴식'}
print(act)
print(sorted(act.keys()))

hour = localtime().tm_hour

for act_time in sorted(act.keys()):
    if hour < act_time:
        print(act[act_time])
        break
    else:
        print('~~~~~~~~~~~~')
        
print('과일 값 출력-----')
price = {'사과':2000, '감':500, '바나나':1000}
guest = {'사과':2, '감':3}
print(sum([2,3], 0))
bill = sum(price[f] * guest[f] for f in guest)
print(bill)

print()

datas = [1, 2, 'a', True, 3]
li = [i * i for i in datas if type(i) == int]
print(li)

print()
datas = {1, 1, 2, 3, 3}
se = {i * i for i in datas}
print(se)

print()
id_name = {1:'tom', 2:'james'}
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
temp = [1, 2, 3]
for i in temp:
    print(i, end=' ')
print()
print([i for i in temp])
print({i for i in temp})

print()
temp2 = list()
for i in temp:
    temp2.append(i + 10)
print(temp2)

temp3 = [i + 10 for i in temp]
print(temp3)

print()
aa = [(1, 2), (3, 4), (5, 6)]
print(aa)
t = (1,) # tuple
#t = 1 # int
#t = (1) # int
for a, b in aa:
    print(a + b)
    
print('\n-----------------------')
print(list(range(1,6)))
print(set(range(1,11,3)))
print(tuple(range(-10,-100,-20)))

print()
for a in range(6):
    print(a, end = ' ')
    
print()
# n-gram : 문자열에서 n개의 연속된 값을 추출
text = 'hello'

for i in range(len(text) - 1):
    print(text[i], text[i + 1], sep = '')

print()
text = 'this is python script'
words = text.split()
print(words)
for i in range(len(words) - 1):
    print(words[i], words[i + 1], sep = '')

# 2 ~ 9단 출력
for i in range(2,10):
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j), end = ' ')
    print()
print()
# 문1) 1 ~ 100 사이의 3의 배수이면서 5의 배수의 합
sum = 0
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        sum += i
print(sum)
# 문2) 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
for i in range(1,7):
    for j in range(1,7):
        if (i + j) % 4 == 0:
            print('({}, {})'.format(i,j), end=' ')
    print()
    
print([[i,j] for i in range(1,7) for j in range(1,7) if (i+j) % 4 == 0])
