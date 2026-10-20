# Bloco 1
'''

1
print("Hellow, Word")

'''

'''

2
idade = 15
nome = "felipe"
altura = 1.75

print(idade, nome, altura)

'''

'''

3
nome = input("Digite seu nome: ")
print("Olá, " + nome)
'''

'''

4
idade = input("Digite sua idade: ")
print("vc tem " + idade + " anos")
'''

'''

5
vlr1 = int(input("Digite um valor: "))
vlr2 = int(input("Digite outro valor: "))
print(vlr1 + vlr2)
'''

'''

6
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um valor: "))
print(valor1 + valor2)
print(valor1 - valor2)
print(valor1 * valor2)
print(valor1 / valor2)
'''

'''

7
multi = float(input("Digite um valor; "))
dobro = multi * 2
print("Esse é o dobro do valor digitado ",6 + dobro )
'''

'''

8
valor = int(input("Digite o valor: "))
triplo = valor * 3
metade = valor / 2
print("Triplo: ", + triplo)
print("Metade:", + metade)
'''

'''

9
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print(nome + " " + sobrenome)
'''

'''

10
ano = int(input("Digite o ano do seu nascimento: "))
idade = 2026 - ano
print(f"vc tem aproximadamente {idade} anos" )
'''

'''

11
metro = int(input("Digite quantos metro vc quer "))
cm = metro * 100
mm = metro * 1000
print(f"{cm} cm")
print(f"{mm} mm")
'''

'''

12
minutos = int(input("Digite quantos minutos vc quer "))
seg = minutos * 60
print(f"{seg} segundos")
'''

'''

13
horas = int(input("Digite quantas horas vc quer "))
min = horas * 60
print(f"{min} minutos")
'''

'''

14
cel = int(input("Digite quantos graus "))
fahrenheit = cel * 9 / 5 + 32
print(f"A temperatura é {fahrenheit}")
'''

'''

15
real = float(input("Digite quantos reais vc tem "))
dolar = 5
dolares = real / dolar
print(f"vc tem US$ {dolares:.2f}")
'''

# bloco 2
'''

16
quadrado = int(input("Digite o valor "))
lado = quadrado * quadrado
print(f"Sua area é {lado}")
'''

'''

17
altura = int(input("Digite a altura "))
largura = int(input("Digite a largura "))
ret = largura * altura
print(f"A area do retangulo é {ret}")
'''

'''

18
base = int(input("Digite a base "))
altura = int(input("Digite a altura "))
resu = base * altura / 2
print(f"A area do triangulo é {resu:.2f}")
'''

'''

19
raio = int(input("Digite o valor da raio: "))
area = 3.14 * raio ** 2
print(f"O valor da sua area é {area}")
'''

'''

20
largura = int(input("Digite a largura "))
altura = int(input("Digite a altura "))
perimetro = 2 * (altura + largura)
print(f"O perímetro do retângulo é {perimetro}")
'''

'''

21
nota1 = int(input("Digite a primeira nota "))
nota2 = int(input("Digite a segunda nota "))
nota3 = int(input("Digite a terceira nota "))
notas = (nota1 + nota2 + nota3) / 3
print(f"A média das notas são {notas}")
'''

'''

22
hora = float(input("Digite o valor recebido por hora: "))
horas = float(input("Digite o número de horas trabalhadas no mês: "))
salario = hora * horas
print(f"O salário bruto é R$ {salario:.2f}")
'''

'''

23
salario = int(input("Digite seu salario: "))
aumento = salario * 0.10
novo_salario = salario + aumento
print(f"Seu salario é {salario}")
print(f"Seu novo aumento é de {aumento}")
print(f"Seu novo salario é {novo_salario}")
'''

'''

24
valor = int(input("Digite o valor "))
porc = valor * 0.15
final = valor - porc
print(f"desconto {porc}")
print(f"valor final {final}")
'''

'''

25
valor_compra = float(input("Digite o valor da compra "))
parcelas = int(input("Digite quantas parcelas vai ser "))
total = valor_compra / parcelas
print(f"valor de cada parcela {total}")
'''

'''

26
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / altura ** 2
print(f"Seu IMC é {imc}")
'''

'''

27
nota1 = int(input("Digite o valor "))
nota2 = int(input("Digite o valor "))
total = (nota1 * 2 + nota2 * 3) / 5
print(f"O total é {total}")
'''

'''

28
valor1 = int(input("Digite o valor "))
valor2 = int(input("Digite o valor "))
quociente = valor1 // valor2
resto = valor1 % valor2
print(f"O quociente é {quociente}")
print(f"O resto é {resto}")
'''

'''

29
valor = int(input("Digite o valor "))
ant = valor - 1
suc = valor + 1
print(f"O antecessor é {ant}")
print(f"O sucessor é {suc}")
'''

'''

30
base = int(input("Digite a base "))
expoente = int(input("Digite o expoente "))
calculo = base ** expoente
print(f"Sua potencia é {calculo}")
'''

# Bloco 3
'''

31
numero = int(input("Digite um numero: "))

if numero >0:
print("Seu numero é positivo")
elif numero < 0:
print("Seu numero é negativo")
else:
print("Seu numero é zero")
'''

'''

32
idade = int(input("Digite sua idade: "))

if idade >= 18:
print("Pode beber")
else:
print("Não pode beber")
'''

'''

33
numero = int(input("Digite um numero: "))

if numero % 2 == 0:
print("Seu numero é par")
else:
print("Seu numero é impar")
'''

'''

34
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if n1 > n2:
print(f"O maior numero é {n1}")
elif n2 > n1:
print(f"O maior numero é {n2}")
else:
print("Os numeros são iguais")
'''

'''

35
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

if n1 > n2 and n1 > n3:
print(f"O maior é {n1}")
elif n2 > n1 and n2 > n3:
print(f"O maior é {n2}")
else:
print(f"O maior é {n3}")
'''

'''

36
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

if n1 < n2 and n1 < n3:
print(f"O menor é {n1}")
elif n2 < n1 and n2 < n3:
print(f"O menor é {n2}")
else:
print(f"O menor é {n3}")
'''

'''

37
media = int(input("Digite a media: "))

if media >= 6:
print("Aprovado")
else:
print("Reprovado")
'''

'''

38
media = int(input("Digite a media: "))

if media >= 7:
print("Aprovado")
elif media < 7 and media >= 5:
print("Recuperação")
else:
print("Reprovado")
'''

'''

39
idade = int(input("Digite sua idade: "))

if idade <= 11:
print("Criança")
elif idade > 11 and idade <= 17:
print("Adolescente")
elif idade > 18 and idade <= 59:
print("Adulto")
else:
print("idoso")
'''

'''

40
senha = int(input("Digite sua senha: "))
senha_final = 1234

if senha == senha_final:
print("Senha correta")
else:
print("Senha incorreta")
'''

'''

41
login = int(input("Digite seu login: "))
senha = int(input("Digite sua senha: "))

login_final = 123
senha_final = 1234

if login == login_final and senha == senha_final:
print("Sucesso")
else:
print("Não aprovado")
'''

'''

42
n1 = int(input("Digite um numero: "))

if n1 % 5 == 0:
print("Multiplo de 5")
else:
print("Não multiplo")
'''

'''

43
n1 = int(input("Digite um numero: "))

if n1 % 3 == 0 and n1 % 5 ==0:
print("O número é divisível por 3 e por 5.")
else:
print("O número não é por 3 e por 5.")
'''

'''

44
n1 = int(input("Digite o ano: "))

if n1 % 4 == 0:
print("Ano bissexto")
else:
print("Não é ano bissexto")
'''

'''

45
compra = int(input("Digite o valor: "))

if compra >= 200:
desconto = compra * 0.10
final = compra - desconto
print(f"O valor é: R$ {final:.2f}")
else:
print(f"Não tem desconto, o valor ficou: R$ {compra}")
'''

'''

46
valor = int(input("Digite o valor: "))
frete = 20

if valor >= 150:
print("Frete grátis")
else:
print(f"O valor ficou: R${frete}")
'''

'''

47
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
op = input("Digite a operação (+, -, * ou /): ")

if op == "+":
resultado = n1 + n2
print(f"{resultado}")
elif op == "-":
resultado = n1 - n2
print(f"{resultado}")
elif op == "*":
resultado = n1 * n2
print(f"{resultado}")
elif op == "/":
if n2 == 0:
print("Não é possivel dividir por 0")
else:
resultado = n1 / n2
print(f"{resultado}")
else:
print("Operação invalida")
'''

'''

48
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
print("Os lados podem formar um triângulo.")
else:
print("Os lados não podem formar um triângulo.")
'''

'''

49
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:

if lado1 == lado2 and lado2 == lado3:
    print("O triângulo é equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno")
else:
print("Esses lados não podem formar um triângulo.")
'''

'''

50
salario = float(input("Digite o valor: "))

if salario <= 2000:
print("Não tem impostos")
elif salario <= 4000:
result = salario * 0.10
salariorest = salario - result
print(f"Seus impostos é: {result:.2f}")
print(f"O resto do salario é de R${salariorest:.2f}")
else:
result = salario * 0.20
salariorest = salario - result
print(f"Seus impostos é {result:.2f}")
print(f"O resto do salario é de R${salariorest:.2f}")
'''

# Bloco 4
'''

51
contador = 0

for contador in range(10):
contador += 1
print(f"{contador}")
'''

'''

52
for numero in range(10, -1, -1):
print(numero)
print("Fim")
'''

'''

53
for numero in range(0, 101, 2):
print(numero)
'''

'''

54
for numero in range(1, 100, 2):
print(numero)
'''

'''

55
numero = int(input("Digite um numero: "))

for multi in range(1, 11):
resu = numero * multi
print(f"{numero} x {multi} = {resu}")
'''

'''

56
numero = int(input("Digite um numero: "))
soma = 0

for fim in range(1, numero, +1):
soma = soma + 1
print(f"A soma é de {soma}")
'''

'''

57
numero = int(input("Digite um numero não negativo: "))
fatorial = 1

for i in range(1, numero + 1):
fatorial = fatorial * i
print(f"O fatorial de {numero} é {fatorial}")
'''

'''

58
pares = 0

for i in range(10):
numero = int(input("Digite um numero: "))

numero % 2 == 0
pares += 1
print(f"Numeros pares {pares}")
'''

'''

59
posi = 0

for i in range(10):
numero = float(input("Digite um numero: "))

if numero > 0:
    posi += numero
print(f"o resultado é {posi:.2f}")
'''

'''

60
maior = None

for i in range(5):
numero = int(input("Digite um numero: "))

if maior == None or numero > maior:
    maior = numero
print(f"O maior numero digitado é {maior}")
'''

'''

61
menor = None

for i in range(5):
numero = float(input("Digite um numero: "))

if menor is None or numero < menor:
    menor = numero
print(f"Esse é o menor numero {menor}")
'''

'''

62
notas = 0

for i in range(5):
nt = float(input("Digite um numero: "))
notas += nt
media = notas / 5

print(f"A media é {media:.2f}")
'''

'''

63
senha = ''

while (senha != 1234):
senha = int(input("Digite a senha: "))
print("Parabens")
'''

'''

64
numero = int(input("Digite um numero positivo: "))

while numero <= 0:
numero = float(input("Digite um numero: "))
print("Parabens")
'''

'''

65
opcao = -1

while opcao != 0:
print("\n Menu")
print("1- Olá")
print("2- Bom-dia")
print("0- Sair")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    print("Olá")
elif opcao == 2:
    print("Bom-dia")
elif opcao == 0:
    print("Saindo")
else:
    print("Opção invalida")
'''

'''

66
soma = 0
numero = float(input("Digite um numero: "))

while numero != 0:
soma += numero
numero = float(input("Digite um numero: "))

print(f"A soma de todos os numeros é {soma}")
'''

'''

67
soma = 0
quantidade = 0

numero = float(input("Digite uma nota (-1 pra sair): "))

while numero != -1:
soma += numero
quantidade += 1

numero = float(input("Digite uma nota (-1 pra sair): "))
if quantidade > 0:
media = soma / quantidade
print(f"As notas válidas são {quantidade} e a média é {media:.2f}")
else:
print("Nenhuma nota válida foi digitada")
'''

'''

68
secreto = 3
numero = int(input("Digite um numero: "))

while numero != 3:
numero = int(input("Digite um numero: "))

if numero < 3:
    print("Maior")
elif numero > 3:
    print("Menor")
else:
    print("Você acertou")
'''

'''

69
numero = int(input("Digite um numero: "))
primo = True

for i in range(2, numero):
if numero % i == 0:
primo = False

if primo:
print("é primo")
else:
print("Não é primo")
'''

'''

70
inicio = int(input("Digite o primeiro numero: "))
fim = int(input("Digite o segundo numero: "))

for numero in range(inicio, fim + 1):
if numero < 2:

primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False

if primo:
    print(numero)
'''

# Bloco 5
'''

71
pala = "Ela tem não sei quantas caracteres"
quant = len(pala)
print(f"{pala} tem {quant} caracteres")
'''

'''

72
frase = input("Digite algo ")

mai = frase.upper()
minu = frase.lower()

print(f"Maiusculas {mai} e minusculas {minu}")
'''

'''

73
digite = input("Digite algo ")

print(f"O primeiro {digite[0]} ultimo {digite[-1]}")
'''

'''

74
digite = input("Digite algo ")
cont = digite.lower().count("a")

print(f"a letra A apareceu {cont}")
'''

'''

75
digite = input("Digite algo ")
digite = digite.lower()

if digite == digite[::-1]:
print("É um palidromo")
else:
print("Não é um palidromo")
'''

'''
#76
digite = input("Digite algo: ")
inv = digite[::-1]

print(f"{inv}")
'''

'''

77
digite = input("Digite algo: ")
digite = digite.split()

for digite in digite:
print(f"{digite}")
'''

'''

78
digite = input("Digite algo: ")
digite = digite.split()
quant = len(digite)

print(f"Tem {quant} palavras")
'''

'''

79
digite = input("Digite algo: ")
digite_novo = input("Digite a palavra que deseja substituir: ")
novo = input("Digite a nova palavra: ")

nv = digite.replace(digite_novo, novo)
print(f"Nova frase: {nv}")
'''

'''

80
email = input("Digite seu e-mail: ")

if "@" in email and "." in email[email.find("@"):]:
print("E-mail válido!")
else:
print("E-mail inválido!")
'''

'''
# 81
lista = ["maria", "ana", "carlos", "raphael", "felipe"]

for i in lista:
    print(i)
'''

'''
# 82
lista = []

for i in range(5):
    nome = input("Digite seu nome: ")
    lista.append(nome)
print(lista)
'''

'''
# 83
lista_num = [1, 7, 4, 6, 4]
soma = 0

for numero in lista_num:
    soma += numero
    result = soma
print(result)
'''

'''
# 84
lista_num = [1, 7, 4, 6, 4]
maior = 0

for i in lista_num:
    if i > maior:
        maior = i
print(maior)
'''

'''
# 85
lista_num = [1, 7, 4, 6, 4]
menor = lista_num[0]

for i in lista_num:
    if i < menor:
        menor = i
print(menor)
'''

'''
# 86
notas = []
quantidade = 0
soma = 0

for i in range(5):
    media = int(input("Digite as notas: "))
    quantidade += 1
    soma += media

    resultado = soma / quantidade
print(f"{resultado}")
'''

'''
# 87
lista = []
lista_par = []

for i in range(10):
    numeros = int(input("Digite os numeros: "))

    if numeros % 2 == 0:
        lista_par.append(numeros)
else:
    print("Não tem numeros pares")
print(f"Numeros pares {lista_par}")
'''

'''
# 88
lista_nome = ["maria", "ana", "carlos", "raphael", "felipe"]

for i in range(5):
    remov = input("Escreva um nome: ")

    if remov in lista_nome:
        lista_nome.remove(remov)
        print(f"Nome removido")
    else:
        print("Esse nome não existe")
'''

'''
# 89
lista = []

for i in range(5):
    add = input("Digite o produto: ")
    lista.append(add)

produto = input("Digite o produto que deseja procurar: ")

if produto in lista:
    print("Produto encontrado")
else:
    print("Este produto não foi encontrado")
'''

'''
# 90
lista = []

for i in range(6):
    numeros = input("Digite seus numeros: ")
    lista.append(numeros)

lista.sort()
print(f"Do menor para o maior: {lista}")
print(f"Do maior para o menor: {lista[::-1]}")
'''

'''
# 91
lista = set()

for i in range(10):
    numeros = input("Digite 10 numeros: ")

    lista.add(numeros)
print(lista)
'''

'''
# 92
conj = {1,2,3,4,5,6}
conj2 = {2,7,8,9,1}
conj3 = conj & conj2
print(f"{conj3}")
'''

'''
# 93
tup = (15,22)
print(f"x {tup[0]}, y {tup[1]}")
'''

'''
# 94
chaves = {
    "nome": "Felipe",
    "cidade": "Uberlandia",
    "idade": "15"
}

print(f"{chaves}")
'''

'''
# 95
dados = {
    "nome": "",
    "media": ""
}


novonome = input("Digite seu nome: ")
novanota = float(input("DIgit sua nota: "))
novanota2 = float(input("DIgit sua nota: "))

dados["nome"] = novonome

dados["media"] = (novanota + novanota2) / 2

print(dados)
'''

'''
# 96
dados = {}
lista = []


dados["nome"] = input("Digite o nome do prouto: ")
dados["preco"] = float(input("Digite o valor: "))
lista.append(dados.copy())

dados["nome"] = input("Digite o nome do prouto: ")
dados["preco"] = float(input("Digite o valor: "))
lista.append(dados.copy())

dados["nome"] = input("Digite o nome do prouto: ")
dados["preco"] = float(input("Digite o valor: "))
lista.append(dados.copy())

for i in range(3):
    print(lista[i])
'''

'''
# 97
dados = {}
lista = []

dados["nome"] = input("Digite o nome do prouto: ")
dados["preco"] = float(input("Digite o valor: "))
lista.append(dados.copy())

dados["nome"] = input("Digite o nome do prouto: ")
dados["preco"] = float(input("Digite o valor: "))
lista.append(dados.copy())

dados["nome"] = input("Digite o nome do prouto: ")
dados["preco"] = float(input("Digite o valor: "))
lista.append(dados.copy())

maior = lista[0]

for produto in lista:
    if produto["preco"] > maior["preco"]:
        maior = produto
print(f"O maior preço é {maior["preco"]}")
'''

'''
# 98
list = {
    "gestor": "34984289524",
    "senac": "34999999999",
    "davi": "34888888888"
}

nome = input("digite o nome da pessoa: ")

if nome in list:
    print(f"Telefone {nome}: {list[nome]}")
else:
    print("pessoa não encontrada")
'''

'''
# 99
digite = input("Digite alguma frase: ")

pala = digite.lower().split()
cont = {}

for palavra in pala:
    if palavra in cont:
        cont[palavra] += 1
    else:
        cont[palavra] = 1
print(cont)
'''

'''
# 100
estoq = {
    "arroz": 20,
    "feijao": 10,
    "pc": 30
}

nomeprod = input("Digite o nome do produto: ")
quant = int(input("Digite a quantidade de produto: "))

if nomeprod in estoq:
    if quant <= estoq[nomeprod]:
        estoq[nomeprod] -= quant
        print(f"retirada realizada, a quantidade de sobra atual é: {estoq[nomeprod]}")
    else:
        print(f"Não tem estoque")
else:
    print("Não encontrei esse produto")
print(f"A quantidade atual é {estoq}")
'''

'''
# 101
def saudacao():
    print("Bem-vindo ao programa!")
saudacao()
'''

'''
# 102
def nome(name):
    print(f"Bom dia, {name}")
nome("Felipe")
'''

'''
# 103
def soma(x,y):
    print(x+y)
soma(5,6)
'''

'''
# 104
def maior(x,y):
    if x > y:
        print(f"O maior numero é {x}")
    elif x < y:
        print(f"O maior é {y}")
    else:
        print(f"O maior é {x}")
maior(5,3)
'''

'''
# 105
def numero(x):
    if x % 2 == 0:
        print(f"O numero é par")
    else:
        print("O numero é impar")

x = int(input("Digite o primeiro numero "))

numero(x)
'''

'''
# 106
def nota(x,y,z):
    print(f"a média é: {(x + y + z) / 3}")


y = int(input("Digite a segunda nota "))
z = int(input("Digite a terceira nota "))

nota(x,y,z)
'''

'''
# 107
def retangulo(altura,largura):
    print(f"Area do retangulo é {(altura * largura)}")

altura = int(input("Digite a altura "))
largura = int(input("Digite a largura "))

retangulo(altura,largura)
'''

'''
# 108
def cel(fa):
    print(f"Fahrenheit {(fa * 9 / 5 + 32)}")
fa = int(input("Digite os graus: "))
cel(fa)
'''


'''
# 109
def fatorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


n = int(input("Digite um numero não negativo: "))

print(fatorial(n))
'''

'''
# 110
def primo(p):
    if p < 2:
        return False

    for i in range(2, p):
        if p % i == 0:
            return False

    return True

p = int(input("Digite um numero primo: "))

if primo(p):
    print("É primo")
else:
    print("Não é primo")
'''

'''
# 111
def vogal(v):
    contador = 0

    for letra in v:
        if letra.lower() in "aeiou":
            contador += 1

    return contador


frase = input("Digite algo: ")

print(f"Quantidade de vogais: {vogal(frase)}")
'''

'''
# 112
def maior(mai):
    maior = mai[0]

    for numero in mai:
        if numero > maior:
            maior = numero

    return maior

numero = [1,3,5,6,2,5]

print(maior(numero))
'''

'''
# 113
def media(x,y,z,a,b):
    
    print(f"a média é: {(x + y + z + a + b) / 5}")

x = int(input("Digite a primeira nota "))
y = int(input("Digite a segunda nota "))
z = int(input("Digite a terceira nota "))
a = int(input("Digite a quarta nota "))
b = int(input("Digite a quinta nota "))


media(x,y,z,a,b)
'''

'''
# 114
def posi(p):
    positivo = []
    for numero in p:
        if numero > 0:
            positivo.append(numero)

    return positivo

numeros = [-1, 5, 6, 0, -3, 7]
print(f"{posi(numeros)}")
'''


# 115
def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def divisao(a,b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"


print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = int(input("Escolha uma opção: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:
    print(f"Resultado: {somar(num1, num2)}")
elif opcao == 2:
    print(f"Resultado: {subtrair(num1, num2)}")
elif opcao == 3:
    print(f"Resultado: {multiplicar(num1, num2)}")
elif opcao == 4:
    print(f"Resultado: {divisao(num1, num2)}")
else:
    print("Opção inválida!")