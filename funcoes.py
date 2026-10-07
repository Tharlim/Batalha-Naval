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

def preenche_frota(F,n,x,y,o,l):
    # F= frota atual, x = linha, y = coluna, o = orientação, l= tamanho, n= nome da frota

    if n not in F:
        F[n]=[define_posicoes(x,y,o,l)]
    else:
        F[n].append(define_posicoes(x,y,o,l))

    return F

def faz_jogada(T,x,y):
    # T= tabuleiro, x = linha, y = coluna
    if T[x][y] == 0:
        T[x][y] = '-'
    if T[x][y] == 1:
        T[x][y] = 'X'

    return T

def posiciona_frota(F):
    T=[]
    for i in range(10):
        T.append([])
        for j in range(10):
            T[i].append(0)

    for i in F.values():
        for j in i:
            for x,y in j:
                T[x][y] = 1

    return T

def afundados(F,T):
    a=0 # numero de navios afundados 
    k=0 # contador
    for i in F.values():
        for j in i:
            k=0
            for x,y in j:
                if T[x][y] == 'X':
                    k+=1
            if k == len(j):
                a+=1
    return a

def posicao_valida(F,x,y,o,l):
    A = define_posicoes(x,y,o,l)
    for i in F.values():
        for j in i:
            for k in A:
                if k in j:
                    return False
    for x1,y1 in A:
        if x1>9 or x1<0:
            return False
        if y1>9 or y1<0:
            return False
    return True
