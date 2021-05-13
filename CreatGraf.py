from tkinter import *
from tkintertable import TableCanvas, TableModel
from tkinter import filedialog as fd


root = Tk()
root.title('Ручное создание графа')
root.geometry('640x480')

colVerticesVar = StringVar()
startWayVar = StringVar()
endWayVar = StringVar()
blockVerticesVar = StringVar()


mainMenuButton = Button(text='Главное меню') #, command=insert_text)
mainMenuButton.pack()
str_vertices = Label(text = 'Введите количество вершин: ')
str_vertices.pack()
numOfVertices = Entry(root, bg='white', font=30, width = 3, justify = CENTER, textvariable = colVerticesVar)
numOfVertices.pack()
ismarried = IntVar()
ismarried_checkbutton = Checkbutton(text="Сгенерировать веса", variable=ismarried)
ismarried_checkbutton.pack()
str_table = Label(text = 'Укажите связи между вершинами графа: ')
str_table.pack()

tframe = Frame(root)
tframe.pack()
table = TableCanvas(tframe, rows=5, cols=5, cellwidth = 3) #width  height
table.show()

wayFrame = Frame(root)
wayFrame.pack()
str_way1 = Label(wayFrame, text = 'Из какой вершины в какую нужно попасть: из')
str_way1.pack(side = LEFT)
start_way = Entry(wayFrame, bg='white', font=30, width = 3, justify = CENTER, textvariable = startWayVar)
start_way.pack(side = LEFT)
str_way2 = Label(wayFrame, text = ' в ')
str_way2.pack(side = LEFT)
end_way = Entry(wayFrame, bg='white', font=30, width = 3, justify = CENTER, textvariable = endWayVar)
end_way.pack()
blockFrame = Frame(root)
blockFrame.pack()
str_blockVertices = Label(blockFrame, text = 'Номера заблокированных к обходу вершин через запятую')
str_blockVertices.pack(side = LEFT)
block_Vertices = Entry(blockFrame, bg='white', font=30, width = 20, justify = CENTER, textvariable = blockVerticesVar)
block_Vertices.pack()
creatGrafButton = Button(text='Создать граф') #, command=insert_text)
creatGrafButton.pack()


root.mainloop()

