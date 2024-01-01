Blog de #Truzz | Python + Tkinter | Cómo crear una GUI
# Cómo crear un formulario de registro usando Python + Tkinter

# Importemos tkinter
de  tkinter  importar  *
#importar tkinter como tk
 
# Manipular datos de campos de registro
def  enviar_datos ():
  nombre_de_usuario  = nombre de  usuario . obtener ()
  contraseña_info  =  contraseña . obtener ()
  fullname_info  =  nombre completo . obtener ()
  edad_info  =  str ( edad . obtener ())
  print ( info_usuario , " \ t " , info_contraseña , " \ t " , info_nombre_completo , " \t " , info_edad )
 
# Abrir y escribir datos en un archivo
  archivo  =  abrir ( "usuario.txt" , "a" )
  archivo _ escribir ( nombre_de_usuario )
  archivo _ escribir ( " \t " )
  archivo _ escribir ( contraseña_info )
  archivo _ escribir ( " \t " )
  archivo _ escribir ( nombre completo_info )
  archivo _ escribir ( " \t " )
  archivo _ escribir ( age_info )
  archivo _ escribir ( " \t \n " )
  archivo _ cerrar ()
  print ( " Nuevo usuario registrado. Nombre de usuario: {} | Nombre completo: {} " . formato ( info_usuario , info_nombre_completo ))
 
# Eliminar datos del evento anterior
  nombre_de_entrada . eliminar ( 0 , FIN )
  entrada_contraseña . eliminar ( 0 , FIN )
  entrada_nombre_completo . eliminar ( 0 , FIN )
  edad_entrada . eliminar ( 0 , FIN )

# Crear nueva instancia - Clase Tk()  
miventana  =  Tk ()
miventana _ geometría ( "650x550" )
miventana _ title ( "Formulario de registro - Python + Tkinter" )
miventana _ redimensionable ( Falso , Falso )
miventana _ configuración ( fondo  =  "#213141" )
main_title  =  Etiqueta ( texto  =  "Python Form | TRUZZ BLOGG" , fuente  = ( "Cambria" , 14 ), bg  =  "#56CD63" , fg  =  "negro" , ancho  =  "500" , alto  =  "2" )
título_principal . paquete ()

# Definir campos de etiquetas
username_label  =  Etiqueta ( texto  =  "Nombre de usuario" , bg  =  "#FFEEDD" )
nombre_usuario_etiqueta . lugar ( x  =  22 , y  =  70 )
contraseña_etiqueta  =  Etiqueta ( texto  =  "Contraseña" , bg  =  "#FFEEDD" )
etiqueta_contraseña . lugar ( x  =  22 , y  =  130 )
fullname_label  =  Etiqueta ( texto  =  "Nombre completo" , bg  =  "#FFEEDD" )
nombre_completo_etiqueta . lugar ( x  =  22 , y  =  190 )
age_label  =  Etiqueta ( texto  =  "Edad" , bg  =  "#FFEEDD" )
etiqueta_edad . lugar ( x  =  22 , y  =  250 )
 
# Obtener y almacenar datos de los usuarios
nombre de usuario  =  StringVar ()
contraseña  =  StringVar ()
nombre completo  =  StringVar ()
edad  =  StringVar ()
 
nombre_de_entrada  =  Entrada ( variable de texto  = nombre de  usuario , ancho  =  "40" )
contraseña_entrada  =  Entrada ( variable de texto  =  contraseña , ancho  =  "40" ,   mostrar  =  "*" )
fullname_entry  =  Entrada ( variable de texto  = nombre  completo , ancho  =  "40" )
edad_entrada  =  Entrada ( variable de texto  =  edad , ancho  =  "40" )
 
nombre_de_entrada . lugar ( x  =  22 , y  =  100 )
entrada_contraseña . lugar ( x  =  22 , y  =  160 )
entrada_nombre_completo . lugar ( x  =  22 , y  =  220 )
edad_entrada . lugar ( x  =  22 , y  =  280 )
 
# Botón de enviar
enviar_btn  =  Botón ( miventana , texto  =  "Enviar información" , ancho  =  "30" , alto  =  "2" , comando  =  enviar_datos , bg  =  "#00CD63" )
enviar_btn . lugar ( x  =  22 , y  =  320 )

miventana _ bucle principal ()
