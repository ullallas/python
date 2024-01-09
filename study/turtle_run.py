import turtle
from random import randint

tcolor = ['red', 'gold', 'green', 'blue', 'violet']
tlist = []
title = ['☆','★','☆','★','거', '북', '이', '경', '주', '대', '회', '마', '참', '내', '시', '작','☆','★','☆','★',]
b = turtle

# 제목 변경
b.title('turtle race')

# 트랙
b.speed(0)
b.up()
b.ht()
b.goto(-350,210)

for i in range(20):
    b.pendown(), b.write(title[i], font=('', 20)), b.fd(30)
    b.up(), b.rt(90), b.fd(30), b.down(), b.fd(370), b.up(), b.bk(400), b.lt(90)
k = b.xcor()

# 생성
for i in range(len(tcolor)):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(tcolor[i])
    t.speed(0)
    
    # 정렬
    t.up()
    t.goto(-350, 200-60*(i+1))
    t.down()
    tlist.append(t)
    
# 출발
b.speed(0)
x=1
while x == 1:
    for i in range(5):
        x1 = randint(2,20)
        tlist[i].fd(x1)
        if tlist[i].xcor() >= k-20:
            win = i
            x = 0
        
for i in range(1,10):
    tlist[win].shapesize(i)
    tlist[win].right(45)
    

        
        
input("Press any key to exit...")
    
    