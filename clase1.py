#nombre = input("cual es tu nombre? " ) ejercicio 1
#print("tu nombre es:" , nombre ) 

#nombre = input(" introduzca su nombre:"  ) ejercicio 2
#apellido = input("ïntroduzca sus apellidos:" )
#print("usted es : ",  nombre,  apellido)

#print("what do you call  a bear with no teeth?\n A gummy bear!") ejercicio 3


#A = int(input("entre el primer numero" )) ejercicio 4
#B = int(input("entre el segundo numero" ))
#answer = A + B
#print(" la suma  es: ", answer )

#Ask the user to enter three // ejercicio 5 
#numbers. Add together the first 
#two numbers and then multiply this total by the third. Display the answer as The answer is [answer].

#A = int(input("entre el primer numero: "  )) ejercicio6
#B = int(input("entre el segundo numero: "  ))
#C = int(input("entre el tercer  numero: "  ))

#answer = (A + B  )* C
#print("la respuestra es ", answer )

#nombre = input("Cual es tu nombre:" ) ejercicio 7
#edad = int(input("cual es su edad:" ))
#cumpleano = edad + 1
#print( nombre, " El proximo ano tendras ", cumpleano)

#ejercicio 8
#bill = int(input("cuanto es la cuenta?: " ))
#person = int(input("cuantas personas son?:" ))
#split = float(bill / person)
#print ("cada persona debe pagar:", split )

#ejercicio 9

#dias = int(input("entre el numero de dias: " ))
#horas = dias*24
#min = horas*60
#sec = min*60
#print (dias, "dias tiene")
#print(horas, "horas" )
#print(min, "minutos")
#print(sec, "segundos")

#ejercicio 10
#kilos =int( input("entre el peso:" ))
#libras = float(kilos * 2.204)
#print (kilos, "kilos tienen")
#print(libras, "libras")

 #ejercicio 11

#mayor = int(input("entre un numero mayor que 100"))
#menor = int(input("entre un numero menor qe 10"))
#answer = (mayor // menor)
#print( menor, " cabe dentro de", mayor, answer, "veces")

#ejercicio12
#num1 = int(input("entre el primer numero"))
#num2 = int(input("entre el segundo numero"))
#if num1 > num2:
# print(num2, num1)
#else:
# print(num1, num2)



#ejercicio13
#num = int(input( "entre un numero menor que 20" ))
#if num >= 20:
#    print("rango no valido" )

#else:
#    print("muchas gracias" )

#ejercicio 14

#num = int(input("entre numero entre 10 y 20:"  ))
#if num >= 10 and num <= 20:
#    print ("muchas gracias") 
#else:
# print ("incorrect answer")

#ejercicio 15
#fvcolor = input("entre su color favorito:"  )
#if fvcolor == "red" or fvcolor == "RED"   or fvcolor == "Red": 
#   print("i like red color too")
#else:
#   print("i dont like that color, i prefer red")

#ejercicio 16
#rainy = input("esta lloviendo?"  )
#rainy = str.lower( rainy )
#if rainy == "yes" or  rainy == "si": 
#    windy = input("esta haciendo aire?" )
#   windy = str.lower(windy)
#   if windy == "yes" or windy == "si":
#        print("hace mucho aire para una sombrilla")
#    if windy == "no":
#        print ("coge una sombrilla")
#if rainy == "no":
#    print("que tengas un bue dia")

#ejercicio 17

#age = int(input("entre su edad:" ))
#if age >= 18:
#    print("you can vote")
#elif age == 17:
#    print("you can learn to drive")
#elif age == 16:
#    print("you can buy a lottery ticket")
#elif age < 16:
#    print("you can go to play hide and seek")

#ejercicio 20

#name = input("entre su nombre: " )
#largo = len(name)
#print(largo)

#ejercicio 21
#nombre = input("entre su nomre: " )
#apellido = input("entre su apellido:")
#largo = nombre + apellido
#fun = len(largo)
#print(fun)

#ejercicio  22

#name = input("entre su nombre en minusculas: " )
#apellido = input ("entre su apellido en minusculas")
#name = name.title()
#apellido = apellido.title()
#nombre = name + "" + apellido
#print (nombre)

#forzar al usuario a entrar un numero
num = input("introduzca un numero: " )
while not num.isdigit():
  num = input("introduzca un numero entero: " )
while num.isdigit():
    print("has acabado")
    exit()
