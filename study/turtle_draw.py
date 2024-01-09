import turtle

""" # 일시정지
turtle.done() """

# 제목변경
turtle.title('hi turtle')

# 생성
turtle.color('black', 'red')
turtle.shape('turtle')

turtle.penup() # 펜 들고 pu
turtle.write("뿡") # 문자열 출력
turtle.forward(80) # 앞으로 이동 fd
# turtle.pendown() # 펜 내림 pd
turtle.backward(100) # 뒤로 이동

""" 펜을 들고 이동하면 이동하는 선이 그려지지 않고 내리고 이동하면 선 그어짐 """

turtle.left(90); turtle.fd(20) # 왼쪽으로 90도 회전, 앞으로 20 이동
turtle.write("뿡")

turtle.right(90); turtle.fd(110) # 오른쪽으로 90도 회전, 앞으로 110 이동
turtle.write("뿡")

turtle.right(90); turtle.fd(20) # 오른쪽으로 90도 회전, 앞으로 20 이동
turtle.write("뿡")

turtle.right(90); turtle.fd(110) # 오른쪽으로 90도 회전, 앞으로 110 이동
turtle.left(180) # 180도 회전


""" 
# 클릭시 종료
turtle.exitonclick()
"""

input("Press any key to exit...")