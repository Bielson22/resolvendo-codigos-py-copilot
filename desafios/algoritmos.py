# 1. Concatenando Dados
info1 = input("Digite a primeira informação: ")
info2 = input("Digite a segunda informação: ")
print(f"Informações combinadas: {info1} {info2}")

# 2. Repetindo Textos
texto = input("Digite um texto: ")
vezes = int(input("Quantas vezes deseja repetir? "))
print((texto + " ") * vezes)

# 3. Operações Matemáticas Simples
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == '+': print(num1 + num2)
elif operacao == '-': print(num1 - num2)
elif operacao == '*': print(num1 * num2)
elif operacao == '/': print(num1 / num2)
else: print("Operação inválida")
