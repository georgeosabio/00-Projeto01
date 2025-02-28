
CONSTANTE_BONUS = 1000

# Solicite o nome do usuário
nome_usuario = input("Digite o seu nome: ")

# Insira o valor do seu salário
salario_usuario = float(input("Digite o seu salário: "))

# Solicite a porcentagem do bônus recebido pelo usuário
bonus_usuario = float(input("Digite o seu bonus: "))

valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# O cálculo do KPI do bônus de 2024 é de `1000 + salario * bônus`
print(f"O usuario {nome_usuario} possui o bonus de {valor_bonus}!")


# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".