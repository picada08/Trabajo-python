a=input('Ingrese el primer numero: ')
b=input('Ingrese el segundo numero: ')
if(int(a)>int(b)):
	c=2*int(a)
	d=int(b)/2
	print('El doble del mayor es: '+str(c))
	print('La mitad del menor es: '+str(d))
if(int(a)<int(b)):
	h=2*int(b)
	j=int(a)/2
	print('El doble del mayor es: '+str(h))
	print('La mitad del menor es: '+str(j))
if(int(a)==int(b)):
	print('Los numeros que ingreso son iguales')
