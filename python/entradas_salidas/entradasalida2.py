from functools import reduce
numeros = [1,2,3,4,5,6,7,8,9]

def funcion(listanumeros): 
    res = list(filter((lambda x: x % 2), listanumeros )) 
    print(res)
    res = reduce( (lambda x, y: x + y), listanumeros) 
    print(res)


funcion(numeros)