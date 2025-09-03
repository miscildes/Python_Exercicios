idade = int(input('Digite sua idade: '))

if (idade >= 18):
    print(idade, 'Você é maior de idade.')

elif (idade >= 13 and idade <= 17) :
    print(idade, 'Você é adolescente')

else:
    print(idade, 'Você é uma criança')