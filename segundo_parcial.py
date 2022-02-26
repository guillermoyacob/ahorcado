# Función encargada de llenar la lista que declaramos con guiones, donde cada guión equivale a una leta de la palabra ingresada, esto es así para que el usuario pueda ver la cantidad de letras que se necesitan completar sin ver la palabra.
def generarGuiones():

	contador=0

	while contador < len(palabraString):
		palabraLista.append("_")
		contador+=1

# Función encargada de comparar las posiciones de la palabraLista (la que tiene que adivinar el usuario) con la palabraString (la palabra ingresada que desconoce el jugador), si estas no coinciden en su totalidad retorna falso, en caso contrario si cada una de las letras coinciden retorna verdadero. Esta función es necesaria para saber posteriormente si la palabra ha sido adivinada.
def compara(palabraLista,palabraString):

	contador=0
	
	while contador < len(palabraString):
		if palabraLista[contador]!= palabraString[contador]:
			return False
		else:
			contador+=1	
	return True

# Función encargada de imprimir por consola la lista que contiene en un principio los guiones equivalentes a las letras de la palabra a adivinar.
def mostrarLista(palabraLista):

	print(palabraLista)

# Función encargada de verificar que se hayan introducido la cantidad de caracteres correctos, es decir o 1 caracter (equivalente a una letra) o la palabra completa, si es que el usuario arriesga y quiere adivinar toda la palabra.
def comprueba(valorIngresado):

	if len(valorIngresado) == 1:
		return True
	elif valorIngresado == palabraString:
		return True
	else:
		return False

# Función que busca la letra o la palabra que introduce el jugador. Si hay coincidencia retorna verdadero, en caso contrario retorna falso.
def buscar(valorIngresado):

	if valorIngresado in palabraString or valorIngresado == palabraString:
		return True
	else:
		return False

# Función que se encarga de reemplazar la letra o la palabra que ha intruducido el jugador en la lista de guiones que se muestra al comienzo. Función consecuente a la función buscar.
def reemplazar(valorIngresado, palabraString, palabraLista):

	contador=0

	if valorIngresado == palabraString:
		while contador < len(valorIngresado):
			palabraLista[contador] = valorIngresado[contador]
			contador=contador+1
	else:
		while contador < len(palabraString):
			if valorIngresado == palabraString[contador]:
				palabraLista[contador]=valorIngresado
			contador=contador+1

# La función jugar es la que posibilita el desarrollo del juego, llamando a las demás funciones que hagan falta para esta tarea.
def jugar():
	
	# Estas son las vidas del jugador, las oportunidades que tiene, que se iran decrementando si no acierta.
	vidas=6
	
	generarGuiones()
	
	# Se utiliza un bucle while para el desarrollo del juego, para que el usuario pueda ingresar una letra que crea que corresponde a la palabra o la palabra completa que crea haber adivinado, esto se realiza repetidas veces hasta que no se cumpla la condición del bucle, la cual será primero que el usuario no disponga de vidas para seguir jugando o que la palabra completa haya sido adivinada. En caso de que pase alguna de estas dos cosas se pasará a la siguiente sección del código en la cual se determinará si el usuario ganó o perdió. Es decir que mientras el usuario tenga vidas y la palabra no haya sido adivinada éste bucle se ejecutará.
	while vidas and not compara(palabraLista,palabraString):
		
		mostrarLista(palabraLista)

		# Variable que contendrá la letra o la palabra que el jugador cree que corresponde a la palabra a adivinar.
		valorIngresado = input("Ingrese la letra que crea pertenecer a la palabra o la palabra que cree que es la correcta: ")
		
		# Bucle while que verifica que el valor ingresado sea correcto. Si el valor ingresado no es válido se mantiene dentro del bucle hasta que ingrese un valor válido.
		while comprueba(valorIngresado) == False:
			print("El valor ingresado es incorrecto, por favor ingrese un nuevo valor")
			valorIngresado = input("Ingrese la letra que crea pertenecer a la palabra o la palabra que cree que es la correcta: ")

		# Si el jugador acierta la letra o la palabra eso se reemplazará en la lista de guiones, en caso contrario el jugador perderá una vida.
		if buscar(valorIngresado):
			reemplazar(valorIngresado, palabraString, palabraLista)
		else:
			vidas-=1
			print("Perdiste una vida\nCantidad de vidas: ", vidas)

	# Para finalizar el juego se imprimirá por pantalla si el jugador ganó (salió del bucle while con vidas) o si perdió (si salió sin vidas).
	if vidas != 0:
		print("YOU WIN!!!")
	else:
		print("GAME OVER")

# Aquí se almacenará la palabra que se deberá adivinar.
palabraString = input("Ingrese la palabra que desee ser adivinada: ")
# Declaramos una lista vacía que posteriormente contendrá guiones, uno por cada letra de la palabra.
palabraLista =[]
# Llamamos a la función jugar, la cual contiene todas las llamadas a las demás funciones necesarias para el desarrollo del juego.
jugar()