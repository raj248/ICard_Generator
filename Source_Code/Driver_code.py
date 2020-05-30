from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
from id_generator import * 

root = Tk()
root.title('ID Generator')
sec = StringVar()
canvas = Canvas(root, width=180, height=220)
canvas.place(x=350,y=60)

l10 = Label(root, text='ID Card Generator', font='arial 22 bold').place(x=160,y=10)
l1 = Label(root, text='Name')
l1.place(x=10,y=50)
l2 = Label(root, text='Roll No.')
l2.place(x=10, y=90)
l3 = Label(root, text='Section')
l3.place(x=10, y=210)
l4 = Label(root, text='Class')
l4.place(x=10, y=130)
l5 = Label(root, text='D.O.B (DD/MM/YYY)')
l5.place(x=10, y=170)
l6 = Label(root, text='Student ID')
l6.place(x=10, y=250)
l7 = Label(root, text='Phone No.')
l7.place(x=10, y=290)
l8 = Label(root, text='Address')
l8.place(x=10, y=330)
l8 = Label(root, text='(OPTIONAL) Photo Name')
l8.place(x=10, y=370)
l9 = Label(root,text='No Image Selected')
l9.place(x=380,y=250)

e1 = Entry(root, bd=2, width=30)
e1.place(x=70,y=50)
e2 = Entry(root, bd=2, width=10)
e2.place(x=70, y=90)

#e4 = Entry(root, bd=2, width=5)
e3_A = Radiobutton(root, text="A", variable = sec, value='A')
e3_B = Radiobutton(root, text="B", variable = sec, value='B')
e3_C = Radiobutton(root, text="C", variable = sec, value='C')
e3_D = Radiobutton(root, text="D", variable = sec, value='D')

e3_A.place(x=70, y=210)
e3_B.place(x=110, y=210)
e3_C.place(x=150, y=210)
e3_D.place(x=190, y=210)
e3_A.select()

e4 = Spinbox(root, from_=1,to=12)
e4.place(x=70, y=130)
e5 = Entry(root, bd=2, width=10)
e5.place(x=150, y=170)
e6 = Entry(root, bd=2, width=20)
e6.place(x=90, y=250)
e7 = Entry(root, bd=2, width=30)
e7.place(x=90, y=290)
e8 = Entry(root, bd=2, width=30)
e8.place(x=90, y=330)


photo = None
tmp = None
def PreviewPic(*pic):
	try:		
		global tmp
		global photo
		img = Image.open(photo.get())
		l9.config(text='Image Found')
		img.thumbnail((150,190))
		i = ImageTk.PhotoImage(img)
		tmp = i
		canvas.create_image(0,0, image = i, anchor='nw')
		canvas.image = tmp
	except:
		photo.set('')
		canvas.delete('all')
		l9.config(text='No Image Selected')
photo = StringVar()
photo.set('')
photo.trace('w',PreviewPic)


def TakeInput():
	name = e1.get()
	roll = e2.get()
	clas = e4.get() +'th'
	dob = e5.get()
	stu_id = e6.get()
	phno = e7.get()
	addr = e8.get()
	details = [name,clas,roll,sec.get(),dob,stu_id,phno,addr,photo.get()]
	GenerateID(details)
def Clear():
	e1.delete(0,'end')
	e2.delete(0,'end')
	e5.delete(0,'end')
	e6.delete(0,'end')
	e7.delete(0,'end')
	e8.delete(0,'end')
	photo.set('')
def OpenImage():
	filename =  filedialog.askopenfilename(initialdir = "./",title = "Select Image",filetypes = (("all files","*.*"),("jpg files","*.jpg")))
	global photo
	photo.set(filename)
	print(photo.get())


but1 = Button(root, text='Generate', command = TakeInput, bd=2)
but1.place(x = 330, y = 450)
but2 = Button(root, text = 'Close', command = quit, bd=2)
but2.place(x = 130, y = 450)
but3 = Button(root, text = 'Clear', command = Clear, bd=2)
but3.place(x = 230, y = 450)
but4 = Button(root, text='Select Image', command=OpenImage, bd=2)
but4.place(x=30,y=390)

root.geometry('550x500')
root.mainloop()
