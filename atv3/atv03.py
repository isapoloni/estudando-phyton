print('-------Empresa cara de pau-------')
pessoas = int(input('Quantas pessoas participaram do processo? :'))
print('Certo! vamos cadastrar as respostas agora.')

resps = 0
respn = 0
respfs = 0 
respmn = 0    
contador = 0
while contador < pessoas: 
    contador = contador + 1
    print('=====================')
    sexo = str(input('M/F: '))
    idade = int(input('Idade: '))
    resposta = str(input('S=sim, N=não, I=indiferente: '))

    if resposta =='S':
        resps = resps + 1
    else:
        respn = respn + 1
    
    if sexo =='M' and resposta == 'N':
        respmn = respmn + 1
    
    if sexo == 'F' and resposta == 'S':
        respfs = respfs + 1
    

print('Quantas pessoas foram entrevistadas: {}'.format(pessoas))
print('Quantas pessoas disseram sim: {}'.format(resps))
print('Quantas pessoas disseram não: {}'.format(respn))
print('Quantas mulheres disseram sim: {} e quantos homens disseram não {}.'.format(respfs, respmn))
