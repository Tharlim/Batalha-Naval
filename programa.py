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

FO = { # frota do Oponente
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

T=funcoes.posiciona_frota(F)
TO=funcoes.posiciona_frota(FO)
J=[] #jogadas

print(funcoes.monta_tabuleiros(T,TO))
while True:

    a=int(input('Jogador, qual linha deseja atacar? '))
    while a not in range (10):
        print('Linha inválida!')
        a=int(input('Jogador, qual linha deseja atacar? '))
    b=int(input('Jogador, qual coluna deseja atacar? '))
    while b not in range (10):
        print('Coluna inválida!')
        b=int(input('Jogador, qual coluna deseja atacar? '))

    if [a,b] in J:
        print(f'A posição linha {a} e coluna {b} já foi informada anteriormente!')
    else:
        J.append([a,b])
        funcoes.faz_jogada(TO,a,b)
        if funcoes.afundados(FO,TO) == 10:
            break
        print(funcoes.monta_tabuleiros(T,TO))

print('Parabéns! Você derrubou todos os navios do seu oponente!')
