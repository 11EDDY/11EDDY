

import tkinter

#ventana=tkinter.Tk()
#ventana.geometry("400x300")

#etiqueta=tkinter.Label(ventana,text="eddy",bg = "blue")
#etiqueta.pack(fill=tkinter.X)

#def saludo(nombre):
    #print("hola"+ nombre)
    
#boton1=tkinter.Button(ventana,text="preciona", command=lambda:saludo("python"))
#boton1.pack()

#cajaTexto=tkinter.Entry(ventana, font = "helvetica 25")
#cajaTexto.pack()

#etiqueta=tkinter.Label(ventana)
#etiqueta.pack()

#def textoDeLaCaja():
    #text20=cajaTexto.get()
    #etiqueta["text"]=text20
    
#boton1=tkinter.Button(ventana,text="click", command=textoDeLaCaja)
#boton1.pack()

ventana=tkinter.Tk()
ventana.geometry("400x300")

boton1=tkinter.Button(ventana,text="boton1",width=10,height=5)
boton2=tkinter.Button(ventana,text="boton2",width=10,height=5)
boton3=tkinter.Button(ventana,text="boton3",width=10,height=5)

boton1.grid(row=0,column=0)
boton2.grid(row=1,column=1)
boton3.grid(row=2,column=2)

ventana.mainloop()
