#01 Calculadora simples

print("=== Calculadora ===")
print("Operações disponíveis: +, -, *, /")

num1 = float(input("Digite o primeiro número: "))
operador = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro! Divisão por zero."
else:
    resultado = "Operador inválido!"

print("Resultado:", resultado)


#02 Notas e média da turma

qtd_alunos = int(input("Quantos alunos tem na turma? "))
soma_notas = 0

for i in range(qtd_alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma_notas += nota

media = soma_notas / qtd_alunos
print(f"A média da turma é {media:.2f}")


#03 Verificação de senha

senha = input("Digite uma senha: ")

tem_numero = any(char.isdigit() for char in senha)  # verifica se tem número

if len(senha) >= 8 and tem_numero:
    print("Senha válida!")
else:
    print("Senha inválida! Deve ter pelo menos 8 caracteres e conter um número.")
    


#04 Analisador de números pares e ímpares

pares = 0
impares = 0

while True:
    numero = input("Digite um número (ou 'sair' para encerrar): ")

    if numero.lower() == "sair":
        break

    numero = int(numero)
    if numero % 2 == 0:
        pares += 1
        print(f"{numero} é par")
    else:
        impares += 1
        print(f"{numero} é ímpar")

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)


