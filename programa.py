import funcoes
F={}
N=['porta-aviões','navio-tanque','contratorpedeiro','submarino']
for i in range(len(N)):
    for j in range(i+1):
        while True:
            print(f'Insira as informações referentes ao navio {N[i]} que possui tamanho {4-i}')
            x=int(input('Linha: '))
            y=int(input('coluna: '))

            if i!=3:
                o=int(input("[1] Vertical [2] Horizontal >"))
                if o == 1:
                    o = 'vertical'
                if o == 2:
                    o = 'horizontal'

            if i==3:
                o= 'vertical'

            if funcoes.posicao_valida(F,x,y,o,(4-i)):
                F = funcoes.preenche_frota(F,N[i],x,y,o,(4-i))
                break
            else:
                print('Esta posição não está válida!')
print(F)
