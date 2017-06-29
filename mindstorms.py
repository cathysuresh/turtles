import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("blue")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(15)




	degrees = 10
	for i in range(36):
		brad.forward(100)
		brad.right(90)

		brad.forward(100)
		brad.right(90)

		brad.forward(100)
		brad.right(90)

		brad.forward(100)
		brad.right(90)
		brad.left(degrees)
		degrees += 10



	

	window.exitonclick()

	

draw_square()


