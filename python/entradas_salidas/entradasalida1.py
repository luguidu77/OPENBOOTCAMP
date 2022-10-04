paises = []
entrada = []
unicos = []

print('Ingresa varios paises separados por comas :')
entrada = input().split(',')
ordena = entrada.sort()
unicos = set(entrada)
paises = list(unicos)
paises.sort()

print('Paises ordenados alfabeticamente :')
print(', '.join(map(str.capitalize, paises)))
