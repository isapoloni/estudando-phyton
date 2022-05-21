carros = list()

for cont in range(0, 3):
    nomecarro = str(input('Nome do carro: '))
    kmpl = int(input('Quantos km ele faz por litro?: '))
    litros = (500 / kmpl)
    reais = (litros * 4.90)
    carros.append([nomecarro, kmpl, litros, reais])  
     
print(carros)






    
# conta ( 500 / Km por L ) -> vai dar o resultado de "litros" / conta (litros * 4.90) -> vai dar o resultado de


