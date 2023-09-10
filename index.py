from tkinter import *
import pymysql

win = Tk()                   #win is object of TK class
def login ():
		
		user=uid.get()
		password=pwd.get()
		#print("user id =",user," ","password =",password)
		conobj=pymysql.connect(host="localhost",user="root",password="",port=3308)
		curobj=conobj.cursor()
		curobj.execute('use StudentPro;')
		test=f'select * from user where nuid ="{user}" and npwd ="{password}";'
		curobj.execute(test)
		record=curobj.fetchall()
		#print(record)
		if len (record):
			print("welcome to home page")
			win3=Tk()

			def Del():
					win5=Tk()
					def Delete():
						D=duid.get()
						conobj=pymysql.connect(host="localhost",user="root",password="",port=3308)
						curobj=conobj.cursor()
						curobj.execute('use StudentPro;')
						r=f'delete from user where nuid = "{D}";'
						print(" record is deleted")
						curobj.execute(r)
						conobj.commit()
						curobj.close()
						conobj.close()
						win5.destroy()
					win5.title("Delete student")
					win5.maxsize(height =700,width=700)
					win5.minsize(height =700,width=700)
					Label ( win5 , text="Enter User Id",font = ("Baskerville Old Face",15),fg="red").place(x=150,y=100)
					duid=Entry (win5,font =("Baskerville Old Face",15),bg="blue",fg="white")
					duid.place(x=400,y=100)
					Button(win5,text="Delete Student",bg="brown",fg="white",font=("Baskerville Old Face",20),command = Delete).place(x=250,y=250)
			def Search():
				win4=Tk()
				def Find():
						F=suid.get()
						conobj=pymysql.connect(host="localhost",user="root",password="",port=3308)
						curobj=conobj.cursor()
						curobj.execute('use StudentPro;')
						r=f'select * from user where nuid = "{F}";'
						curobj.execute(r)
						record1=curobj.fetchall()
						print(record1)
						curobj.close()
						conobj.close()
						win4.destroy()
				win4.title("search student")
				win4.maxsize(height =700,width=700)
				win4.minsize(height =700,width=700)
				Label ( win4 , text="Enter User Id",font = ("Baskerville Old Face",15),fg="red").place(x=150,y=100)
				suid=Entry (win4,font =("Baskerville Old Face",15),bg="blue",fg="white")
				suid.place(x=400,y=100)
				Button(win4,text="Search",bg="brown",fg="white",font=("Baskerville Old Face",20),command = Find).place(x=250,y=250)
				win4.mainloop()
			def details():
				conobj=pymysql.connect(host="localhost",user="root",password="",port=3308)
				curobj=conobj.cursor()
				curobj.execute('use StudentPro;')
				curobj.execute('select * from user;')
				record = curobj.fetchall()
				for A,B,C,D,E,F in record :
						print(A," ",B," ",C," ",D," ",E," ",F)
			def exit():
				win3.destroy()
			win3.title("Home Page")
			win3.maxsize(height =700,width=700)
			win3.minsize(height =700,width=700)
			Button(win3,text="Add New Student",bg="brown",fg="white",font=("Baskerville Old Face",20),command=NewUser).place(x=150,y=100)
			Button(win3,text="Delete Student",bg="red",fg="white",font=("Baskerville Old Face",20),command=Del).place(x=450,y=100)
			Button(win3,text="Search Student Detail",bg="red",fg="white",font=("Baskerville Old Face",20),command =Search).place(x=150,y=200)
			Button(win3,text="All Student Details",bg="red",fg="white",font=("Baskerville Old Face",20),command=details).place(x=450,y=250)
			Button(win3,text="Exit",bg="red",fg="white",font=("Baskerville Old Face",20),command=exit).place(x=250,y=400)
			
			win3.mainloop()
		else :
			print("try again")
				
				
		curobj.close()
		conobj.close()
		
			
def reset ():
		uid.delete(0,END)
		pwd.delete(0,END)
def exit ():
		win.destroy()	
def NewUser  ():
	def Save():
		a =fname.get()
		b=lname.get()
		c=nuid.get()
		d=dname.get()
		e=""
		if radVar.get() == 0:
				e ="Male"
		if radVar.get() == 1:
				e="Female"
		f=npwd.get()
		#print(a," " ,b," ",c," ",d," ",e," ",f)
		conobj=pymysql.connect(host="localhost",user="root",password="",port=3308)
		curobj=conobj.cursor()
		curobj.execute('use StudentPro;')
		r=' insert into user values ("{fname}","{lname}","{nuid}","{dname}","{var}","{npwd}");'
		r1=r.format(fname =a, lname = b, nuid = c, dname = d, var = e, npwd =f)
		curobj.execute(r1)
		conobj.commit()
		curobj.close()
		conobj.close()
		win1.destroy()
		
	def Reset():
		fname.delete(0,END)
		lname.delete(0,END)
		nuid.delete(0,END)
		dname.delete(0,END)
		#r1.delete(0,END)
		#r2.delete(0,END)
		npwd.delete(0,END)
	win1=Tk()
	win1.title("Registration Page")
	win1.maxsize(height =750,width=750)
	win1.minsize(height =750,width=750)
	win1.configure(bg="cyan")
	Label ( win1 , text="REGISTRATION HERE",font = ("Baskerville Old Face",25),fg="white",bg="pink").place(x=230,y=30)
	Label ( win1 , text="Enter First Name",font = ("Baskerville Old Face",15),fg="black",bg="silver").place(x=170,y=100)
	fname=Entry (win1,font =("Baskerville Old Face",15),bg="orange",fg="black")
	fname.place(x=400,y=100)
	
	Label ( win1 , text="Enter Last Name",font = ("Baskerville Old Face",15),fg="black",bg="silver").place(x=170,y=170)
	lname=Entry (win1,font =("Baskerville Old Face",15),bg="orange",fg="black")
	lname.place(x=400,y=170)

	Label ( win1 , text="Enter User Id",font = ("Baskerville Old Face",15),fg="black",bg="silver").place(x=170,y=240)
	nuid=Entry (win1,font =("Baskerville Old Face",15),bg="orange",fg="black")
	nuid.place(x=400,y=240)

	Label ( win1 , text="Enter Dept Name",font = ("Baskerville Old Face",15),fg="black",bg="silver").place(x=170,y=310)
	"""menu=StringVar()
	menu.set("select any dept")
	drop=OptionMenu(win1,menu,"BSC.CS","ITM","IST")
	drop.place(x=400,y=310)"""
	dname=Entry (win1,font =("Baskerville Old Face",15),bg="orange",fg="black")
	dname.place(x=400,y=310)

	Label ( win1 , text="Select Gender",font = ("Baskerville Old Face",15),fg="black",bg="silver").place(x=170,y=380)
	radVar=IntVar()
	r1=Radiobutton( win1,text="Male",variable=radVar,font =("Baskerville Old Face",15),value=1)
	r1.place(x=400,y=380)
	r2=Radiobutton( win1,text="Female",variable=radVar,font =("Baskerville Old Face",15),value=2)
	r2.place(x=500,y=380)

	Label ( win1 , text="Enter New Password",font = ("Baskerville Old Face",15),fg="black",bg="silver").place(x=170,y=500)
	npwd=Entry (win1,font =("Baskerville Old Face",15),bg="orange",fg="black",show="*")
	npwd.place(x=400,y=500)

	Button(win1,text="Submit",bg="green",fg="black",font=("Baskerville Old Face",15),command =Save).place(x=300,y=530)
	Button(win1,text="Reset",bg="green",fg="black",font=("Baskerville Old Face",15), command = Reset).place(x=450,y=530)

	win1.mainloop()	
win.title("Student Database System")
win.maxsize(height =550,width=750)
win.minsize(height =550,width=750)

Label ( win , text="PLEASE LOGIN HERE",font = ("Baskerville Old Face",25),fg="white",bg="blue",relief=RAISED).place(x=200,y=50)

Label ( win , text="Enter User ID",font = ("Baskerville Old Face",15),fg="white",bg="purple").place(x=10,y=130)

uid=Entry (win,font =("Baskerville Old Face",15),fg="red",bg="black")
uid.place(x=150,y=130)


Label ( win , text="Enter Password",font = ("Baskerville Old Face",15),fg="white",bg="purple").place(x=10,y=230)

pwd=Entry (win,font =("Baskerville Old Face",15),fg="red",bg="black",show="*")
pwd.place(x=150,y=230)


Button(win,text="Login",bg="red",fg="white",font=("Baskerville Old Face",15) ,command = login,activebackground="blue",activeforeground="red",relief=RAISED).place(x=180,y=330)#SUNKEN
Button(win,text="Reset",bg="white",fg="black",font=("Baskerville Old Face",15),command = reset).place(x=300,y=330)
Button(win,text="Exit",bg="green",fg="black",font=("Baskerville Old Face",15),command = exit).place(x=410,y=330)
Button(win,text="New User Click Here",bg="green",fg="black",font=("Baskerville Old Face",15),command = NewUser).place(x=300,y=430)          #/n can be used


win.mainloop ()