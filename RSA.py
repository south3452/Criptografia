import random
import string

#Cores do Terminal
reset_color = "\033[0m"
red = "\033[31m"

#definir numeros aleatórios
def randomnumber():
    while 1:
        w = list(str(random.random()))[2]
        x = list(str(random.random()))[2]
        y = list(str(random.random()))[2]
        z = list(str(random.random()))[2]
        if int(x) and int(y) and int(w) and int(z) > 0:
            if x != y:
                return int(w)+int(x),int(y)+int(z)

#pegar 2 primos
def doisprimos():
    dois = randomnumber()
    lista = list()
    fim = 10000
    while 1:
        try:
            for x in range(2, fim):
                i = 2
                while i < x: 
                    if(x%i) == 0:
                        break
                    i+=1
                else:
                    lista.append(x)
            while 1:
                return lista[dois[0]*dois[0]], lista[dois[1]*dois[1]]
        except IndexError:
            fim+=1000
#verificar se os numeros são primos entre si
def primosentresi(a,b):
    diva = list() 
    divb = list()
    for i in range(1, a+1):
        if (a%i) == 0:
            diva.append(i)

    for i in range(1, b+1):
        if (b%i) == 0:
            divb.append(i)
    for i in diva:
        try:
            if divb.index(i):
                return False
        except:
            for x in divb:
                try:
                    if diva.index(x):
                        return False
                except:
                    return True

def verificaprimos(a):
    i = 2
    while i < a: 
        if(a%i) == 0:
            return False
        i+=1
    else:
        return True


print("Quer escolher os primos ou deixar eles gerarem aleatoriamente?")
print("OBS: os numeros gerados aleatoriamente podem ser grandes quanto maior o numero mais demorado o cálculo para criptografar/desciptografar variando de CPU para CPU")
print("1) Inserir primos")
print("2) Gerar aleatórios")

while 1:
    try:
        while 1:
            escolha = int(input("Escolha uma opção:"))
            if escolha == 1 or escolha == 2: 
                break
            else: 
                print(red + 'Escolha apenas 1 ou 2' + reset_color)
        break
    except:
        print(red + 'Escolha apenas numeros' + reset_color )

if escolha == 1:
    while 1:
        p = int(input("Insira um numero primo:"))
        if verificaprimos(p) == True:
            break
        else:
            print(red + "O numero ",p, "não é primo!" + reset_color)
            print(red + "Escolha um numero que é primo" + reset_color)
    while 1:
        q = int(input("Insira um numero primo:"))
        if verificaprimos(q) == True:
            break
        else:
            print(red + "O numero ",q, "não é primo!" + reset_color)
            print(red + "Escolha um numero que é primo" + reset_color)
else:
    #definir valor de dois primos
    num = doisprimos()
    #definir valor de p
    p = num[0]
    #definir valor de q
    q = num[1]
    #se p e q forem iguais mudar os valores para ficarem diferentes
    while 1:
        if p == q:
            q = doisprimos()[0]
        else:
            break

#Definir valor de n 
n = p*q

#Calcule a Função totiente de Euler em n
phi = (p-1)*(q-1)

#Escolha um inteiro 'e' tal que 1 < e < phi(n) de forma que o 'e' e phi(n) sejam relativamente primos entre si.
while 1:
    e = randomnumber()[1]
    if e > 1:
        if e < phi:
            if primosentresi(e, phi) == True:
                break

#Escolha d tal que e*d mod phi(N) = 1
#Achar d
def achad(e, totiente):
    i = 1
    while True:
        if(e * i % totiente == 1):
            return i
        i+=1 

d = achad(e,phi)

print(20*"-")
print('Chave Publica(n,e)')
print(f'A chave publica é: {n},{e}')
print('Chave Privada(d)')
print(f'A chave privada é: {d}')


arquivo = open("teste.txt", "r")
file = arquivo.read()
arquivo.close()

#file = list('testea,.[^ ')
alfa = list(string.printable)
cifrada = list()

file = list(file)

#cifrar mensagem
for i in file:
    if i == '\n':
        cifrada.append('\n')
    else:
        cifrada.append(chr(((ord(i)) ** e) % n))

print("Seu aquivo foi Criptografado, de uma olhada nele")

'''
arquivo = open('teste.txt', 'w')
arquivo.write(''.join(str(cifrada)))
arquivo.close()
'''

arquivo = open('teste.txt', 'w')
arquivo.write(''.join(cifrada))
arquivo.close()

decifrada = list()

#decifrar mensagem
arquivo = open("teste.txt", "r")
file = arquivo.read()
arquivo.close()

for i in file:
    if i == '\n':
        decifrada.append('\n')
    else:
        conta = (ord(i)**d) % n
        decifrada.append(chr(conta))

input("Aperte [ENTER] para descptografar o arquivo")

arquivo = open('teste.txt', 'w')
arquivo.write(''.join(decifrada))
arquivo.close()
