# dict 모양의 텍스트를 읽어 dict type으로 처리
import ast

with open('dict.txt', mode='r') as f:
    aa = f.read()
    print(aa)
    print(type(aa))
    bb = ast.literal_eval(aa) # eval 보다 보안이 강하다.
    print(bb)
    print(type(bb))
    
print('----------------------------')
with open('dict.txt','r') as f2:
    cc = eval(f2.read())
    print(cc)
    print(type(cc))