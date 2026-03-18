#17/03/25
doce = ["uva","brigadeiro","bolo","bala"]            #posição <y>

#localização de tal coisa
print("primeiro doce:", doce[0]) #uva
print("ultimo doce:",doce[-1]) #bala

#alterando elementos
doce[1] = "doce de uva"
doce[2]= input("escrever:")
print("alteração:",doce)

#adc elementos
doce.append("doce de morango")   
doce.append("kiwi")                      #adiciona no final
doce.insert(4, "casadinho")           #adiciona <x> na posição y 
print(f'apos add:{doce}')


#removendo 
doce.remove("casadinho")
doce.remove("bala")
doce.remove("uva")
doce.pop()
print(f"remover {doce}")

#quantidade de elementos
print("tamanho da lista 'doce':",len(doce))

#dividir
print(("fatiamento [0:2]:",doce[0:2]))

#verificar o item na lista 
print("tem  'doce de damasco'?","doce de damasco" in doce)
