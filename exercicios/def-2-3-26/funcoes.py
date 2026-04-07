def nome (abacate):
    print(f'bem vindo,{abacate}')
nome("seu pedro")
nome("amanda")

def soma (a,b):
    print(a+b)
soma(1,5)

def par (a ):
    if a %2 == 0:
        return 'par'
    else:
        return 'impar'
#par(4)
print(f"o valor {par(3)}")

def qualMaior():
    numeros = []
    for i in range(5):
        numeros.append(float(input('Numero: ')))
    return max(numeros)
 
def ContadorLetras():
    valor = input('nome: ')
    print(len(valor))
 
def qualMedia():
    numeros = []
    for i in range(3):
        numeros.append(float(input('Numero: ')))
    return sum(numeros)/len(numeros)
 
def palindromo(palavra):
    if palavra == palavra[::-1]:
        return 'é'
    else:
        return 'num é'