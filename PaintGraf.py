import tkinter as tk
import math
import random

#root = tk.Tk()
#root.iconbitmap('Graf.ico')
#root.title('Нахождение пути по графу')
#root.geometry('640x480')
#c = tk.Canvas(width = 500, height = 500, bg = 'white')
#c.focus_set()
#c.pack()

#weith = 500
#height = 500
#colVerticesVar = 10
#lineWidth = 3
#ball_radius = 25
#graf_radius = ball_radius * 5
#sector = 360 / colVerticesVar 

class App(tk.Tk):
	colors = ("red", "yellow", "green", "blue", "orange")
	colVerticesVar = 10
	lineWidth = 3
	ball_radius = 25
	graf_radius = ball_radius * 5
	sector = 360 / colVerticesVar 
	flag = False
	koordinati = {}

	def __init__(self):
		super().__init__()
		self.geometry('640x480')
		self.title('Удаление элментов холста')
		self.iconbitmap('Graf.ico')
		self.canvas = tk.Canvas(self, width = 450, height = 450, bg='white')
		frame = tk.Frame(self)
		generate_btn = tk.Button(frame, text='Создавать элементы',
								 command=self.generate_items)
		clear_btn = tk.Button(frame, text='Удалить элементы',
							   command=self.clear_items)
		self.canvas.pack()
		frame.pack(fill=tk.BOTH)
		generate_btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		clear_btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		self.update()
		self.width = self.canvas.winfo_width()
		self.height = self.canvas.winfo_height()

		self.canvas.bind("<Button-1>", self.on_click)
		self.generate_items()

	def on_click(self, event):
		item = self.canvas.find_withtag(tk.CURRENT)
		#item.itemconfig(fill = 'red')
		if self.canvas.itemconfig(item)["fill"][4] == 'red':
			self.canvas.itemconfig(item, fill = 'white')
			self.flag = False
		else:
			self.canvas.itemconfig(item, fill = 'red')
			self.flag = True


	def generate_items(self):
		self.clear_items()
		for i in range(self.colVerticesVar):
			x = self.width / 2 - self.ball_radius - self.graf_radius * math.sin(math.radians(i * self.sector))
			y = self.height / 2 - self.ball_radius - self.graf_radius * math.cos(math.radians(i * self.sector))
			color = random.choice(self.colors)
			
			self.canvas.create_oval(x, y, x + 2 * self.ball_radius, y + 2 * self.ball_radius, fill=color, width = self.lineWidth)
	def clear_items(self):
		self.canvas.delete(tk.ALL)

if __name__ == "__main__":
	app = App()
	app.mainloop()




'''
for i in range(colVerticesVar):
	x0 = weith / 2 - ball_radius - graf_radius * math.sin(math.radians(i * sector))
	y0 = height / 2 - ball_radius - graf_radius * math.cos(math.radians(i * sector))
	x1 = x0 + 2 * ball_radius 
	y1 = y0 + 2 * ball_radius	
	#c.create_line(x0 + ball_radius, y0 + ball_radius, x0 + ball_radius + 2 * graf_radius , y0 + ball_radius, width = lineWidth)
	c.create_oval(x0, y0, x1, y1, fill = 'white', width = lineWidth)

def on_click(event):
    item = canvas.find_withtag(tk.CURRENT)
    canvas.delete(item)

root.mainloop()
'''
