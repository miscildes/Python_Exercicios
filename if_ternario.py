grana = float(input('Digite quanto você tem na conta: '))
gasto = float(input('Digite quanto você tem de gastos: '))

saude_financeira = 'Verde' if gasto < grana else 'Vermelho'

print('Sua saúde financeira está:' ,saude_financeira)