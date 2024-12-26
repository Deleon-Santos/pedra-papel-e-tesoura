from random import randint 

vitoria = []
limite_jogada= 0
jogando= True
resultado =[]


def buscar_jogada(escolha):
    global limite_jogada
    jogada = 'pedra' if escolha == '1' else 'papel' if escolha == '2' else 'tesoura'
    return jogada 

def vitorias():
    if vitoria[0]=='pedra':
        ganhou = "you_loose" if vitoria[1]=='papel' else 'empaty' if vitoria[1]=='pedra' else 'you_win'
        resultado.append(ganhou)
        print(ganhou)
        vitoria.clear()
        return
    
    elif vitoria[0]=='papel':
        ganhou = "empaty" if vitoria[1]=='papel' else 'you_win' if vitoria[1]=='pedra' else 'you_loose'
        resultado.append(ganhou)
        print(ganhou)
        vitoria.clear()
        return
    
    elif vitoria[0]=='tesoura':
        ganhou = "you_win" if vitoria[1]=='papel' else 'you_loose' if vitoria[1]=='pedra' else 'empaty'
        resultado.append(ganhou)
        print(ganhou)
        vitoria.clear()
        return
    
def contar_resultado():
    contagem = {'you_win': 0, 'you_loose': 0, 'empaty': 0}
    for resultados in resultado:
        contagem[resultados] += 1
    return contagem

print('Vamos Jogar'.center(25,'*'))
print('1-Pedra 2-Papel 3-Tesoura'.center(16))
while limite_jogada < 6:
    
    if jogando:
        you = input('\nfaça sua jogada :')
        if you not in '1/2/3':
            print('Jogada Invalida')
            continue
        jogada = buscar_jogada(you)
        vitoria.append(jogada)
        jogando= False
        limite_jogada+=1
        print(f'Sua Jogada foi :{jogada}')
        continue
    else:
        com = str (randint(1, 3))
        jogada = buscar_jogada(com)
        vitoria.append(jogada)
        jogando = True
        print(f'A maquina Escolheu :{jogada}')
        vitorias()
        continue

print(f"\nTerminamos um ciclo de {limite_jogada/2:.0f} jogadas e temos o resultado")
contagem= contar_resultado()
for k,i in contagem.items():
    print(f"{k} : {i}")
print('\nFim')