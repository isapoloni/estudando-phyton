carro = list()


for cont in range(0, 3):
    nomecarro = str(input('Nome do carro: '))
    kmpl = int(input('Quantos km ele faz por litro?: '))
    litros = float((500 / kmpl))
    reais = float((litros * 4.90))
    carro.append([nomecarro, kmpl, litros, reais])

for cont in range(0,3): 
    print('O carro: {0}, que faz {1} Km/L, consome {2:.2f}L em 500km e terá um gasto de R${3:.2f}'.format(carro[cont][0], carro[cont][1], carro[cont][2], carro[cont][3]))
        
    
    
# conta ( 500 / Km por L ) -> vai dar o resultado de "litros" / conta (litros * 4.90) -> vai dar o resultado gasto em reais


