#Proyecto #2
#---------------------------------------------------------
lista = []
listaX = []
listaY = []
#---------------------------------------------------------
cantidad_numeros = input("\nNumeros que quiera agregar: ")
cn = 0
ni = 1
#---------------------------------------------------------
while cn<int(cantidad_numeros):
	numero = input(f"Numero {ni}: ")
	#---------------------------------
	lista.append(numero)
	#---------------------------------
	ni += 1
	cn += 1
#-----------------------------
print(f"\nTu lista:\n{lista}")
#-----------------------------
ParametroX = (len(lista)-1)
#-------------
def suma(x,y):
	#-------------------------------
	if ( x>len(lista)-1 ):
		print("\n###ERROR 404####\n")
	#-------------------------------
	else:
		#--------------------------------
		f = 1
		i = 0
		n = 0
		a = -1
		b = 0
		#--------------------------------
		for Y in str(y):
			listaY.append(Y)
		print(f"\nLista de Y:\n{listaY}")
		#--------------------------------
		for X in lista[x]:
			listaX.append(X)
		print(f"\nLista de X:\n{listaX}")
		#
		residuo_de_Y = y
		#-----------------------------
		while n<len(lista):
			for l in lista[::-1][i:f]:
				#------------------------------------------
				res = 0
				#-------------------------------------------------------------
				sumaY = "".join(map(str,listaY[::-1][0:(len(str(lista[x])))]))
				print(f"\nSuma de Y:\n{sumaY}")
				#-------------------------------------------------------------
				res = int(lista[x+b]) + int(str(sumaY[::-1]))
				#-------------------------------------------------------------
				print(f"\nSuma: {lista[x+b]} + {listaY[-1]}\n")
				#-------------------------------------------------------------
				if (f == (len(lista))) or residuo_de_Y == 0:
					lista[0] = int(lista[0]) + residuo_de_Y
					n = len(lista)
				else:
					#----------------------------------------------
					listaR = []
					#----------------------------------------------
					for r in str(res):
						listaR.append(r)
					print(f"\nResultado de la suma:\n{res}")
					print(f"\nLista de R:\n{listaR}")
					#----------------------------------------------
					if (len(listaR)<=len(listaX)):
						#------------------------------------------
						residuo_de_Y = y - int(str(sumaY[::-1]))
						print(f"\nResiduo de Y:\n{residuo_de_Y}")
						#------------------------------------------
						listaY.clear()
						#------------------------------------------
						for Y in str(residuo_de_Y):
							listaY.append(Y)
						print(f"\nLista de Y:\n{listaY}")
						#------------------------------------------
						lista[x+b] = str(res)
						#------------------------------------------
						listaR = []
						#------------------------------------------
						f += 1
						i += 1		
						n += 1
						a -= 1
						b -= 1
						sumaY = 0
					else:
						sumaY = 0
						f += 1
						i += 1		
						n += 1
						a -= 1
						b -= 1
		print(f"\nLista Final:\n{lista}")


#--------------------------------------------------------------------------------------------------------------------------------	
suma(int(input(f"\nElige un parametro entre (0,{ParametroX}): ")),int(input("\nDame una cantidad a sumar: ")) )
