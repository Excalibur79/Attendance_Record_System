from tkinter import *
import attendance_code

def get_selected(event):
   try:
      global selected
      index=list1.curselection()[0]
      selected=list1.get(index)
      e1.delete(0,END)
      e1.insert(END,selected[1])
      e2.delete(0, END)
      e2.insert(END, selected[2])
      e3.delete(0, END)
      e3.insert(END, selected[3])
      e4.delete(0, END)
      e4.insert(END, selected[4])
   except:
       pass

def delete_command():
    attendance_code.delete(selected[0])

def update_command():
    attendance_code.update(selected[0],name_value.get(),section_value.get(),enroll_value.get(),status_value.get())

def view_command():
    list1.delete(0,END)
    for row in attendance_code.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in attendance_code.search(name_value.get(),section_value.get(),enroll_value.get(),status_value.get()):
        list1.insert(END,row)
def insert_command():

    attendance_code.insert(name_value.get(),section_value.get(),enroll_value.get(),status_value.get())
    view_command()



window=Tk()

window.wm_title("Attendance_Record")

b3=Button(window,text="VIEW ALL",command=view_command)
b3.grid(row=6,column=3)

b4=Button(window,text="UPDATE",command=update_command)
b4.grid(row=8,column=3)

b4=Button(window,text="CLOSE",command=window.destroy)
b4.grid(row=9,column=3)

b5=Button(window,text="SEARCH",command=search_command)
b5.grid(row=7,column=3)

b6=Button(window,text="ADD RECORD",command=insert_command)
b6.grid(row=11,column=0)

b6=Button(window,text="DELETE RECORD",command=delete_command)
b6.grid(row=11,column=1)

l1=Label(window,text="NAME :")
l1.grid(row=0,column=0)

l2=Label(window,text="SECTION :")
l2.grid(row=0,column=2)

l3=Label(window,text="ENROLLMENT NO. :")
l3.grid(row=1,column=0)

l4=Label(window,text="STATUS :")
l4.grid(row=1,column=2)

l5=Label(window,text="R E C O R D -")
l5.grid(row=4,column=0)

name_value=StringVar()
e1=Entry(window,textvariable=name_value)
e1.grid(row=0,column=1)

section_value=StringVar()
e2=Entry(window,textvariable=section_value)
e2.grid(row=0,column=3)


enroll_value=StringVar()
e3=Entry(window,textvariable=enroll_value)
e3.grid(row=1,column=1)


status_value=StringVar()
e4=Entry(window,textvariable=status_value)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=5,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected)

sb1=Scrollbar(window)
sb1.grid(row=4,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

window.mainloop()



