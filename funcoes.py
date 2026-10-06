def define_posicoes(x,y,o,l):
    # x = linha, y = coluna, o = orientação, l= tamanho
    A=[]
    
    if o == 'horizontal':
        for i in range(l):
            A.append([x,y+i])
    if o == 'vertical':
        for i in range(l):
            A.append([x+i,y])

    return A

def preenche_frota(A,n,x,y,o,l):
    # A= frota atual, x = linha, y = coluna, o = orientação, l= tamanho, n= nome da frota

    if n not in A:
        A[n]=[define_posicoes(x,y,o,l)]
    else:
        A[n].append(define_posicoes(x,y,o,l))

    return A

def faz_jogada(T,x,y):
    # T= tabuleiro, x = linha, y = coluna
    if T[x][y] == 0:
        T[x][y] = '-'
    if T[x][y] == 1:
        T[x][y] = 'X'

    return T