def circle(event):
draw(keypress,oldx,oldy,newx,newy)
if keypress=='c':
	draw_circle = canvas.create_oval(oldx,oldy,newx,newy, fill=color)