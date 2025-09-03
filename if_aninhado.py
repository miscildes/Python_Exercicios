peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = (peso / (altura ** 2))

if (imc >= 25):
    print(imc, "Poxa, você já está em risco.")
    if (imc >= 25 and imc <= 29.9):
        print("Você tem sobrepeso")
    elif (imc >= 30 and imc <= 39.9):
        print('Sua obesidade é mórbida')
    elif (imc >= 40):
        print ('Voce tem sérios riscos de morte')

else :
    print(imc, 'Seu peso é abaixo do saudável. ')
