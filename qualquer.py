#entrada de dados 
peso = float(input("seu peso (exeplo:30,5):"))

altura = float(input("sua altura (exemplo:1.70):"))

#calculo do imc
imc=peso/(altura**2)

#condições
if imc < 18.5:
    classificação = "magro"
elif imc <25 : 
    classificação ="ideal"
else: 
    classificação = "acima do peso"

#saida(resultado)
print (f"imc = {imc:.2f} - {classificação} ")
