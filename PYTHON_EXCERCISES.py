#!/usr/bin/env python
# coding: utf-8

# Introducción a Python A lo largo de este cuaderno explicaremos algunos conceptos básicos de Python. Los temas específicos que cubriremos en estos cuadernos introductorios son los siguientes:
# 
# ¿Qué es Python? Objetos avanzados: Listas y diccionarios Empaquetando código - Funciones Planteamiento del problema: Imagina que queremos crear un directorio que contenga toda la información de los estudiantes de nuestro club. Para ello, necesitaremos construir paso a paso la idea completa del proyecto.
# 
# Para ello, necesitamos saber sobre tipos de variables, objetos avanzados como listas y diccionarios, cómo crear funciones para operar algunos valores y cómo crear nuevos objetos.
# 

# 
# **Ejemplo 5** Función ValidarFecha: Recibe un día, mes y año correspondiente a una fecha y devuelve si la fecha es correcta o no. Simplemente miramos si el día indicado es mayor que 1 y menor que los días del mes. Si introducimos un mes incorrecto, la función DiasDelMes devuelve 0 por lo tanto la fecha va a ser incorrecta. Parámetros de entrada: día, mes y año Dato devuelto: Valor lógico indicando si es correcta (Verdadero) o no (Falso)

# In[2]:


#Ejemplo 5
def ValidarFecha(dia,mes,año):
    mes31 = (1,3,5,7,8,10,12)
    mes30 = (4,6,9,11)
    dia = DiaDelMes (dia,mes)
    correcto = False
    if mes in mes31:
        if(dia>= 1 and dia<= 31):
            correcto = True
    elif mes == 2:
        if(dia>=1 and dia<=28):
            correcto = True
    return correcto

def DiaDelMes (dia,mes):
    if (mes<= 0 and mes >12):
        return 0
    else:
        return dia

dia,mes,año = int(input('Ingresa el día:')), int(input('Mes:')), int(input('Año:'))
ValidarFecha(dia,mes,año)


# **¡A resolver el reto!** Vamos a prodecer a crear una lista de diccionarios, esto es, un directorio de estudiantes de SKILLS FOR WOMEN IN TECH que participarán en una edición en línea.
# 
# Cada estudiante debe tener los siguientes atributos:
# 
# Nombre Edad Temas Menores de edad Puedes asignar los datos a mano o utilizar funciones aleatorias para llenar los campos.

# In[7]:


from posixpath import split
from pprint import pprint
padawans=[]

def registrationPadawans(name,lastname,age,subjects):
    subjects= subjects.lower().split(", ")
    legalAge= True if age >= 18 else False
    try:
        padawans.append({"name":name, "lastname":lastname, "age":age, "subjects":subjects})
    except:
        return "Data were not added"
    return "\n\n SUCCESSFUL REGISTRATION!\n"


while True:
    print('Sign up! Padawan Directory')
    print("1.Add student")
    print("2.View directory") 
    print("3.Exit")
    
    opcion = int(input()) 
    if opcion == 1:
        name = str(input("Enter student name:"))
        lastname= str(input("Enter last name:"))
        age = int(input("Enter age:"))
        if age>=18:
            print('\nYou are of legal age\n')
        else:
            print('\nYou are under age\n')
        print("Subjects available son:Python,JavaScript,Java")
        subjects = str(input("Enter the subjects of your choice:"))
        print(registrationPadawans(name,lastname,age,subjects),"\n\n")
    elif opcion == 2:
        print(padawans)

    elif opcion == 3:
        print("\nByeee")
        break
    else:
        break

