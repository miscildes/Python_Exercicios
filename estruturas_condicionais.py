nota_1 = float(input("Digite a primeira nota "))
nota_2 = float(input("Digite a segunda nota "))
nota_3 = float(input("Digite a terceira nota "))

soma = (nota_1 + nota_2 + nota_3)
media = (soma / 3)

if (media >= 6) :
    print(media)
    print("Aprovado")

if (media <= 5.9) :
    print(media)
    print("Reprovado")