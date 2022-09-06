frase = input("Ingrese la frase a analizar: ")
letra1 = input("Ingrese una letra: ").lower()
letra2 = input("Ingrese otra letra: ").lower()
letra3 = input("Ingrese una última letra: ").lower()

print("La letra "+ letra1 + " aparece " +  str(frase.lower().count(letra1)) + " veces")
print("La letra "+ letra2 + " aparece " +  str(frase.lower().count(letra2)) + " veces")
print("La letra "+ letra3 + " aparece " +  str(frase.lower().count(letra3)) + " veces")
print("La primera letra de la frase es '" + frase[0]  + "' y la última letra de la frase es '"+ frase[-1]+"'")
print("La frase tiene " + str(len(frase.split())) + " palabras")
lfrase = frase.split()
lfrase.reverse()
print("Al revés: '"+ " ".join(lfrase) +"'")
if ('python' in frase.split()):
    print("La palabra 'python' sí aparece" )
else:
    print("La palabra 'python' no aparece" )
