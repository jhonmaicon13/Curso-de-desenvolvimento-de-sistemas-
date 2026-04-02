nota1 = int(input("Digite a nota do 1° Bimestre: "))
nota2 = int(input("Digite a nota do 2° Bimestre: "))
nota3 = int(input("Digite a nota do 3° Bimestre: "))
nota4 = int(input("Digite a nota do 4° Bimestre: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print("Sua média é: ", media)
if media >= 6:
    print("Aprovavdo(a)")
elif media >= 4:
    print("Recuperação")
else:
    print("Reprovado(a)")        