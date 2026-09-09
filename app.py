# Programa de Cálculo de média de notas
# Autor: Gilson Moraes

# Entrada
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite e primeira nota: "))
nota2 = float(input("Digite e segunda nota: "))

#Processamento
media = (nota1 + nota2) / 2

# Saida
print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")

if media >= 6:
    print("Situação: Aprovado")
else: 
    print("Situação: Reprovado"