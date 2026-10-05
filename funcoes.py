def define_posicoes(a,b,c,d):
    # a = linha, b = coluna, c = orientação, d= tamanho
    A=[[a,b]]
    
    if c == 'horizontal':
        for i in range(1,d,1):
            A.append([a,b+i])         
    if c == 'vertical':
        for i in range(1,d,1):
            A.append([a+i,b])  

    return A
