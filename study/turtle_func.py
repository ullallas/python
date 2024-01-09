import turtle

# 제목변경
turtle.title('hi turtle')

# 생성
turtle.shape('turtle')

# 함수정의
def move(length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

move(-200) # 함수 호출

# 사각형 그리기
for _ in range(4):
    turtle.forward(50)
    turtle.left(90)

move(100)

# 도장 찍기
colors = ['red', 'green', 'yellow', 'blue']
for color in colors:
    turtle.color('black', color)
    turtle.forward(50)
    turtle.stamp()

move(150)

# 삼각형 그리기
for i in range(3):
    turtle.left(120)
    turtle.color('black', colors[i])
    turtle.forward(100)
    turtle.stamp()
    
    



input("Press any key to exit...")