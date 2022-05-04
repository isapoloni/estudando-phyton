nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print ('A soma vale {}, o produto é {}, e a divisão é {:.3f}'.format(n1+n2, n1*n2, n1/n2), end=' ')
print('Divisão inteira {} e potencia {}'.format(n1//n2, n1**n2))


# anotações da aula 
    # print // {:20} ->  quantidade em caracteres(espaços) | {:.3f} o f é de "flutuante" para determinar casas decimais // *alinhamentos* (> a direita) (< a esquerda) (^ ao centro) // *quebras de linha* (\n quebrar a linha) (end='' não quebrar a linha)

#desafio-tabuada

n = int(input('Qual tabuada vc quer aprender? '))
print(' 1 x {} = {} \n 2 x {} = {} \n 3 x {} = {} \n 4 x {} = {} \n 5 x {} = {} \n 6 x {} = {} \n 7 x {} = {} \n 8 x {} = {} \n 9 x {} = {} \n 10 x {} = {}'.format(n, 1 * n, n, 2 * n, n, 3*n, n, 4*n, n, 5*n, n, 6*n, n, 7*n, n, 8*n, n, 9*n, n, 10*n))