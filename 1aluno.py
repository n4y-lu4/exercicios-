#registro d aluno

nome=input("nome do usuario:")
idade = float(input("idade do usuario:"))
altura=float(input("altura do usuario:"))
nota1=float(input("primeira nota:"))
nota2=float(input("segunda nota:"))

#media do aluno
media=(nota1+nota2)/2

#situação final
if media >=6:
    print(f'media {media}:congratulations!')
else :
    print(f"media{media}:moggado")
print(nome,idade,altura)

