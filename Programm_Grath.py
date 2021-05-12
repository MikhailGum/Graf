# Импортируем все из библиотеки TKinter
from tkinter import *
from tkintertable import TableCanvas, TableModel
from tkinter import filedialog as fd

# Эта библиотека нужна для работы с отправкой URL запросов
import requests

# Создаем главный объект (по сути окно приложения)
root = Tk()
root.attributes("-topmost", True)


# Эта функция срабатывает при нажатии на кнопку "Посмотреть погоду"
def get_weather():
	# Получаем данные от пользователя
	city = cityField.get()
 
	# данные о погоде будем брать с сайта openweathermap.org
	# ниже пропишите свой API ключ, который получите в кабинете пользователя на сайте openweathermap.org
	key = 'b40381843c8ba64551007156d7d31e08'
	# ссылка, с которой мы получим все данные в формате JSON
	url = 'http://api.openweathermap.org/data/2.5/weather'
	# Дополнительные парамтеры (Ключ, город введенный пользователем и единицины измерения - metric означает Цельсий)
	params = {'APPID': key, 'q': city, 'units': 'metric'}
	# Отправляем запрос по определенному URL
	result = requests.get(url, params=params)
	# Получаем JSON ответ по этому URL
	weather = result.json()

	# Полученные данные добавляем в текстовую надпись для отображения пользователю
	info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'


def creat_graf():
    a = Toplevel()
    a.geometry('200x150')
    a['bg'] = 'grey'
    a.overrideredirect(True)
    Label(a, text="About this")\
        .pack(expand=1)
    a.after(5000, lambda: a.destroy())


# вызов Открытия файла
def insert_text():
	file_name = fd.askopenfilename()
	f = open(file_name)
	s = f.read()
	text.insert(1.0, s)
	f.close()

# Настройки главного окна

# Указываем фоновый цвет
root['bg'] = '#03A762'
# Указываем название окна
root.title('Графы')
# Указываем размеры окна
root.geometry('640x480')
# Делаем невозможным менять размеры окна
#root.resizable(width=False, height=False)

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame_top = Frame(root, bg='#A5218F', bd=5)
# Также указываем его расположение
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

# Все то-же самое, но для второго фрейма
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

# Создаем фреймы для кнопок открытия окон
frame_top2 = Frame(root, bg='#A5218F', bd=5)
frame_top3 = Frame(root, bg='#A5218F', bd=5)
frame_top4 = Frame(root, bg='#A5218F', bd=5)

frame_top2.place(anchor='center', relx=0.25, rely=0.15, relwidth=0.25, relheight=0.1)
frame_top3.place(anchor='center', relx=0.75, rely=0.15, relwidth=0.25, relheight=0.1)
frame_top4.place(anchor='center', relx=0.5, rely=0.75, relwidth=0.25, relheight=0.1)

# Создаем текстовое поле для получения данных от пользователя
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack() # Размещение этого объекта, всегда нужно прописывать

# Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()

# Содаем кнопку вызовы окна Создать граф вручную
btn2 = Button(frame_top2, text='Создать граф в ручную', command=creat_graf)
btn2.pack()

# Содаем кнопку вызовы окна Автоматически сгенерировать граф
btn3 = Button(frame_top3, text='Автоматически \n сгенерировать граф', command=get_weather)
btn3.pack()

# Содаем кнопку вызовы окна Открыть шраф из файла
btn4 = Button(frame_top4, text='Открыть граф из файла', command=insert_text)
btn4.pack()

# Создаем текстовую надпись, в которую будет выводиться информация о погоде
info = Label(frame_bottom, text='Погодная информация', bg='#ffb700', font=40)
info.pack()

# Добавление таблицы
#tframe = Frame(root)
#tframe.pack()
#table = TableCanvas(tframe)
#table.show()

# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()