import random
import string

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

print("p: ",p)
print("q: ",q)
print("n: ",n)
print("phi de n: ",phi)
print("e: ",e)
print("d:", d)


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
        try:
            cifrada.append(str(((alfa.index(i)) ** e) % n) + ' ')
        except ValueError:
            alfa.append(i)
            cifrada.append(str(((alfa.index(i)) ** e) % n) + ' ')

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
for i in cifrada:
    if i == '\n':
        decifrada.append('\n')
    else:
        conta = (int(i)**d) % n
        decifrada.append(alfa[conta])

input("CALMA LÁ")

arquivo = open('teste.txt', 'w')
arquivo.write(''.join(decifrada))
arquivo.close()
