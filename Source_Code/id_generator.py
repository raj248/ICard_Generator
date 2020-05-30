from PIL import Image, ImageDraw, ImageFont, ImageEnhance

font_bold = './Montserrat-Bold.ttf'
font_italic = './Montserrat-SemiBoldItalic.ttf'
save_folder = '../Generated/'
def GenerateID(stu_details):
	size = (680,360)
	base = Image.new("RGBA",size , (255,255,255))

	draw = ImageDraw.Draw(base)

	WriteFields(draw)
	WriteSignSpace(draw)
	WriteSchoolInfo(draw)

	FillStudentDetails(draw,stu_details)

	if(stu_details[8]!=''):
		StudentPic(base,stu_details[8])
	SchoolLogo(base)

#	draw_grid(base)
	base.show()
	if(stu_details[2]==''):
		stu_details[2]='New'
	base.save(save_folder + stu_details[2] + '.png')


def WriteFields(img_draw_object):
	d = img_draw_object
	fnt = ImageFont.truetype(font_bold,23)
	''' ---Writing Field Names---'''	
	d.rectangle((30,80,150,240),outline='black')
	name = 'Name: '
	d.text((185,100),name,font=fnt,fill=(0,0,0))
	clas = "Class & Sec:"
	d.text((185,140),clas,font=fnt,fill='black')
	roll = 'Roll:'
	d.text((475,140),roll,font=fnt,fill='black')
	studentid ="Stud ID:   "
	d.text((185,180),studentid,font=fnt,fill='black')
	dob = 'D.O.B:'
	d.text((456,180),dob,font=fnt,fill='black')
	phno='Ph. No:  '
	d.text((185,220),phno,font=fnt,fill='black')
	add ='Add: '
	d.text((185,260),add,font = fnt,fill='black')

	''' ---Field Space---'''
	d.line((270,125,600,125),width=2,fill='grey')
	d.line((335,165,450,165),width=2,fill='grey')
	d.line((530,165,610,165),width=2,fill='grey')
	d.line((530,205,670,205),width=2,fill='grey')
	d.line((290,205,440,205),width=2,fill='grey')
	d.line((280,245,650,245),width=2,fill='grey')
	d.line((250,285,650,285),width=2,fill='grey')

def WriteSignSpace(img_draw_object):
	d = img_draw_object
	signp = 'Principal\'s \nSignature'
	fnt = ImageFont.truetype(font_bold,20)
	d.text((35,300),signp,font=fnt,fill=(128,128,128,60)) 
	signp = 'Student\'s \nSignature'
	d.text((185,300),signp,font=fnt,fill=(128,128,128,60)) 
	signp = 'Class Teacher\'s \nSignature'
	d.text((410,300),signp,font=fnt,fill=(128,128,128,60)) 	

def WriteSchoolInfo(img_draw_object):
	d = img_draw_object
	size = (680,360)
	soe = "School Of Excellence"
	fnt=ImageFont.truetype(font_bold,30)
	w,h = fnt.getsize(soe)
	d.text(((size[0]-w)/2,0),soe,font=fnt,fill='black')
	fnt = ImageFont.truetype(font_italic,17)
	add = 'Khichripur, Delhi-91'
	d.text((190,30),add,font=fnt,fill='black')
	s_id = 'School ID: 1002400'
	d.text((390,30),s_id,font=fnt,fill='black')
	session = 'Session: 2020-21'
	d.text((20,30),session,font=fnt,fill='black')

def FillStudentDetails(img_draw_object, details):
	d = img_draw_object
	name = details[0]
	clas = details[1]
	roll = details[2]
	sec = details[3]
	dob = details[4]
	stu_id = details[5]
	phno = details[6]
	add = details[7]

	fnt = ImageFont.truetype(font_italic,20)

	w,h = fnt.getsize(name)
	d.text((290,100+h/5),name,font=fnt,fill=(20,20,20))
	w,h = fnt.getsize(clas)
	d.text((355,140+h/5),clas,font=fnt,fill=(20,20,20))	
	w,h = fnt.getsize(sec)
	d.text((410,140+h/5),sec,font=fnt,fill=(20,20,20))	
	w,h = fnt.getsize(roll)
	d.text((545,140+h/5),roll,font=fnt,fill=(20,20,20))	
	w,h = fnt.getsize(dob)
	d.text((550,180+h/5),dob,font=fnt,fill=(20,20,20))	
	w,h = fnt.getsize(stu_id)
	d.text((300,180+h/5),stu_id,font=fnt,fill=(20,20,20))
	w,h = fnt.getsize(phno)
	d.text((295,220+h/5),phno,font=fnt,fill=(20,20,20))	
	w,h = fnt.getsize(add)
	d.text((255,260+h/5),add,font=fnt,fill=(20,20,20))

def StudentPic(img_object,img_name):
	# Student pic
	base = img_object
	try:
		img = Image.open(img_name)
		img.thumbnail((140,180))
		base.paste(img,(30,80))
	except:
		print("No Such Image is found")
def SchoolLogo(img_object):
	# School logo
	base = img_object
	img = Image.open('img.jpeg')
	img.thumbnail((100,120))
	base.paste(img,(580,0))


''' -----For Debugging purposes----- '''
def draw_grid(img):  
	size = img.size
	d=ImageDraw.Draw(img)
	for i in range(0, size[0], 10):
		d.line((i,0,i,size[1]),fill=(12,12,12),width=1)
	for j in range(0, size[1], 10):
		d.line((0,j,size[0],j),fill=(128,128,128,60),width=1)


if __name__ == '__main__':
	GenerateID(['','','','','','','','',''])

