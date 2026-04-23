# Desafio 3: Operações Matemáticas Simples
# Descrição: Solicitar dois números e realizar uma operação simples entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Qual operação deseja realizar? (+, -, *, /): ")

if operacao == '+':
    print(f"Resultado: {num1 + num2}")
elif operacao == '-':
    print(f"Resultado: {num1 - num2}")
elif operacao == '*':
    print(f"Resultado: {num1 * num2}")
elif operacao == '/':
    if num2 != 0:
        print(f"Resultado: {num1 / num2}")
    else:
        print("Erro: Divisão por zero!")
else:
    print("Operação inválida!")
