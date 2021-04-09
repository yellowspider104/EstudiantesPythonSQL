from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("API ESTUDIANTES")
root.geometry("600x300")

Id=StringVar()
Nombre=StringVar()
Apellido=StringVar()
Edad=StringVar()

def conexionBDSQL():
	Conexion=sqlite3.connect("BD")
	Cursor=Conexion.cursor()

	try:
		Cursor.execute("CREATE TABLE estudiantes (ID INTEGER PRIMARY KEY AUTOINCREMENT NOMBRE VARCHAR(30) NOT NULL,APELLIDO VARCHAR(70) NOT NULL,EDAD INT NOT NULL)")
		messagebox.showinfo("CONEXION","BASE DE DATOS CREADA EXITOSAMENTE")
	except:
		messagebox.showinfo("CONEXION","SE HA CONECTADO CORRECTAMENTE")

def eliminarBD():
	Conexion=sqlite3.connect("BD")
	Cursor=Conexion.cursor()
	if messagebox.askyesno(message="Se van a perder los datos,realmente desea salir de la aplicacion",title="WARNING"):
		cursor.execute("DROP TABLE empleado")
	else:
		pass
		
def salirAPI():
	valor = messagebox.askquestion("SALIR","Esta seguro que desea salir?")
	if valor=="yes":
		root.destroy()
	
def limpiarCampos():
	Id.set("")
	Nombre.set("")
	Apellido.set("")
	Edad.set("")


def crear():
	Conexion=sqlite3.connect("BD")
	Cursor=Conexion.cursor()
	try:
		datos=Nombre.get(),Apellido.get(),Edad.get()
		Cursor.execute("INSERT INTO estudiantes VALUES(NULL,?,?,?)")
		Conexion.commit()
	except:
		messagebox.showwarning("ERROR")

	limpiarCampos()
	mostrar()

def mostrar():
	Conexion=sqlite3.connect("BD")
	Cursor=Conexion.cursor()
	registros=tree.get_children()
	for elemento in registros:
		tree.delete(elemento)

	try:
		Cursor.execute("SELECT * FROM empleado")
		for row in Cursor:
			tree.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
	except:
		pass



tree=ttk.Treeview(height=10,columns=('#0','#1','#2'))
tree.place(x=0,y=130)
tree.column('#0',width=100)
tree.heading('#0',text="ID", anchor=CENTER)
tree.heading('#1',text="Nombre del Estudiante", anchor=CENTER)
tree.heading('#2',text="Apellido del Estudiante", anchor=CENTER)
tree.column('#3',width=100)
tree.heading('#3',text="EDAD", anchor=CENTER)

def actualizar():
	Conexion=sqlite3.connect("BD")
	Cursor=Conexion.cursor()
	try:
		datos=Nombre.get(),Apellido.get(),Edad.get()
		Cursor.execute("UPDATE estudiantes SET NOMBRE=?, APELLIDO=?,EDAD=? WHERE ID="+Id.get(), (datos))
		Conexion.commit()
	except:
		messagebox.showwarning("ADVERTENCIA","NO SE PUDO COMPLETAR EL ACTUALIZAR REGISTROS")
	limpiarCampos()
	mostrar()

def borrar():
	Conexion=sqlite3.connect("BD")
	Cursor=Conexion.cursor()
	try:
		if messagebox.askyesno(message="Realmente deseas borrar el registro?"):
			Cursor.execute("DELETE FROM estudiantes WHERE ID="+Id.get())
			
	except:
			messagebox.showwarning("ADVERTENCIA","HUBO UN ERROR AL TRATAR DE ELIMINAR")
	limpiarCampos()
	mostrar()

menubar=Menu(root)
menubasedat=Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear/Conectar a la BD ",command=conexionBDSQL)
menubasedat.add_command(label="Eliminar BD " ,command=eliminarBD)
menubasedat.add_command(label="SALIR " ,command=salirAPI)
menubar.add_cascade(label="Inicio",menu=menubasedat)

##falta enlazar el menu y esta todo listo

root.mainloop()