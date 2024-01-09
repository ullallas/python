import turtle

# 제목변경
turtle.title('hi turtle')

# 생성
turtle.shape('turtle')

# 도장찍기
""" 직선 """
turtle.color('black', 'red')
turtle.stamp()

turtle.forward(30)
turtle.color('black', 'green')
turtle.stamp()

turtle.forward(30)
turtle.color('black','yellow')
turtle.stamp()

turtle.forward(30)
turtle.color('black','blue')
turtle.stamp()

""" 삼각형 """
turtle.color('black','red') 
turtle.forward(100)
turtle.stamp()                 
turtle.left(120)

turtle.color('black','green') 
turtle.forward(100)
turtle.stamp()
turtle.left(120)

turtle.color('black','blue')
turtle.forward(100)
turtle.stamp()

input("Press any key to exit...")
