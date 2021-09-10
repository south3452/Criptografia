'''
Lucas Venancio Coutinho
Atividade Development For Security
'''
import string
import time
import sys
global variacao

#Cores do Terminal
reset_color = "\033[0m"
warning = '\033[93m'
ok = '\033[92m'
header = '\033[95m'

#Pegando informações
while True:
    try:
        variacao = int(input('insira qual vai ser a variação da cifra: '))
        break
    except:
        print('Insira apenas numeros')


#salvando o alfabeto em lista
alfabeto = string.printable
alfabeto = list(alfabeto)

def doisemum(params):
    #Abrindo e lendo o arquivo
    arquivo = open("teste.txt", "r")
    file = arquivo.read()
    arquivo.close()

    newlist = list()

    #Aplicando a cifra e salvando em uma lista 
    for x in range(len(file)):
        for y in file[x]:
            if y == ' ':
                newlist.append(' ')
            elif y == '\n':
                newlist.append('\n')
            else:
                #des é de descriptografar
                if params == 'des':
                    cifra = (ord(y) - variacao)
                else:
                    cifra = (ord(y) + variacao)
                newlist.append(chr(cifra))
    #abrir e escrever o conteudo no arquivo
    arquivo = open('teste.txt', 'w')
    arquivo.write(''.join(newlist))
    arquivo.close()

#deixar o terminal bonito
def carregamento():
    for x in range(5):
        sys.stdout.write('\rCarregando   ')
        time.sleep(0.5)
        sys.stdout.write('\rCarregando.')
        time.sleep(0.3)    
        sys.stdout.write('\rCarregando..')
        time.sleep(0.3)
        sys.stdout.write('\rCarregando...')
        time.sleep(0.3)
        if x == 4:
            sys.stdout.write('\n')

#Modificando o arquivo alvo e avisando o usuario
doisemum('')
print(warning + 'Seu arquivo foi Criptografado, pague agora que será descriptografado.' + reset_color)

#variaveis para controle
var = variacao
variacao = 1 
tanto = 0

while True:    
    pagou = input('Pagou? (Sim/Não): ').upper()
    if pagou == 'SIM' or pagou == 'S':
        variacao = tanto + var
        doisemum('des')
        carregamento()
        print(ok + "Arquivo recuperado" + reset_color)
        break
    elif pagou == 'NAO' or pagou == 'N':
        tanto += 1
        print("Então pague ou não terá o arquivo de volta")
        print(warning + 'PS: Seu arquivo acabou de "ganhar" mais um nivel de criptografia' + reset_color)
        doisemum('')
    else:
        print('Coloque apenas Sim ou Nao')