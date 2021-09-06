import string
import time
import sys
global variacao

#Pegando informações
while True:
    try:
        variacao = int(input('insira qual vai ser a variação da cifra: '))
        break
    except:
        print('Insira apenas numeros')


#salvando o alfabeto em lista
alfabeto = string.ascii_lowercase
Alfabeto = string.ascii_uppercase
pontos = string.punctuation
num = string.digits


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
                try:
                    #des é de descriptografar
                    if params == 'des':
                        cifra = (alfabeto.index(y) - variacao) % 26
                    else:
                        cifra = (alfabeto.index(y) + variacao) % 26
                    newlist.append(alfabeto[cifra])
                except ValueError:
                    try:
                        if params == 'des':
                            cifra = (Alfabeto.index(y) - variacao) % 26
                        else:
                            cifra = (Alfabeto.index(y) + variacao) % 26
                        newlist.append(Alfabeto[cifra])
                    except ValueError:
                        try:
                            if params == 'des':
                                cifra = (pontos.index(y) - variacao) % 32
                            else:
                                cifra = (pontos.index(y) + variacao) % 32
                            newlist.append(pontos[cifra])
                        except ValueError:
                            try:
                                if params == 'des':
                                    cifra = (num.index(y) - variacao) % 10
                                else:
                                    cifra = (num.index(y) + variacao) % 10
                                newlist.append(num[cifra])
                            except:
                                print("Teste")
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
print('Seu arquivo foi Criptografado, pague agora que será descriptografado.')

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
        print("Arquivo recuperado")
        break
    elif pagou == 'NAO' or pagou == 'N':
        tanto += 1
        print("Então pague ou não terá o arquivo de volta")
        print('PS: Seu arquivo acabou de "ganhar" mais um nivel de criptografia')
        doisemum('')
    else:
        print('Coloque apenas Sim ou Nao')