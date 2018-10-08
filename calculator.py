import tkinter as tk

win_width = 250
win_height = 250
bg_color = "red"
expression = ""


def changeBackgroundColor(color:str):
	global logo_screen, app
	logo_screen.configure(bg=color)
	# app.update()


def setText():	
	global expression, entry
	entry.configure(text=expression)


def callback():
	global expression
	expression = ""
	setText()


def parse(express):
	global expression
	if "^" in express :
		try: 
			number = list(map(int, express.split("^")))
			if len(number) == 2:
				expression = str(number[0] ** number[-1])
			return True
		except:
			expression = ""

	elif "*" in express :
		try:
			number = list(map(int, express.split("*")))
			print(number)
			if len(number) == 2:
				expression = str(number[0] * number[-1])
			return True
		except:
			expression = ""
	elif "/" in express :
		try:
			number = list(map(int, express.split("/")))
			if len(number) == 2 and number[-1] != 0:
				expression = str(number[0] / number[-1])
			return True
		except:
			expression = ""
	elif "+" in express :
		try: 
			number = list(map(int, express.split("+")))
			if len(number) == 2:
				expression = str(number[0] + number[-1])
			return True
		except:
			expression = ""
	elif "-" in express :
		try:
			number = list(map(int, express.split("-")))
			if len(number) == 2:
				expression = str(number[0] - number[-1])
			return True
		except:
			expression = ""
	else:
		return False


def power():
	global expression
	if not parse(expression) and len(expression) > 0:
		expression = expression + "^"
	try:
		int(expression)
		expression = expression + "^"
	except:
		pass
	changeBackgroundColor("red")
	setText()


def add():
	global expression
	if not parse(expression) and len(expression) > 0:
		expression = expression + "+"
	try:
		int(expression)
		expression = expression + "+"
	except:
		pass
	changeBackgroundColor("green")
	setText()


def sub():
	global expression
	if not parse(expression) and len(expression) > 0:
		expression = expression + "-"
	try:
		int(expression)
		expression = expression + "-"
	except:
		pass
	changeBackgroundColor("blue")
	setText()


def mul():
	global expression
	if not parse(expression) and len(expression) > 0:
		expression = expression + "*"
	try:
		int(expression)
		expression = expression + "*"
	except:
		pass
	changeBackgroundColor("blue")
	setText()


def div():
	global expression
	if not parse(expression) and len(expression) > 0:
		expression = expression + "/"
	try:
		int(expression)
		expression = expression + "/"
	except:
		pass
	changeBackgroundColor("yellow")
	setText()


def n1():
	global expression
	expression = expression + str(1)
	setText()


def n2():
	global expression
	expression = expression + str(2)
	setText()


def n3():
	global expression
	expression = expression + str(3)
	setText()


def n4():
	global expression
	expression = expression + str(4)
	setText()


def n5():
	global expression
	expression = expression + str(5)
	setText()


def n6():
	global expression
	expression = expression + str(6)
	setText()


def n7():
	global expression
	expression = expression + str(7)
	setText()


def n8():
	global expression
	expression = expression + str(8)
	setText()


def n9():
	global expression
	expression = expression + str(9)
	setText()


def n0():
	global expression
	expression = expression + str(0)
	setText()


app = tk.Tk()
app.title("CalSee")
app.minsize(width=win_width, height=win_height)
app.maxsize(width=win_width, height=win_height)
logo_screen = tk.Frame(app, bg=bg_color, height=win_height, width=win_width)
logo_screen.pack()
add_button = tk.Button(logo_screen, text=" + ", height=2, width=4, command=add, bd=0)
sub_button = tk.Button(logo_screen, text=" - ", height=2, width=4, command=sub, bd=0)
mul_button = tk.Button(logo_screen, text=" * ", height=2, width=4, command=mul, bd=0)
div_button = tk.Button(logo_screen, text=" / ", height=2, width=4, command=div, bd=0)
c_button = tk.Button(logo_screen, text=" C ", height=2, width=4, command=callback, bd=0)
equ_button = tk.Button(logo_screen, text=" ^ ", height=2, width=4, command=power, bd=0)
i_button = tk.Button(logo_screen, text=" 1 ", height=2, width=4, command=n1, bd=0)
ii_button = tk.Button(logo_screen, text=" 2 ", height=2, width=4, command=n2, bd=0)
iii_button = tk.Button(logo_screen, text=" 3 ", height=2, width=4, command=n3, bd=0)
iv_button = tk.Button(logo_screen, text=" 4 ", height=2, width=4, command=n4, bd=0)
v_button = tk.Button(logo_screen, text=" 5 ", height=2, width=4, command=n5, bd=0)
vi_button = tk.Button(logo_screen, text=" 6 ", height=2, width=4, command=n6, bd=0)
vii_button = tk.Button(logo_screen, text=" 7 ", height=2, width=4, command=n7, bd=0)
viii_button = tk.Button(logo_screen, text=" 8 ", height=2, width=4, command=n8, bd=0)
ix_button = tk.Button(logo_screen, text=" 9 ", height=2, width=4, command=n9, bd=0)
x_button = tk.Button(logo_screen, text=" 0 ", height=2, width=4, command=n0, bd=0)
entry = tk.Label(logo_screen, height=2, bd=0)
logo_screen.pack()
entry.place(relx = 0.02, rely=0.05)
i_button.place(relx=0.02, rely=0.2)
ii_button.place(relx=0.27, rely=0.2)
iii_button.place(relx=0.52, rely=0.2)
c_button.place(relx=0.77, rely=0.2)
iv_button.place(relx=0.02, rely=0.4)
v_button.place(relx=0.27, rely=0.4)
vi_button.place(relx=0.52, rely=0.4)
mul_button.place(relx=0.77, rely=0.4)
vii_button.place(relx=0.02, rely=0.6)
viii_button.place(relx=0.27, rely=0.6)
ix_button.place(relx=0.52, rely=0.6)
div_button.place(relx=0.77, rely=0.6)
x_button.place(relx=0.02, rely=0.8)
add_button.place(relx=0.27, rely=0.8)
sub_button.place(relx=0.52, rely=0.8)
equ_button.place(relx=0.77, rely=0.8)
app.mainloop()