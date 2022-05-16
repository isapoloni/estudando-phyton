
print('-------Empresa cara de pau-------')
pessoas = int(input('Quantas pessoas participaram do processo? :'))
print('Certo! vamos cadastrar as respostas agora.')
print('Observações:  O sexo e a resposta devem ser usados somente os caracteres pedidos, para que o sistema funcione!')

resps = 0
respn = 0
respi = 0
respfs = 0 
respmn = 0    
contador = 0
while contador < pessoas: 
    contador = contador + 1
    print('=====================')
    sexo = str(input('M/F: ')).upper()
    idade = int(input('Idade:'))
    resposta = str(input('S=sim, N=não, I=indiferente: ')).upper()

    if resposta =='S':
        resps = resps + 1

    elif resposta == 'N':
        respn = respn + 1

    elif resposta == 'I':
        respi = respi + 1
    
    if sexo =='M' and resposta == 'N':
        respmn = respmn + 1
    
    if sexo == 'F' and resposta == 'S':
        respfs = respfs + 1
    
print('=====================')
print('Quantas pessoas foram entrevistadas: {}'.format(pessoas))
print('Quantas pessoas disseram sim: {}'.format(resps))
print('Quantas pessoas disseram não: {}'.format(respn))
print('Quantas pessoas disseram indiferente: {}'.format(respi))
print('Quantas mulheres disseram sim: {} e quantos homens disseram não {}.'.format(respfs, respmn))
