# exercio 1 (média)
print("A média dos números 8,9 e 7 é: ", (8+9+7)/3)
print("A média dos números 4, 5 e 6 é: ", (4+5+6)/3)
print("A soma das duas médias é: ", 8+5)
print("Já a média das médias é: ", (8+5)/2)

# exercio 2 (multiplicação de tesxto)
nome = input("Digete o seu nome: ")
print(nome*10)

# exercio 3 (antecessor e sucessor)
num = int(input("Digite um número inteiro: "))
print("O antecessor de", num,"é", num-1, ",e o seu sucessor é", num+1)

# exercio 4 (reajuste em %)
num2 = float(input("Digite um valor qualquer: "))
reajuste = num2*10/100
print("O valor teve um reajuste positivo de 10%, então o valor novo é de:", num2+reajuste)

# exercio 5 (média)
inteiro = int(input("Digete o primeiro número inteiro: "))
inteiro2 = int(input("Digete o segundo número inteiro: "))
inteiro3 = int(input("Digete o terceiro número inteiro: "))
print("A média dos três números digitados é: ", (inteiro+inteiro2+inteiro3)/3)

# exerecio 6 (numero elevado)
num3 = int(input("Digite um número inteiro: "))
print("O número informado elevado ao quadrado é: ", num3**2)

# exercio 7 (reajuste em %)
num4 = float(input("Digite um número qualquer: "))
reajuste2 = num4*1/100
print("Ouve um reajuste negativo de 1%, o valor passou a ser: ",num4-reajuste2)

# exercio 8 (reajuste em %)
preço = float(input("Digete o preço de uma calça na sua cidade: "))
desconto = preço*9/100
print("Na nossa loja online, essa calça sai a: ",preço-desconto)

# exercio 9 (salario liquido)
hora = float(input("Professor, digite o valor que recebe por hora de aula: "))
aulas = float(input("Diga quantas aulas o senhor faz: "))
inss = float(input("E quantos porcentos é descontado no seu INSS?: "))
desconto_inss = (hora*aulas)*inss/100
print("Seu sálario líquido é de: ",(hora*aulas)-desconto_inss)

# exercio 10 (Gruas para Fahrenheit)
graus = float(input("Digite o a temperatura (em graus) atual na sua ciadade: "))
print("Essa temperatura equivale a ", 1.8*graus+32, "em Fahrenheit.")

# exercio 11 (if, elif e else)
num5 = float(input("Digite um número: "))
if num5 > 20:
    print(num5/2)

# exercio 12 (if, elif e else)
num_int1 = int(input("Digite o primeiro número inteiro: "))
num_int2 = int(input("Digite o segundo número inteiro: "))
if num_int1+num_int2 > 10:
    print(num_int1+num_int2)

# exercio 13 (if, elif e else)
num_ale = float(input("Digite um número: "))
if num_ale >= 0:
    print(num_ale**1/2)
else:
    print(num_ale**2)

# exercio 14 (if, elif e else)
salario = float(input("Digite o seu sálario: "))
prestaçao = float(input("Digite a prestação: "))
if prestaçao > salario*20/100:
    print("Empréstimo não pode ser concedido.")
else:
    print("empréstimo pode ser concedido.")

# exercio 15 (if, elif e else)
num6 = float(input("Digite um número: "))
if num6 > 20:
    print(num6, "> 20")
elif num6 == 20:
    print(num6, "= 20")
else:
    print(num6, "< 20")

# exrcio 16 (calcular idade)
nasc = int(input("Digite seu ano de nascmineto: "))
ano = int(input("Digite o ano atual: "))
print("Sua idade é: ", ano-nasc)

# exercio 17 (ler inferior e superior e mostrar apenas os números pares e soma-los)