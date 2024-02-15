nota_ava = float(input("Digite sua nota do ava:\n"))
nota_prova = float(input("Digite sua nota da prova:\n"))

media = (nota_ava * 0.4) + (nota_prova * 0.6)

print("Sua media foi:", media)

if media >= 5:
    print("Você foi aprovado, PARABENS!")
else:
    print("Você reprovou")