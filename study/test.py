# a = 1+2
# print(type(a))

# name = input('name :')
# print(name)

# 리스트에 데이터 추가하기
""" 
list = []
name = '창균'
list.append(name)
print(list) 
"""

# 리스트 데이터 불러오기 및 배열 갯수 구하기
""" 
names = ['aa', 'bb', 'cc']
print(names[0])
print(names[1:])
print(len(names))
"""

# 인덱스 찾기
""" 
names = ['aa', 'bb', 'cc']
print(names.index('aa'))
"""
 
# 리스트 내림차순 정렬
""" 
x = [4,2,3,1]
y = sorted(x)
print(y)
"""

# 이차원 배열 리스트에서 특정 값 가져오기
""" 
names = ['aa', 'bb', 'cc', 'dd']
scores = [10, 50, 90, 60]
highscores = [names, scores]
print(highscores)
print(highscores[1][1])
"""

# 딕셔너리 - key/value - key는 불변하는 값만 넣을 수 있음
""" 
dic = {'사과': 1, '바나나': 2, '포도': 3}
print(dic)
"""

# 빈 딕셔너리에 값 추가하기
""" 
dic = {}

dic['임창균'] = '123-4567'
dic['이민혁'] = '444-8888'
dic['유기현'] = '111-9999'

print(dic)
"""

# 딕셔너리에 값 추가
""" 
dic = {'사과': 1, '바나나': 2, '포도': 3}
dic['망고'] = 5
print(dic)
"""

# 딕셔너리 키, 벨류 값 체크
""" 
dic = {'사과': 1, '바나나':2, '포도': 3}

print(dic.keys())
print(dic.values())
"""

# 튜플
""" 
r = tuple('1' '2')
x = (1, 2, 3)
y = ('a', 'b', 'c')
z = (1, "hello", "there")

print(r)
print(x + y)
print('a' in y)
print(z.index(1))
"""

# 조건문
""" 
if 2 > 1:
    print("조건문 하이룽")

if not 1 > 2:
    print("조건문 바이룽")
"""

""" 
a = 0

if a > 1:
    print("a는 1보다 큽니다")

elif a < 1:
    print("a는 1보다 작습니다")

else:
    print("a는 1보다 크지도 작지도 않습니다")
"""

# 조건문 연산자
""" 
if 1 > 0 and 2 > 1:
    print("조건문 and 연산자 hello")
    
if 1 > 0 or 0 > 1:
    print("조건문 or 연산자 hello")
"""

# 순서대로 치환
""" 
print('포지셔닝포맷팅, 순서대로 치환, aram hello {} say how are you {} fine not'
      .format('ck',12))
"""

# 위치기반 치환
""" 
print('to {name}. Loren ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut...{age}'
      .format(name='ck', age=12))
"""

# 반복문
""" 
for i in range(3):
    print("hi for")
"""

""" 
name = ['서울', '대전', '대구', '부산', '경기도', '인천']
for i in name:
    print(i)
"""  

""" 
i = 0
while True:
    print("무한루프 & 브레이크")
    i = i + 1

    if i > 2:
        break
"""

""" 
for i in range(2,10):
    for s in range(1,10):
        print("%2d x %2d = %5d" %(i, s, i*s))
"""