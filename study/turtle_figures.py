import turtle

# 제목변경
turtle.title('hi turtle')

# 함수정의
def move(length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()
    
move(-300)

for i in range(3,15):
    turtle.begin_fill()
    turtle.circle(20, steps=i)
    move(50)
    turtle.end_fill()
    
input("Press any key to exit...")
