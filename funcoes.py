def define_posicoes(a,b,c,d):
    # a = linha, b = coluna, c = orientação, d= tamanho
    A=[]
    
    if c == 'horizontal':
        for i in range(d):
            A.append([a,b+i])         
    if c == 'vertical':
        for i in range(d):
            A.append([a+i,b])  

    return A
def preenche_frota(A,n,a,b,c,d):
    # A= frota atual, a = linha, b = coluna, c = orientação, d= tamanho, n= nome da frota
    if n not in A:
        A[n]=[define_posicoes(a,b,c,d)]
    else:
        A[n].append(define_posicoes(a,b,c,d))
    return A