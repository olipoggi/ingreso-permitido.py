#Paso 1: SOlicitar al usuario que ingrese la edad

edad =int(input("Por favor, ingresá tu edad: "))

#Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca

permitido = True if edad >= 18 else False #Ternario

#Paso 3: Mostrar al usuario si su cliente puede o no entrar a la discoteca

if permitido:
    print("Podes pasar")
else:
    print("no podes siendo menor")